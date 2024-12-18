import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtGui import QIcon

from petdb import dbPet
from tabmodel import *
from mainwindow import Ui_MainWindow
from resultctrl import ResDialog
from catctrl import CatDialog
from diagctrl import DiagDialog
from loginctrl import LoginDialog

class MainWindow(QMainWindow,Ui_MainWindow):
    def  __init__(self,  window):
        super(MainWindow, self).__init__(window)
        self.setupUi(window)
        #--------------------------------------------------------- Cats
        # res=dbPet.all("Cats","*",f"user_id={dbPet.User[0]}")
        # res=dbPet.select("SELECT C.id,C.Nick,B.title,age,gender "+
        #                  "FROM Cats C left join Breed B on B.id=C.breed_id "+
        #                  f"where user_id={dbPet.User[0]}")

        # self.tabCat=TableModel(res,["Nick","Breed","Age","Gender"]) # Setup CATS GRID
        # self.gridCat.setModel(self.tabCat)

        hlayout = QtWidgets.QHBoxLayout(self.subFrame)              # Add image frame
        self.imgFrame=uic.loadUi("UI/imgFrame.ui")  # Create image frame
        hlayout.addWidget(self.imgFrame)

        # Connect events
        # self.gridCat.itemSelectionChanged.connect(self.gridCatChange)
        # self.tabCat.dataChanged.connect(self.gridCatEdit) +D+ ???
        self.fillGrid()

        self.gridCat.clicked.connect(self.gridCatChange)
        self.gridDiag.clicked.connect(self.gridDiagChange)
        self.btnAddPet.clicked.connect(self.addPetClick)
        self.btnNewDiag.clicked.connect(self.newDiagClick)
        self.btnCheck.clicked.connect(self.checkClick)

        # self.gridCat.selectRow(0)
        # self.setDiag(self.tabCat.getId(0))

    # --------------------------------------------------- GRIDS & LISTS
    def fillGrid(self):
        res=dbPet.select("SELECT C.id,C.Nick,B.title,age,gender "+
                         "FROM Cats C left join Breed B on B.id=C.breed_id "+
                         f"where user_id={dbPet.User[0]}")

        self.tabCat=TableModel(res,["Nick","Breed","Age","Gender"]) # Setup CATS GRID
        self.gridCat.setModel(self.tabCat)
        self.gridCat.setItemDelegateForColumn(3, GenderDelegate())  # Assuming Gender is in column 3

        self.gridCat.selectRow(0)
        self.setDiag(self.tabCat.getId(0))


    def setDiag(self,id):
        #res=dbPet.select("SELECT id,d_date,flag FROM Diagnostics "+
        res=dbPet.select("SELECT id,d_date FROM Diagnostics "+
                         f"where cat_id={id}")
        #self.tabDiag=TableModel(res,["Date","Flag"])
        self.tabDiag=TableModel(res,["Date"])
        self.gridDiag.setModel(self.tabDiag)
        self.gridDiag.selectRow(0)
        self.setImage(self.tabDiag.getId(0))

    # ---------------------------------------------------------------------- setImage
    def setImage(self,id): 
        res=dbPet.all("Image","img",f"diagnostics_id={id}") # +D+
        # pix = QtGui.QPixmap("Pics/default.jpg") // +D+
        pix=QtGui.QPixmap()
        for i in self.imgFrame.imgLayout.children():    # Clear frame
            self.imgFrame.imgLayout.removeWidget(i)
        for i in reversed(range(self.imgFrame.imgLayout.count())):
            self.imgFrame.imgLayout.itemAt(i).widget().deleteLater()

        for dbimg in res:                       # Add images
            pix.loadFromData(dbimg[0],"JPEG")
            # pix.save("Model/bumpy.jpg") # Export +D+
            # print(pix.isNull()) # +D+
            # self.imgFrame.img.setPixmap(pix)
            img = QtWidgets.QLabel(self.imgFrame.saWidget)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(img.sizePolicy().hasHeightForWidth())
            img.setSizePolicy(sizePolicy)
            img.setBaseSize(QtCore.QSize(400, 400))
            # img.setObjectName("img")
            img.resize(400, 400)
            img.setPixmap(pix)
            self.imgFrame.imgLayout.addWidget(img)
        # pix.loadFromData(res[0],"JPEG")
        # print(pix.isNull()) # +D+
        # self.imgFrame.img.setPixmap(pix)
        # print("PIX SET",pix.size()) // +D+
        # imgList.img.resize(400, 400) // +D+
        
    # --------------------------------------------------- E V E N T S
    # def gridCatEdit(self, index: QModelIndex):
    #     row = index.row()
    #     col = index.column()
    #     value = self.model.data(index, Qt.DisplayRole)
    #     print(f'Cell ({row}, {col}) changed to {value}')

    def gridCatChange(self, index: QModelIndex):
        row = index.row()
        # col = index.column()
        # value = self.tabCat.data(index, Qt.DisplayRole)
        self.setDiag(self.tabCat.getId(row))

    def gridDiagChange(self, index: QModelIndex):
        row = index.row()
        self.setImage(self.tabDiag.getId(row))

    def addPetClick(self):
        catWin = QtWidgets.QDialog()
        ui = CatDialog(catWin,-1)
        catWin.exec()
        self.fillGrid()
        # if catWin.exec_()==QtWidgets.QDialog.accepted():
        #     self.fillGrid()
        #     print("Yaaa")
        
        #print(self.sender())
        # dbPet.insert("Image","image_path,img", ("filename",dbPet.getBLOB("Pics/default.jpg")) ) # insert blob

    #     pix = QtGui.QPixmap("Pics/default.jpg")
    #     if pix.isNull():
    #         QMessageBox.error(self, "Error", "Can't open file")
    #     img = QtWidgets.QLabel(self.imgFrame.saWidget)
    #     sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    #     sizePolicy.setHorizontalStretch(0)
    #     sizePolicy.setVerticalStretch(0)
    #     sizePolicy.setHeightForWidth(img.sizePolicy().hasHeightForWidth())
    #     img.setSizePolicy(sizePolicy)
    #     img.setBaseSize(QtCore.QSize(400, 400))
    #  # img.setObjectName("img")
    #     img.resize(400, 400)
    #     img.setPixmap(pix)
    #     self.imgFrame.imgLayout.addWidget(img)

    def newDiagClick(self):
        row=self.gridCat.currentIndex().row()
        diagWin = QtWidgets.QDialog()
        ui = DiagDialog(diagWin,self.tabCat.getId(row))
        diagWin.exec()
        self.gridCatChange(self.gridCat.currentIndex())

    def checkClick(self):
        row=self.gridDiag.currentIndex().row()
        resWin = QtWidgets.QDialog()
        ui = ResDialog(resWin,self.tabDiag.getId(row))
        resWin.exec()

 #----------------------------------------------------- M A I N
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon("Images/ic_kat.png")) #karina
    if not dbPet.ready:
        exit(0)

    # Login
    LoginDlg = QtWidgets.QDialog()
    ui = LoginDialog(LoginDlg)
    LoginDlg.exec()
    LoginDlg.destroy()
    if dbPet.User==None:
        print("No user")
        sys.exit(1)
#---
    #window = uic.loadUi("UI/mainform.ui")
# -- process: pyuic5 -x UI\mainform.ui.ui -o mainform.py
    window = QtWidgets.QMainWindow()
    ui = MainWindow(window)

#---
    window.show()
    sys.exit(app.exec())
