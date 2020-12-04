# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogo_busqueda_edit.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(321, 191)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 140, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 140, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.campos = QtWidgets.QComboBox(Dialog)
        self.campos.setGeometry(QtCore.QRect(10, 90, 141, 21))
        self.campos.setObjectName("campos")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(170, 90, 113, 20))
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 70, 61, 16))
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(110, 140, 80, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 0, 221, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 20, 261, 20))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Buscar"))
        self.pushButton_2.setText(_translate("Dialog", "Cancelar"))
        self.label.setText(_translate("Dialog", "Atributo"))
        self.pushButton_3.setText(_translate("Dialog", "Editar"))
        self.label_2.setText(_translate("Dialog", "1- Primero busca el registro a editar"))
        self.label_3.setText(_translate("Dialog", "2- Selecciona el atributo a editar y escribe"))

