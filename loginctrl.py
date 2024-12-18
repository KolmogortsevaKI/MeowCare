import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import Qt

from petdb import dbPet
from logindialog import Ui_LoginDlg


class LoginDialog(QDialog,Ui_LoginDlg):
    def  __init__(self,  window):
        super(LoginDialog, self).__init__(window)
        # self.setModal(True)
        self.setWindowModality(Qt.WindowModality.WindowModal)
        self.parent=window
        self.setupUi(window)

        self.editLogin.setText("pups")
        self.editPass.setText("1")
        
        # Connect events
        self.btnLogin.clicked.connect(self.LoginClick)
        self.btnCancel.clicked.connect(self.CancelClick)
        
    def LoginClick(self):
        # res=dbPet.select("Users")
        res=dbPet.one("Users",f"login='{self.editLogin.text()}' and passwd='{self.editPass.text()}'")
        if res==None:
            QMessageBox.warning(self.parent, "Login failed", "Get out of here, sucker!")
            return
        dbPet.User=res
        #self.done(QDialog.DialogCode.Accepted)
        self.accept()
        self.parent.close()

    def CancelClick(self):
        self.reject()
        self.parent.close()

#----------------------------------------------------- L O G I N
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    LoginDlg = QtWidgets.QDialog()
    ui = LoginDialog(LoginDlg)
    LoginDlg.show()
    sys.exit(app.exec_())
