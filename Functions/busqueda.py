from PyQt5.QtWidgets import  QDialog
import pandas as pd
import Functions.dbconnection as db
from interfaces.dialogo_busqueda import Ui_Dialog as Busqueda
from Functions.table_model import TableModel

class buscar(QDialog, Busqueda):
    def __init__(self, parent = None, table = None, columns = None):
        super().__init__()

        QDialog.__init__(self, parent)
        self.parent = parent
        self.setupUi(self)
        self.table = table
        self.columns = columns
        self.campos.addItems(self.columns)
        self.pushButton.clicked.connect(lambda: self.find())
        self.pushButton_2.clicked.connect(self.close)


    def find(self,  data = None):
        value = self.lineEdit.text()
        column = self.campos.currentText()
        table = self.table
        if  self.checkBox.isChecked():
            databases = ['Moreliadb', 'Patzcuarodb']
            results = db.list_find(value, column, table, databases)
        else:
            results = db.list_find(value, column, table)

        print(results)

        results = pd.DataFrame(results, columns=self.columns)
        self.model = TableModel(results)
        self.parent.tableView.setModel(self.model)
