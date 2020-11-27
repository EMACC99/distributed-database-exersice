from Functions.table_model import TableModel
from PyQt5.QtWidgets import QDial, QDialog
import pandas as pd
import Functions.dbconection as db
from interfaces.insertar_tabla import Ui_Dialog as talbe_dialog

class NewTable(QDialog, talbe_dialog):
    def __init__(self, parent = None):
        super().__init__()
        
        QDialog.__init__(self, parent)

        self.parent = parent
        self.setupUi(self)

        self.keyComboBox.addItems(['Primaria' , 'Foranea', ''])
        self.ReferenceTable.addItems(db.get_tables(self.parent.DatabaseComboBox.currentText()))
        self.dataType.addItems(['int', 'varchar'])
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.insert_table)
        self.pushButton_3.clicked.connect(self.close)

        self.col_names = []
        self.data_types = []
        self.keys = []
        self.checked = False

        self.keyCheckBox.toggled.connect(self.enable_combo)

    
    def enable_combo(self):
        if self.keyCheckBox.isChecked():
            self.keyComboBox.setEnabled(True)
            self.ReferenceTable.setEnabled(True)
            self.checked = True
        else:
            self.keyComboBox.setEnabled(False)
            self.ReferenceTable.setEnabled(False)
            self.checked = False
        
    
    def insert_table(self):
        db.new_table("nombre", self.col_names, self.data_types, "Moreliadb") 

    def add(self):

        col_name = self.Columna.text()
        data_type = self.dataType.currentText()
        data_size = str(self.sizeSpinBox.value())

        if self.checked:
            key_type = self.keyComboBox.currentText()
            if key_type is 'Primaria':
                self.keyComboBox.removeItem(self.keyComboBox.currentIndex())
            referenced_table = self.ReferenceTable.currentText()
            self.keys.append(tuple(key_type, referenced_table))

        
        self.col_names.append(col_name)
        self.data_types.append((data_type, data_size))
        
        self.textBrowser.textCursor().insertText(f"{col_name} : {data_type}({data_size}) \n")
