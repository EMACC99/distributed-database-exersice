# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'insertar_tabla.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(622, 493)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(60, 350, 75, 23))
        self.pushButton.setDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 440, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(390, 440, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(40, 10, 511, 191))
        self.textBrowser.setObjectName("textBrowser")
        self.Columna = QtWidgets.QLineEdit(Dialog)
        self.Columna.setGeometry(QtCore.QRect(10, 300, 113, 20))
        self.Columna.setObjectName("Columna")
        self.keyComboBox = QtWidgets.QComboBox(Dialog)
        self.keyComboBox.setEnabled(False)
        self.keyComboBox.setGeometry(QtCore.QRect(380, 300, 121, 22))
        self.keyComboBox.setObjectName("keyComboBox")
        self.sizeSpinBox = QtWidgets.QSpinBox(Dialog)
        self.sizeSpinBox.setGeometry(QtCore.QRect(230, 300, 42, 22))
        self.sizeSpinBox.setObjectName("sizeSpinBox")
        self.dataType = QtWidgets.QComboBox(Dialog)
        self.dataType.setGeometry(QtCore.QRect(140, 300, 69, 22))
        self.dataType.setObjectName("dataType")
        self.ReferenceTable = QtWidgets.QComboBox(Dialog)
        self.ReferenceTable.setEnabled(False)
        self.ReferenceTable.setGeometry(QtCore.QRect(510, 300, 111, 22))
        self.ReferenceTable.setObjectName("ReferenceTable")
        self.keyCheckBox = QtWidgets.QCheckBox(Dialog)
        self.keyCheckBox.setGeometry(QtCore.QRect(290, 300, 51, 17))
        self.keyCheckBox.setObjectName("keyCheckBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 280, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(140, 270, 61, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(230, 280, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(410, 270, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(510, 270, 101, 16))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Añadir"))
        self.pushButton_2.setText(_translate("Dialog", "Aceptar"))
        self.pushButton_3.setText(_translate("Dialog", "Cancelar"))
        self.keyCheckBox.setText(_translate("Dialog", "key"))
        self.label.setText(_translate("Dialog", "Columna"))
        self.label_2.setText(_translate("Dialog", "Tipo de dato"))
        self.label_3.setText(_translate("Dialog", "Tamaño"))
        self.label_4.setText(_translate("Dialog", "Tipo llave"))
        self.label_5.setText(_translate("Dialog", "Tabla que referencia"))
