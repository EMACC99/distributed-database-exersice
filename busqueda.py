from PyQt5.QtWidgets import  QDialog
import pandas as pd
import dbconection as db
from dialogo_busqueda import Ui_Dialog as Busqueda


class buscar(QDialog, Busqueda):
    def __init__(self, parent = None):
        super().__init__()

        QDialog.__init__(self, parent)
        self.parent = parent
        self.setupUi(self)
        
        if parent is not None:
            self.load()
        
        self.pushButton.clicked.connect(lambda: self.find())


    def load(self):
        tables = [self.parent.TablecomboBox.itemText(i) for i in range(self.parent.TablecomboBox.count())]
        self.campos.addItems(tables)

    def find(self,  data = None):
        if not self.checkBox.isChecked():
            database = self.parent.DatabaseComboBox.currentText()
        tables = [self.parent.TablecomboBox.itemText(i) for i in range(self.parent.TablecomboBox.count())]
        
        print(tables)
        self.campos.addItems(tables)

    