import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QMessageBox, QWidget
from PyQt5.QtCore import Qt

from petdb import dbPet
from catdialog import Ui_CatDlg

class CatDialog(QDialog,Ui_CatDlg):
    def  __init__(self,  window, catID):
        super(CatDialog, self).__init__(window)
        self.catID=catID
        self.setWindowModality(Qt.WindowModality.WindowModal)
        self.parent=window
        self.setupUi(window)

        # Breeds combo
        res=dbPet.all("Breed","Title")
        for s in res:
            self.cbBreed.addItems(s)
        
        # Connect events
        self.btnCancel.clicked.connect(self.cancelClick)
        self.btnSave.clicked.connect(self.saveClick)

    def cancelClick(self):
        # self.setResult(self.rejected)
        self.reject()
        self.parent.close()

    def saveClick(self):
        breedid=0
        if self.rbMale.isChecked():
            gender=True
        else:
            gender=False
        print(self.rbMale.isChecked(),gender)
        res=dbPet.one("Breed",f"title='{self.cbBreed.currentText()}'","id")
        if res!=None:
            breedid=res[0]
        else:
            breedid=None
        
        if self.catID==-1:  # Add cat
            dbPet.insert("Cats","user_id,breed_id,age,gender,nick",
                (dbPet.User[0],breedid,int(self.editAge.text()),
                gender,self.editNick.text()))

        self.accept()
        self.parent.close()
