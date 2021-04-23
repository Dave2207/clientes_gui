import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.titulo = QtWidgets.QLabel("Cliente")
        self.button_crear = QtWidgets.QPushButton("Registrar Persona")
        self.button_listar = QtWidgets.QPushButton("Listado de Personas")

        self.layout = QtWidgets.QVBoxLayout()
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(22)
        self.layout.addWidget(self.titulo, alignment=QtCore.Qt.AlignTop)
        self.layout.addWidget(self.button_crear, alignment=QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.button_listar, alignment=QtCore.Qt.AlignCenter)
    
        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()
    sys.exit(app.exec_())