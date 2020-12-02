import Functions.dbconnection as db
import sys
from PyQt5.QtWidgets import QDialog, QMainWindow, QMessageBox
from interfaces.login_ui import Ui_MainWindow as login_ui

class login(QMainWindow, login_ui):
    def __init__(self, parent = None):
        super().__init__(parent)
        # QDialog.__init__(self, parent)
        self.parent = parent
        self.setupUi(self)

        self.setWindowTitle("MySQL login")
        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(sys.exit)

    def login(self):
        user = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if db.verify_credentials(user, password):
            db.config['user'] = user
            db.config['password'] = password
            
            self.parent.show_main()
            self.close()
        else:
            QMessageBox.critical(self, "Login error", "Incorrect username or password")
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            