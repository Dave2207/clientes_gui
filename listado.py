# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout_listar.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import requests, json
from zeep import Client

class Ui_Listar(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(629, 737)
        font = QtGui.QFont()
        font.setFamily("Arial")
        Dialog.setFont(font)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(150, 20, 300, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_buscar = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_buscar.setObjectName("btn_buscar")
        self.gridLayout.addWidget(self.btn_buscar, 3, 2, 1, 2)
        self.btn_listarTodos = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_listarTodos.sizePolicy().hasHeightForWidth())
        self.btn_listarTodos.setSizePolicy(sizePolicy)
        self.btn_listarTodos.setObjectName("btn_listarTodos")
        self.gridLayout.addWidget(self.btn_listarTodos, 4, 0, 1, 4, QtCore.Qt.AlignHCenter)
        self.lbl_buscarID = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_buscarID.setObjectName("lbl_buscarID")
        self.gridLayout.addWidget(self.lbl_buscarID, 3, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.lbl_listado = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_listado.setFont(font)
        self.lbl_listado.setObjectName("lbl_listado")
        self.gridLayout.addWidget(self.lbl_listado, 1, 0, 1, 4, QtCore.Qt.AlignHCenter)
        self.spn_id = QtWidgets.QSpinBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spn_id.sizePolicy().hasHeightForWidth())
        self.spn_id.setSizePolicy(sizePolicy)
        self.spn_id.setMinimum(1)
        self.spn_id.setMaximum(10000)
        self.spn_id.setObjectName("spn_id")
        self.gridLayout.addWidget(self.spn_id, 3, 1, 1, 1)
        self.lbl_usuario = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_usuario.setObjectName("lbl_usuario")
        self.gridLayout.addWidget(self.lbl_usuario, 2, 0, 1, 1)
        self.spn_usuario = QtWidgets.QSpinBox(self.layoutWidget)
        self.spn_usuario.setMinimum(1)
        self.spn_usuario.setObjectName("spn_usuario")
        self.gridLayout.addWidget(self.spn_usuario, 2, 1, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(490, 40, 101, 91))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rdbtn_REST_listar = QtWidgets.QRadioButton(self.layoutWidget1)
        self.rdbtn_REST_listar.setEnabled(True)
        self.rdbtn_REST_listar.setChecked(True)
        self.rdbtn_REST_listar.setObjectName("rdbtn_REST_listar")
        self.verticalLayout.addWidget(self.rdbtn_REST_listar)
        self.rdbtn_SOAP_listar = QtWidgets.QRadioButton(self.layoutWidget1)
        self.rdbtn_SOAP_listar.setObjectName("rdbtn_SOAP_listar")
        self.verticalLayout.addWidget(self.rdbtn_SOAP_listar)
        self.tabla_listado = QtWidgets.QTableWidget(Dialog)
        self.tabla_listado.setGeometry(QtCore.QRect(10, 180, 601, 531))
        self.tabla_listado.setObjectName("tabla_listado")
        self.tabla_listado.setColumnCount(6)
        self.tabla_listado.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tabla_listado.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_listado.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_listado.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_listado.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_listado.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_listado.setHorizontalHeaderItem(5, item)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #Funcionalidades
        self.btn_buscar.clicked.connect(self.buscarID)
        self.btn_listarTodos.clicked.connect(self.buscarTodos)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_buscar.setText(_translate("Dialog", "Buscar"))
        self.btn_listarTodos.setText(_translate("Dialog", "Listar todos"))
        self.lbl_buscarID.setText(_translate("Dialog", "Buscar por Id:"))
        self.lbl_listado.setText(_translate("Dialog", "Listado de Personas"))
        self.lbl_usuario.setText(_translate("Dialog", "Id. usuario:"))
        self.rdbtn_REST_listar.setText(_translate("Dialog", "REST"))
        self.rdbtn_SOAP_listar.setText(_translate("Dialog", "SOAP"))
        item = self.tabla_listado.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ID"))
        item = self.tabla_listado.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Nombre"))
        item = self.tabla_listado.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Sector"))
        item = self.tabla_listado.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Nivel Educ."))
        item = self.tabla_listado.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Latitud"))
        item = self.tabla_listado.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Longitud"))

    def buscarID(self):
        if self.rdbtn_REST_listar.isChecked() == True:
            url = "http://localhost:7000/REST/"
            req = requests.get(url + str(self.spn_id.value()))
            data = req.json()
            self.tabla_listado.setRowCount(0)
            rowPosition = self.tabla_listado.rowCount()
            self.tabla_listado.insertRow(rowPosition)
            self.tabla_listado.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(data["id"])))
            self.tabla_listado.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(data["nombre"]))
            self.tabla_listado.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(data["sector"]))
            self.tabla_listado.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(data["nivelEscolar"]))
            self.tabla_listado.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(data["ubicacion"]["latitud"]))
            self.tabla_listado.setItem(rowPosition, 5, QtWidgets.QTableWidgetItem(data["ubicacion"]["longitud"]))

        elif self.rdbtn_SOAP_listar.isChecked() == True:
            cli = Client("http://localhost:7000/ws/PersonaWebServices?wsdl")
            persona = cli.service.getPersona(self.spn_id.value())
            persona = json.loads(persona)
            self.tabla_listado.setRowCount(0)
            rowPosition = self.tabla_listado.rowCount()
            self.tabla_listado.insertRow(rowPosition)
            self.tabla_listado.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(persona["id"])))
            self.tabla_listado.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(persona["nombre"]))
            self.tabla_listado.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(persona["sector"]))
            self.tabla_listado.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(persona["nivelEscolar"]))
            self.tabla_listado.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(data["ubicacion"]["latitud"]))
            self.tabla_listado.setItem(rowPosition, 5, QtWidgets.QTableWidgetItem(data["ubicacion"]["longitud"]))

    def buscarTodos(self):
        if self.rdbtn_REST_listar.isChecked() == True:
            url = "http://localhost:7000/REST/"
            req = requests.get(url)
            data = req.json()
            self.tabla_listado.setRowCount(0)
            for j in data:
                rowPosition = self.tabla_listado.rowCount()
                self.tabla_listado.insertRow(rowPosition)
                self.tabla_listado.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(j["id"])))
                self.tabla_listado.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(j["nombre"]))
                self.tabla_listado.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(j["sector"]))
                self.tabla_listado.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(j["nivelEscolar"]))
                self.tabla_listado.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(j["ubicacion"]["latitud"]))
                self.tabla_listado.setItem(rowPosition, 5, QtWidgets.QTableWidgetItem(j["ubicacion"]["longitud"]))
        
        elif self.rdbtn_SOAP_listar.isChecked() == True:
            print('SOAP todos')
            cli = Client("http://localhost:7000/ws/PersonaWebServices?wsdl")
            personas = cli.service.getListaPersona()
            self.tabla_listado.setRowCount(0)
            for p in personas:
                p = json.loads(p)
                rowPosition = self.tabla_listado.rowCount()
                self.tabla_listado.insertRow(rowPosition)
                self.tabla_listado.insertRow(rowPosition)
                self.tabla_listado.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(p["id"])))
                self.tabla_listado.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(p["nombre"]))
                self.tabla_listado.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(p["sector"]))
                self.tabla_listado.setItem(rowPosition, 3, QtWidgets.QTableWidgetItem(p["nivelEscolar"]))
                self.tabla_listado.setItem(rowPosition, 4, QtWidgets.QTableWidgetItem(p["ubicacion"]["latitud"]))
                self.tabla_listado.setItem(rowPosition, 5, QtWidgets.QTableWidgetItem(p["ubicacion"]["longitud"]))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())
