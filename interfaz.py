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
        MainWindow.resize(788, 655)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(490, 0, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 60, 801, 501))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtWidgets.QTableView(self.verticalLayoutWidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.LoadValues = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.LoadValues.setObjectName("LoadValues")
        self.verticalLayout.addWidget(self.LoadValues)
        self.LoadTables = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.LoadTables.setObjectName("LoadTables")
        self.verticalLayout.addWidget(self.LoadTables)
        self.ListAll = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ListAll.setObjectName("ListAll")
        self.verticalLayout.addWidget(self.ListAll)
        self.TablecomboBox = QtWidgets.QComboBox(self.centralwidget)
        self.TablecomboBox.setGeometry(QtCore.QRect(150, 40, 151, 20))
        self.TablecomboBox.setObjectName("TablecomboBox")
        self.DatabaseComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.DatabaseComboBox.setGeometry(QtCore.QRect(0, 40, 151, 20))
        self.DatabaseComboBox.setObjectName("DatabaseComboBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 788, 21))
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
        self.menuOperaciones.addAction(self.actionNuevo_Registro)
        self.menuOperaciones.addAction(self.actionEditar_Registro)
        self.menuOperaciones.addAction(self.actionBuscar)
        self.menubar.addAction(self.menuOperaciones.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Mi primer base de datos Mi Alegria"))
        self.LoadValues.setText(_translate("MainWindow", "Load Values"))
        self.LoadTables.setText(_translate("MainWindow", "Load Tables"))
        self.ListAll.setText(_translate("MainWindow", "List All"))
        self.menuOperaciones.setTitle(_translate("MainWindow", "Operaciones"))
        self.actionNuevo_Registro.setText(_translate("MainWindow", "Nuevo Registro"))
        self.actionEditar_Registro.setText(_translate("MainWindow", "Editar Registro"))
        self.actionBuscar.setText(_translate("MainWindow", "Buscar"))

