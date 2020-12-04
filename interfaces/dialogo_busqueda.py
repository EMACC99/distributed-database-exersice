# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogo_busqueda.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(321, 182)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 140, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 140, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.campos = QtWidgets.QComboBox(Dialog)
        self.campos.setGeometry(QtCore.QRect(20, 70, 141, 21))
        self.campos.setObjectName("campos")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(180, 70, 113, 20))
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 50, 61, 16))
        self.label.setObjectName("label")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(70, 100, 171, 21))
        self.checkBox.setObjectName("checkBox")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 10, 121, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Buscar"))
        self.pushButton_2.setText(_translate("Dialog", "Cancelar"))
        self.label.setText(_translate("Dialog", "Atributo"))
        self.checkBox.setText(_translate("Dialog", "Buscar en todas las db"))
        self.label_2.setText(_translate("Dialog", "Buscar por atributo"))

