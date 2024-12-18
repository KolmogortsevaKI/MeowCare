import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QMessageBox, QFileDialog
from PyQt5.QtCore import Qt

from petdb import dbPet
from tabmodel import TableModel
from diagdialog import Ui_DiagDlg

from callmodel import catPredictor

class DiagDialog(QDialog,Ui_DiagDlg):
    def  __init__(self,  window, catID):
        super(DiagDialog, self).__init__(window)
        self.catID=catID
        self.setWindowModality(Qt.WindowModality.WindowModal)
        self.parent=window
        self.setupUi(window)

        #pix = QtGui.QPixmap("Images/default.jpg") # +D+ File!
        pix = QtGui.QPixmap("Images/cat.png") # +D+ File!
        if pix.isNull():
            QMessageBox.error(self, "Error", "Can't open file")
        self.imgDiag.setPixmap(pix)

        self.btnLoad.clicked.connect(self.loadClick)
        self.btnStart.clicked.connect(self.startClick)

    def loadClick(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Open File', './', "Image (*.jpg *jpeg)")
        fimg=open(file,"rb")
        self.img=fimg.read()
        fimg.close()
        pix=QtGui.QPixmap()
        pix.loadFromData(self.img,"JPEG")
        self.imgDiag.setPixmap(pix)
        # print("LOAD: ", file)
        
    def startClick(self):
        cat=dbPet.one("Cats",f"ID={self.catID}")
        if cat==None:
            print(f"Can't find cat {self.CatID}")
            return
        # print(cat)
        # breed=cat[2] +D+
        age=cat[3]
        gender=1.0 if cat[4] else 0.0 # 0 - Male
        cp=catPredictor()
        if not cp.loadmodel("Model/cat_eye_disease_model.h5"):
            print("Load model failed")
            return
        #cp.setimage(self.img) +D+
        res=cp.exec(self.img,age,gender)
        # if res==None:
        #     QMessageBox.error(self, "Error", "Fail to determine")
        #     return
        diagID=dbPet.insert("diagnostics","cat_id,d_date,flag",(self.catID,self.calDate.selectedDate().toPyDate(),0))
        dbPet.insert("image","diagnostics_id,img",(diagID,self.img))
        
        modelDisSq=['Blepharitis', 'Conjunctivitis', 'Corneal Dermoid', 'Non-ulcerative Keratitis', 'Corneal Ulcer', 'Normal']
        n=0 
        for p in res:
            disID=dbPet.one("diseases",f"title like '%{modelDisSq[n]}%'","id")
            if disID!=None: disID=disID[0] 
            # print("ONE: ",n,disID)
            dbPet.insert("result","disease_id,diagnostics_id,presence,probability,class_type",(disID,diagID,1 if (p>0.2) else 0,p.item()*100.0,1))
            n+=1
        QMessageBox.information(self,"Info","Complete")

