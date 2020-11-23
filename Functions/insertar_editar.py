from PyQt5.QtWidgets import  QDial, QDialog
import pandas as pd
import Functions.dbconection as db
from interfaces.insertar_editar import Ui_Dialog as insertar_editar

class InsertarEditar(QDialog, insertar_editar):
    def __init__(self, parent = None, insertar = False, table = None, columns = None):
        super().__init__()

        QDialog.__init__(self, parent)
        self.parent = parent
        self.setupUi(self)
        
        self.plainTextEdit.setReadOnly(True)

        self.table = table
        self.columns = columns
        self.registro = []
        self.flag_error = False
        self.comboBox.addItems(columns)

        if insertar:
            self.pushButton.setText("Insertar")
        else:
            self.pushButton.setText("Editar")

        self.CancelButton.clicked.connect(self.close)
        
        self.pushButton.clicked.connect(lambda : self.insertar() if insertar else self.editar())
        self.pushButton_2.clicked.connect(self.update_text)

    def editar(self):
        # db.editar_registro()
        self.plainTextEdit.textCursor().insertText('Editar \n')
        print('editar')


    def insertar(self):
        self.plainTextEdit.textCursor().insertText('Insertar \n')
        if len(self.registro) != 2*len(self.columns):
            self.plainTextEdit.setPlainText("Para insertar necesitas llenar todos los campos!")
            self.comboBox.clear()
            self.comboBox.addItems(self.columns)
            self.flag_error = True
            # self.close()
            return 
        db.nuevo_registro(self.table, self.registro[1::2]) #esto suelta error porque los tipos de datos los agarra como string y no como int o lo que sea para los ids
        print('insertar')
        print(self.registro)
        self.plainTextEdit.setPlainText('')
        self.close()

    def update_text(self):
        if self.flag_error:
            self.plainTextEdit.setPlainText('')
        
        col = self.comboBox.currentText()
        val = self.lineEdit.text()
        col_type =db.get_column_type(self.table, self.parent.DatabaseComboBox.currentText(), col)

        # print(col_type, type(col_type))

        self.registro.append(col)

        if col_type == "int" and val != '':
            val = int(val)
        elif col_type == "int" and val == '':
            val = 0
        elif val == '':
            val = "NULL"

        self.registro.append(val)

        print(self.registro)

        self.comboBox.removeItem(self.comboBox.currentIndex())
        self.lineEdit.setText('')
        self.plainTextEdit.textCursor().insertText(f'{col} : {val} \n')
