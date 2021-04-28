# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout_listar.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import requests, json
from texttable import *
from zeep import Client

class Ui_Listar(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Dialog")
        MainWindow.resize(600, 269)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txtUsuario = QtWidgets.QLineEdit(self.centralwidget)
        self.txtUsuario.setGeometry(QtCore.QRect(150, 20, 113, 20))
        self.txtUsuario.setObjectName("txtUsuario")
        self.lblUsuario = QtWidgets.QLabel(self.centralwidget)
        self.lblUsuario.setGeometry(QtCore.QRect(90, 20, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblUsuario.setFont(font)
        self.lblUsuario.setObjectName("lblUsuario")
        self.btnConsultar = QtWidgets.QPushButton(self.centralwidget)
        self.btnConsultar.setGeometry(QtCore.QRect(270, 20, 75, 23))
        self.btnConsultar.setObjectName("btnConsultar")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 60, 580, 171))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setBackgroundVisible(True)
        self.plainTextEdit.setCenterOnScroll(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 469, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #self.btnConsultar.clicked.connect(self.consultar)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Consulta"))
        self.lblUsuario.setText(_translate("MainWindow", "Usuario:"))
        self.btnConsultar.setText(_translate("MainWindow", "Consultar"))

        self.plainTextEdit.setPlainText("+----+-------------------+----------+--------------------+---------+----------+\n"+
                                        "| ID |      NOMBRE       |  SECTOR  |    NIVEL EDUC.     | LATITUD | LONGITUD |\n"+
                                        "+====+===================+==========+====================+=========+==========+\n")

        


    # def consultar(self):
    #     usuario = "admin"

        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
