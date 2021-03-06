# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Principal.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from registro import Ui_Crear
from listado import Ui_Listar
import geocoder, requests, json

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(396, 242)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 20, 205, 170))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(30, 0, 30, 15)
        self.verticalLayout_2.setSpacing(16)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.titulo = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo.setObjectName("titulo")
        self.verticalLayout_2.addWidget(self.titulo)
        self.button_registrar = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.button_registrar.setFont(font)
        self.button_registrar.setAutoFillBackground(False)
        self.button_registrar.setObjectName("button_registrar")
        self.verticalLayout_2.addWidget(self.button_registrar, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.button_listar = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.button_listar.setFont(font)
        self.button_listar.setObjectName("button_listar")
        self.verticalLayout_2.addWidget(self.button_listar, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Funcionalidades para la interfaz
        self.button_listar.clicked.connect(self.abrir_listar)
        self.button_registrar.clicked.connect(self.abrir_crear)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titulo.setText(_translate("MainWindow", "Cliente"))
        self.button_registrar.setText(_translate("MainWindow", "Registrar Persona"))
        self.button_listar.setText(_translate("MainWindow", "Listado de Personas"))

    def abrir_crear(self):
        self.crearUI = QtWidgets.QDialog()
        myloc = geocoder.ip('me')
        self.ui = Ui_Crear()
        self.ui.setupUi(self.crearUI, myloc.latlng) #Planeo agregar cliente como argumento
        self.crearUI.show()

    def abrir_listar(self):
        self.listarUI = QtWidgets.QMainWindow()
        self.ui = Ui_Listar()
        self.ui.setupUi(self.listarUI) #Planeo agregar cliente como argumento
        self.listarUI.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
