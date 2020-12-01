from PyQt5.QtWidgets import  QDialog
import pandas as pd
import Functions.dbconnection as db
#from interfaces.dialogo_busqueda import Ui_Dialog as Busqueda
from interfaces.dialogo_busqueda_edit import Ui_Dialog as Busqueda

from Functions.table_model import TableModel

class Edit(QDialog, Busqueda):
    def __init__(self, parent = None, table = None, columns = None):
        super().__init__()

        QDialog.__init__(self, parent)
        self.parent = parent
        self.setupUi(self)
        self.table = table
        self.columns = columns
        self.campos.addItems(self.columns)
        self.results2 = None
        self.pushButton.clicked.connect(lambda: self.find())
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton_3.clicked.connect(lambda: self.edit())


    def find(self,  data = None):
        value = self.lineEdit.text()
        column = self.campos.currentText()
        table = self.table
        if  self.checkBox.isChecked():
            databases = ['Moreliadb', 'Patzcuarodb']
            self.results = db.list_find(value, column, table, databases)
        else:
            self.results = db.list_find(value, column, table)

        print(self.results)
        self.results2 = self.results
        self.close
        self.results = pd.DataFrame(self.results, columns=self.columns)
        self.model = TableModel(self.results)
        self.parent.tableView.setModel(self.model)
        
    def edit(self,data=None):
        #print(self.results2)
        value = self.lineEdit.text()
        column = self.campos.currentText()
        table = self.table
        idr = self.results2[0][0]
        #print(column)
        db.edit_registro(value, column, table,idr)
        self.new_resultado = db.list_find(value, column, table)
        self.new_resultado = pd.DataFrame(self.new_resultado, columns=self.columns)
        self.model = TableModel(self.new_resultado)
        self.parent.tableView.setModel(self.model)
        
        
        
        
        
        
        
        
        
        
