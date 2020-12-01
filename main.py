import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from interfaces.interfaz import Ui_MainWindow as window
import pandas as pd
import Functions.dbconnection as db
from Functions.busqueda import buscar
from Functions.table_model import TableModel
from Functions.insertar_editar import InsertarEditar
from Functions.create_table import NewTable
from Functions.login import login
from Functions.Edit import Edit

class UI(QMainWindow, window):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.log_in()

    def log_in(self):
        login(self).show()
        
    def show_main(self):
        self.setupUi(self)
        self.setWindowTitle("DDB9")

        self.DatabaseComboBox.addItems(db.get_databases())
        
        self.load_tables(self.DatabaseComboBox.currentText())
        # print([self.TablecomboBox.itemText(i) for i in range(self.TablecomboBox.count())])

        self.LoadTables.clicked.connect(lambda : self.load_tables(self.DatabaseComboBox.currentText()))
        self.LoadValues.clicked.connect(lambda : self.select_all( db.get_column_names(self.TablecomboBox.currentText())))
        self.ListAll.clicked.connect(lambda : self.select_all(db.get_column_names(self.TablecomboBox.currentText()), all = True))
        self.actionBuscar.triggered.connect(self.call_find)
        self.actionEditar_Registro.triggered.connect(self.edit_find)
        self.actionNuevo_Registro.triggered.connect(lambda: self.call_edit_insert(insertar = True))
        self.actionNueva_Tabla.triggered.connect(self.call_new_table)
    def call_find(self):
        buscar(self, self.TablecomboBox.currentText(), db.get_column_names(self.TablecomboBox.currentText())).show()

    def edit_find(self):
        Edit(self, self.TablecomboBox.currentText(), db.get_column_names(self.TablecomboBox.currentText())).show()
        
        
    def call_edit_insert(self, insertar):
        InsertarEditar(self, insertar = insertar, table = self.TablecomboBox.currentText(), columns = db.get_column_names(self.TablecomboBox.currentText())).show()

    def call_new_table(self):
        NewTable(self).show()

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
