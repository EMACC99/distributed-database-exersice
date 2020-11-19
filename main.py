import sys
from PyQt5.QtCore import QModelIndex, Qt, QAbstractTableModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog
from interfaz import Ui_MainWindow as window
import pandas as pd
import dbconection as db
from dialogo_busqueda import buscar
class TableModel(QAbstractTableModel):
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


class UI(QMainWindow, window):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Mi primer base de datos distribuida MiAlegria")

        self.DatabaseComboBox.addItems(db.get_databases())

        self.LoadTables.clicked.connect(lambda : self.load_tables(self.DatabaseComboBox.currentText()))
        self.LoadValues.clicked.connect(lambda : self.select_all( db.get_column_names(self.TablecomboBox.currentText())))
        self.ListAll.clicked.connect(lambda : self.select_all(db.get_column_names(self.TablecomboBox.currentText()), all = True))
        self.actionBuscar.triggered.connect()

    def load_tables(self, database):
        tables = db.get_tables(database)
        self.TablecomboBox.clear()
        self.TablecomboBox.addItems(tables)
        # columns = db.get_column_names(self.TablecomboBox.currentText())
        # self.select_all(columns)

    def select_all(self, columns, all = False):
        if all:
            items = db.list_all(databases=["Moreliadb", "Patzcuarodb"], table=self.TablecomboBox.currentText())
        else:
            items = db.todos(self.TablecomboBox.currentText())
        # columns = db.get_column_names(self.TablecomboBox.currentText())
        data = pd.DataFrame(items, columns=columns)

        self.model = TableModel(data)
        self.tableView.setModel(self.model)

    def count(self, table):
        lista = db.count_items(table)
        self.model = TableModel(lista)
        self.tableView.setModel(self.model)


if __name__ == '__main__':
    APP = QApplication(sys.argv)

    GUI = UI()
    GUI.show()

    sys.exit(APP.exec_())