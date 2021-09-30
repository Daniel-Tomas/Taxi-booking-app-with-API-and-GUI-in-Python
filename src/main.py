from PyQt5 import QtWidgets

from login_ui import Ui_login_dialog
from signup_ui import Ui_signup_dialog
from src import admin_ui
from src import login_ui


# import src.admin_ui


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.current_window = None
        self.to_login()

    def change_window(self, new_window):
        if self.current_window is not None:
            self.current_window.hide()

        new_window.show()
        self.current_window = new_window

    def to_login(self):
        login_window = QtWidgets.QMainWindow()
        self.login_ui = Ui_login_dialog()
        self.login_ui.setupUi(login_window)

        self.login_ui.login_button.clicked.connect(self.make_login)
        self.login_ui.sign_up_button.clicked.connect(self.to_signup)

        self.change_window(login_window)

    def make_login(self):
        self.to_admin()

    def to_signup(self):
        signup_window = QtWidgets.QMainWindow()
        self.signup_ui = Ui_signup_dialog()
        self.signup_ui.setupUi(signup_window)

        self.signup_ui.signup_button.clicked.connect(self.make_signup)

        self.change_window(signup_window)

    def make_signup(self):
        pass

    def to_admin(self):
        admin_window = QtWidgets.QMainWindow()
        ad_ui = admin_ui.Ui_Dialog()
        ad_ui.setupUi(admin_window)

        self.change_window(admin_window)

        # self.ui2 = Ui_Dialog()
        # self.ui2.setupUi(self)

    def to_users(self):
        pass


def main():
    app = QtWidgets.QApplication([])
    window = MainWindow()
    # window.show()
    # window.showMaximized()
    app.exec_()


if __name__ == "__main__":
    main()
