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
        MainWindow.resize(799, 629)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setEnabled(True)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 80, 801, 501))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtWidgets.QTableView(self.verticalLayoutWidget)
        self.tableView.setEnabled(True)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.TablecomboBox = QtWidgets.QComboBox(self.centralwidget)
        self.TablecomboBox.setGeometry(QtCore.QRect(160, 20, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Light")
        self.TablecomboBox.setFont(font)
        self.TablecomboBox.setStyleSheet("border-style: outset;\n"
"border-width: 2px;\n"
"border-radius:10px;\n"
"border-color:white;\n"
"\n"
"background-color:#0078CC;\n"
"color:white;\n"
"")
        self.TablecomboBox.setObjectName("TablecomboBox")
        self.DatabaseComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.DatabaseComboBox.setGeometry(QtCore.QRect(0, 20, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Light")
        self.DatabaseComboBox.setFont(font)
        self.DatabaseComboBox.setStyleSheet("border-style: outset;\n"
"border-width: 2px;\n"
"border-radius:10px;\n"
"border-color:white;\n"
"background-color:#0078CC;\n"
"color:white;\n"
"")
        self.DatabaseComboBox.setObjectName("DatabaseComboBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 0, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Light")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white;\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 0, 47, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Light")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:white;\n"
"")
        self.label_3.setObjectName("label_3")
        self.LoadTables = QtWidgets.QPushButton(self.centralwidget)
        self.LoadTables.setGeometry(QtCore.QRect(320, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Light")
        font.setPointSize(10)
        self.LoadTables.setFont(font)
        self.LoadTables.setStyleSheet("background-color:#0078CC;\n"
"color:white;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius:10px;\n"
"border-color:white;")
        self.LoadTables.setObjectName("LoadTables")
        self.LoadValues = QtWidgets.QPushButton(self.centralwidget)
        self.LoadValues.setGeometry(QtCore.QRect(550, 50, 131, 23))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Light")
        font.setPointSize(10)
        self.LoadValues.setFont(font)
        self.LoadValues.setStyleSheet("background-color:#0078CC;\n"
"color:white;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius:10px;\n"
"border-color:white;")
        self.LoadValues.setObjectName("LoadValues")
        self.ListAll = QtWidgets.QPushButton(self.centralwidget)
        self.ListAll.setGeometry(QtCore.QRect(700, 50, 91, 23))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Light")
        font.setPointSize(10)
        self.ListAll.setFont(font)
        self.ListAll.setStyleSheet("background-color:#0078CC;\n"
"color:white;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius:10px;\n"
"border-color:white;")
        self.ListAll.setObjectName("ListAll")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1021, 45))
        self.label.setStyleSheet("background-color:#376D93;\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 45, 1031, 41))
        self.label_4.setStyleSheet("background-color:#2E5B7C;\n"
"")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_4.raise_()
        self.label.raise_()
        self.verticalLayoutWidget.raise_()
        self.TablecomboBox.raise_()
        self.DatabaseComboBox.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.LoadTables.raise_()
        self.LoadValues.raise_()
        self.ListAll.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 20))
        self.menubar.setObjectName("menubar")
        self.menuOperaciones = QtWidgets.QMenu(self.menubar)
        self.menuOperaciones.setObjectName("menuOperaciones")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNuevo_Registro = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Light")
        self.actionNuevo_Registro.setFont(font)
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

