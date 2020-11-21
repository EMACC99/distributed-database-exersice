from PyQt5.QtWidgets import  QDial, QDialog
import pandas as pd
import Functions.dbconection as db
from interfaces.insertar_editar import Ui_Dialog as insertar_editar

class InsertarEditar(QDialog, insertar_editar):
    def __init__(self, parent = None, insertar = False):
        super().__init__()

        QDialog.__init__(self, parent)

        self.parent = parent
        self.setupUi(self)
        if insertar:
            self.pushButton.setText("Insertar")
        else:
            self.pushButton.setText("Editar")

        self.CancelButton.clicked.connect(self.close)
    
    def editar(self):
        pass

    def insertar(self):
        pass