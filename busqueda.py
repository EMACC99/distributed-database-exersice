import sys
from PyQt5.QtCore import QModelIndex, Qt, QAbstractTableModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog
from interfaz import Ui_MainWindow as window
import pandas as pd
import dbconection as db
from dialogo_busqueda import Ui_Dialog as Busqueda


class buscar(QDialog, Busqueda):
    def __init__(self, parent = None):
        super().__init__()

        # QDialog.__init__(self, parent)
        self.parent = parent
        self.setupUi(self)
        # self.pushButton.clicked.connect(lambda: self.find())

    # def find(self, item, column, data):
    
