# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\resultdialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ResultDlg(object):
    def setupUi(self, ResultDlg):
        ResultDlg.setObjectName("ResultDlg")
        ResultDlg.resize(720, 357)
        self.verticalLayout = QtWidgets.QVBoxLayout(ResultDlg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridResult = QtWidgets.QTableView(ResultDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridResult.sizePolicy().hasHeightForWidth())
        self.gridResult.setSizePolicy(sizePolicy)
        self.gridResult.setObjectName("gridResult")
        self.gridResult.verticalHeader().setVisible(False)
        self.horizontalLayout_2.addWidget(self.gridResult)
        self.scrollImage = QtWidgets.QScrollArea(ResultDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollImage.sizePolicy().hasHeightForWidth())
        self.scrollImage.setSizePolicy(sizePolicy)
        self.scrollImage.setWidgetResizable(True)
        self.scrollImage.setObjectName("scrollImage")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 418, 279))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.imgDisease = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imgDisease.sizePolicy().hasHeightForWidth())
        self.imgDisease.setSizePolicy(sizePolicy)
        self.imgDisease.setMinimumSize(QtCore.QSize(400, 0))
        self.imgDisease.setObjectName("imgDisease")
        self.horizontalLayout_3.addWidget(self.imgDisease)
        self.scrollImage.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.addWidget(self.scrollImage)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnCheck = QtWidgets.QPushButton(ResultDlg)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnCheck.setFont(font)
        self.btnCheck.setObjectName("btnCheck")
        self.horizontalLayout.addWidget(self.btnCheck)
        self.btnBack = QtWidgets.QPushButton(ResultDlg)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnBack.setFont(font)
        self.btnBack.setObjectName("btnBack")
        self.horizontalLayout.addWidget(self.btnBack)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ResultDlg)
        QtCore.QMetaObject.connectSlotsByName(ResultDlg)

    def retranslateUi(self, ResultDlg):
        _translate = QtCore.QCoreApplication.translate
        ResultDlg.setWindowTitle(_translate("ResultDlg", "Dialog"))
        self.imgDisease.setText(_translate("ResultDlg", "N/A"))
        self.btnCheck.setText(_translate("ResultDlg", "Check"))
        self.btnBack.setText(_translate("ResultDlg", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ResultDlg = QtWidgets.QDialog()
    ui = Ui_ResultDlg()
    ui.setupUi(ResultDlg)
    ResultDlg.show()
    sys.exit(app.exec_())
