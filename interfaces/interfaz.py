# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Prueba SQL.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 629)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 80, 801, 501))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtWidgets.QTableView(self.verticalLayoutWidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.TablecomboBox = QtWidgets.QComboBox(self.centralwidget)
        self.TablecomboBox.setGeometry(QtCore.QRect(160, 20, 151, 20))
        self.TablecomboBox.setStyleSheet("border-style: outset;\n"
"border-width: 2px;\n"
"border-radius:10px;\n"
"border-color:white;\n"
"")
        self.TablecomboBox.setObjectName("TablecomboBox")
        self.DatabaseComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.DatabaseComboBox.setGeometry(QtCore.QRect(0, 20, 151, 20))
        self.DatabaseComboBox.setStyleSheet("border-style: outset;\n"
"border-width: 2px;\n"
"border-radius:10px;\n"
"border-color:white;\n"
"")
        self.DatabaseComboBox.setObjectName("DatabaseComboBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 0, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 0, 47, 16))
        self.label_3.setObjectName("label_3")
        self.LoadTables = QtWidgets.QPushButton(self.centralwidget)
        self.LoadTables.setGeometry(QtCore.QRect(320, 0, 101, 41))
        self.LoadTables.setStyleSheet("background-color:white;\n"
"color:black;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius:10px;\n"
"border-color:white;")
        self.LoadTables.setObjectName("LoadTables")
        self.LoadValues = QtWidgets.QPushButton(self.centralwidget)
        self.LoadValues.setGeometry(QtCore.QRect(10, 50, 131, 23))
        self.LoadValues.setStyleSheet("background-color:white;\n"
"color:black;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius:10px;\n"
"border-color:white;")
        self.LoadValues.setObjectName("LoadValues")
        self.ListAll = QtWidgets.QPushButton(self.centralwidget)
        self.ListAll.setGeometry(QtCore.QRect(190, 50, 91, 23))
        self.ListAll.setStyleSheet("background-color:white;\n"
"color:black;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius:10px;\n"
"border-color:white;")
        self.ListAll.setObjectName("ListAll")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 20))
        self.menubar.setObjectName("menubar")
        self.menuOperaciones = QtWidgets.QMenu(self.menubar)
        self.menuOperaciones.setObjectName("menuOperaciones")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNuevo_Registro = QtWidgets.QAction(MainWindow)
        self.actionNuevo_Registro.setObjectName("actionNuevo_Registro")
        self.actionEditar_Registro = QtWidgets.QAction(MainWindow)
        self.actionEditar_Registro.setObjectName("actionEditar_Registro")
        self.actionBuscar = QtWidgets.QAction(MainWindow)
        self.actionBuscar.setObjectName("actionBuscar")
        self.actionNueva_Tabla = QtWidgets.QAction(MainWindow)
        self.actionNueva_Tabla.setObjectName("actionNueva_Tabla")
        self.menuOperaciones.addAction(self.actionNuevo_Registro)
        self.menuOperaciones.addAction(self.actionEditar_Registro)
        self.menuOperaciones.addAction(self.actionNueva_Tabla)
        self.menuOperaciones.addAction(self.actionBuscar)
        self.menubar.addAction(self.menuOperaciones.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Base de datos"))
        self.label_3.setText(_translate("MainWindow", "Tablas"))
        self.LoadTables.setText(_translate("MainWindow", "Cargar tablas"))
        self.LoadValues.setText(_translate("MainWindow", "Cargar Registros"))
        self.ListAll.setText(_translate("MainWindow", "Mostrar todo"))
        self.menuOperaciones.setTitle(_translate("MainWindow", "Operaciones"))
        self.actionNuevo_Registro.setText(_translate("MainWindow", "Nuevo Registro"))
        self.actionEditar_Registro.setText(_translate("MainWindow", "Editar Registro"))
        self.actionBuscar.setText(_translate("MainWindow", "Buscar"))
        self.actionBuscar.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.actionNueva_Tabla.setText(_translate("MainWindow", "Nueva Tabla"))

