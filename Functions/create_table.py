from PyQt5.QtWidgets import QDial, QDialog, QMessageBox
import Functions.dbconnection as db
from interfaces.insertar_tabla import Ui_Dialog as talbe_dialog

class NewTable(QDialog, talbe_dialog):
    def __init__(self, parent = None):
        super().__init__()
        
        QDialog.__init__(self, parent)

        self.parent = parent
        self.setupUi(self)

        self.setWindowTitle("Insertar Tabla")

        self.keyComboBox.addItems(['Primaria' , 'Foranea', ''])
        self.ReferenceTable.addItems(db.get_tables(self.parent.DatabaseComboBox.currentText()))
        self.ReferenceColumn.addItems(db.get_table_pk(self.ReferenceTable.currentText(), self.parent.DatabaseComboBox.currentText() ))

        self.dataType.addItems(['int', 'varchar'])
        self.sizeSpinBox.setValue(1)
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.insert_table)
        self.pushButton_3.clicked.connect(self.close)

        self.col_names = []
        self.data_types = []
        self.keys = []
        self.checked = False

        self.keyCheckBox.toggled.connect(self.enable_combo)
        self.keyComboBox.currentIndexChanged.connect(self.enable_referece_table)
        
        self.ReferenceTable.currentIndexChanged.connect(self.update_reference_columns)

    def enable_combo(self):
        if self.keyCheckBox.isChecked():
            self.keyComboBox.setEnabled(True)
            self.checked = True
        else:
            self.keyComboBox.setEnabled(False)
            self.ReferenceTable.setEnabled(False)
            self.ReferenceColumn.setEnabled(False)
            self.checked = False
        
    def enable_referece_table(self):
        if self.keyComboBox.currentText() == 'Primaria':
            self.ReferenceTable.setEnabled(False)
            self.ReferenceColumn.setEnabled(False)
        else:
            self.ReferenceTable.setEnabled(True)
            self.ReferenceColumn.setEnabled(True)
    
    def update_reference_columns(self):
        self.ReferenceColumn.clear()
        self.ReferenceColumn.addItems(db.get_column_names(self.ReferenceTable.currentText()))

    def insert_table(self):
        db.new_table(self.tableName.text(), self.col_names, self.data_types, "Moreliadb", self.keys) 
        db.new_table(self.tableName.text(), self.col_names, self.data_types, "Patzcuarodb", self.keys)
        self.close()

    def add(self):
        col_name = self.Columna.text()
        if col_name in self.col_names:
            QMessageBox.critical(self, "Error", "El nombre de la columna ya esta puesto, usa otro nombre")
            self.Columna.setText('')
            return

        data_type = self.dataType.currentText()
        data_size = self.sizeSpinBox.value()
        key_type = None
        if self.keyCheckBox.isChecked():
            key_type = self.keyComboBox.currentText()
            if self.keyComboBox.currentText() == 'Primaria':
                self.keyComboBox.removeItem(self.keyComboBox.currentIndex())
                referenced_table = None
                referenced_column = None
            elif self.keyComboBox.currentText() != 'Primaria' and self.ReferenceTable.isEnabled():
                referenced_table = self.ReferenceTable.currentText()
                referenced_column = self.ReferenceColumn.currentText()
            else:
                referenced_table = None
                referenced_column = None

            index = len(self.col_names)
            
            self.keys.append([key_type, referenced_table, referenced_column, index])
        
        self.col_names.append(col_name)
        self.data_types.append((data_type, data_size))
        print(self.col_names)
        print(self.data_types)
        print(self.keys)
        self.textBrowser.textCursor().insertText(f"{col_name} : {data_type}({data_size}) key_type = {key_type}\n")
        self.Columna.setText('')
        self.keyCheckBox.setCheckState(False)