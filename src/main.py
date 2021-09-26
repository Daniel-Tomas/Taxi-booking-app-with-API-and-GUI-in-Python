from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets

from login_ui import Ui_login_dialog
from admin_ui import *

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_login_dialog()
        self.ui.setupUi(self)

        # Button
        self.button_login = QtWidgets.QAction("Admin")
        self.button_login.triggered(self.to_admin)

    def to_admin(self):
        self.admin_window = admin_ui.QtWidgets.QMainWindow()
        admin_ui = admin_ui.Ui_Admin_Window()
        admin_ui.setupUi(self.admin_window)
        self.admin_window.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    # window.showMaximized()
    app.exec_()
