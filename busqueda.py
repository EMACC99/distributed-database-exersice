from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5.QtWidgets import  QDialog
import pandas as pd
import dbconection as db
from dialogo_busqueda import Ui_Dialog as Busqueda

class TableSearchModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]
    
    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])


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
            database = self.parent.DatabaseComboBox.currentText()
            results = db.list_find(value, column, table, database)
        else:
            results = db.list_find(value, column, table)

        print(results)

        results = pd.DataFrame(results, columns=self.columns)
        self.model = TableSearchModel(results)
        self.parent.tableView.setModel(self.model)
