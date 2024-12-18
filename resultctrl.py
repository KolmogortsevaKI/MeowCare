import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QMessageBox, QWidget
from PyQt5.QtCore import Qt, QModelIndex

from petdb import dbPet
from tabmodel import *
from resultdialog import Ui_ResultDlg

class ResDialog(QDialog,Ui_ResultDlg):
    def  __init__(self,  window, diagID):
        super(ResDialog, self).__init__(window)
        self.diagID=diagID
        self.setWindowModality(Qt.WindowModality.WindowModal)
        self.setWindowTitle("Results")
        self.parent=window
        self.setupUi(window)
        self.btnCheck.setVisible(False)
        #--------------------------------------------------------- Cats
        res=dbPet.select("SELECT R.id, D.title, "+
            "R.presence,R.probability,R.disease_id "+
            "FROM Result R "+
            "left join Diseases D on R.disease_id=D.id "+
            f"where diagnostics_id={self.diagID}")

        self.tabRes=TableModel(res,["Disease","Presence","Probabilty"])
        self.gridResult.setModel(self.tabRes)
        self.gridResult.setItemDelegateForColumn(1, ResultDelegate())  # Assuming Gender is in column 3


        # # Connect events
        # self.gridCat.clicked.connect(self.gridCatChange)
        # self.gridDiag.clicked.connect(self.gridDiagChange)
        
        self.gridResult.clicked.connect(self.gridChange)
        self.btnCheck.clicked.connect(self.checkClick)
        self.btnBack.clicked.connect(self.backClick)

    def checkClick(self):
        print("CHECK CLICK!!!")

    def backClick(self):
        self.accept()
        self.parent.close()
    # ---------------------------------------------------------------------- setImage
    def setImage(self,id): 
        res=dbPet.one("Diseases",f"id={id}","img") 
        #print("ID:",id,res) +D+
        if res==None: 
            self.imgDisease.clear()
            return
        pix=QtGui.QPixmap()
        pix.loadFromData(res[0],"JPEG")
            # pix.save("Model/bumpy.jpg") # Export +D+
        # print("PIX:",pix.isNull()) # +D+
        self.imgDisease.resize(400, 400)
        self.imgDisease.setPixmap(pix)

    def gridChange(self, index: QModelIndex):
        row = index.row()
        self.setImage(self.tabRes.getData(row,4))
