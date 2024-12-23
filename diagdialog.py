# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\diagdialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DiagDlg(object):
    def setupUi(self, DiagDlg):
        DiagDlg.setObjectName("DiagDlg")
        DiagDlg.resize(695, 400)
        self.horizontalLayout = QtWidgets.QHBoxLayout(DiagDlg)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.imgDiag = QtWidgets.QLabel(DiagDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.imgDiag.sizePolicy().hasHeightForWidth())
        self.imgDiag.setSizePolicy(sizePolicy)
        self.imgDiag.setMinimumSize(QtCore.QSize(200, 0))
        self.imgDiag.setBaseSize(QtCore.QSize(400, 0))
        self.imgDiag.setObjectName("imgDiag")
        self.horizontalLayout.addWidget(self.imgDiag)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.calDate = QtWidgets.QCalendarWidget(DiagDlg)
        self.calDate.setObjectName("calDate")
        self.verticalLayout.addWidget(self.calDate)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnLoad = QtWidgets.QPushButton(DiagDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnLoad.sizePolicy().hasHeightForWidth())
        self.btnLoad.setSizePolicy(sizePolicy)
        self.btnLoad.setObjectName("btnLoad")
        self.horizontalLayout_2.addWidget(self.btnLoad)
        self.btnStart = QtWidgets.QPushButton(DiagDlg)
        self.btnStart.setObjectName("btnStart")
        self.horizontalLayout_2.addWidget(self.btnStart)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(DiagDlg)
        QtCore.QMetaObject.connectSlotsByName(DiagDlg)

    def retranslateUi(self, DiagDlg):
        _translate = QtCore.QCoreApplication.translate
        DiagDlg.setWindowTitle(_translate("DiagDlg", "Diagnostics"))
        self.imgDiag.setText(_translate("DiagDlg", "TextLabel"))
        self.btnLoad.setText(_translate("DiagDlg", "Load"))
        self.btnStart.setText(_translate("DiagDlg", "Start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DiagDlg = QtWidgets.QDialog()
    ui = Ui_DiagDlg()
    ui.setupUi(DiagDlg)
    DiagDlg.show()
    sys.exit(app.exec_())
