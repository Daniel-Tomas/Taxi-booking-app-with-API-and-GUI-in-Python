from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, QtGui

# import src.admin_ui

from src import admin_ui
from src import login_ui
from login_ui import Ui_login_dialog
from admin_ui import Ui_Dialog

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_login_dialog()
        self.ui.setupUi(self)

        # Button
        self.ui.login_button.clicked.connect(self.to_admin)

    def to_admin(self):
        self.admin_window = admin_ui.QtWidgets.QDialog()
        ad_ui = admin_ui.Ui_Dialog()
        ad_ui.setupUi(self.admin_window)
        self.admin_window.show()

        # self.ui2 = Ui_Dialog()
        # self.ui2.setupUi(self)

    def to_users(self):
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    # window.showMaximized()
    app.exec_()
