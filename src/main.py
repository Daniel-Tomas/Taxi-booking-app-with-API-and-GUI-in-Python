from PyQt5 import QtWidgets
import requests

from admin_ui import Ui_admin_dialog
from login_ui import Ui_login_dialog
from signup_ui import Ui_signup_dialog
from msg_dialog_ui import Ui_msg_dialog


# import src.admin_ui


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.base_url = 'http://127.0.0.1:8000'

        self.current_window = None
        self.to_login()

    def change_window(self, new_window):
        if self.current_window is not None:
            self.current_window.hide()

        new_window.show()
        self.current_window = new_window

    def show_msg_dialog(self, msg):
        self.msg_dialog = QtWidgets.QDialog()
        self.msg_dialog_ui = Ui_msg_dialog()
        self.msg_dialog_ui.setupUi(self.msg_dialog)

        self.msg_dialog_ui.msg_label.setText(msg)

        self.msg_dialog.show()

    def to_login(self):
        self.login_window = QtWidgets.QMainWindow()
        self.login_ui = Ui_login_dialog()
        self.login_ui.setupUi(self.login_window)

        self.login_ui.login_button.clicked.connect(self.make_login)
        self.login_ui.sign_up_button.clicked.connect(self.to_signup)

        self.change_window(self.login_window)

    def make_login(self):
        username = self.login_ui.username_lineEdit.text()
        passwd = self.login_ui.passwd_lineEdit.text()

        login_resp = requests.post(f'{self.base_url}/users/{username}/login', json={'password': passwd})
        if login_resp.status_code == 200:
            if username == 'admin':
                self.to_admin()
            else:
                self.to_users()
        else:  # user not exists, password incorrect, or need to confirm via email
            get_resp = requests.get(f'{self.base_url}/users/{username}')
            user_exists = get_resp.status_code == 200
            if user_exists and not (is_active := get_resp.json()['is_active']):
                self.show_msg_dialog('Please confirm signup via email')
            else:
                self.show_msg_dialog('Incorrect username or password')

    def to_signup(self):
        signup_window = QtWidgets.QMainWindow()
        self.signup_ui = Ui_signup_dialog()
        self.signup_ui.setupUi(signup_window)

        self.signup_ui.signup_button.clicked.connect(self.make_signup)

        self.change_window(signup_window)

    def make_signup(self):
        username = self.signup_ui.username_lineEdit.text()
        passwd = self.signup_ui.passwd_lineEdit.text()
        email = self.signup_ui.email_lineEdit.text()
        card = self.signup_ui.card_lineEdit.text()
        phone = self.signup_ui.phone_lineEdit.text()
        body = {'nickname': username, 'email': email, 'pay_method': card,
                'phone_number': phone, 'password': passwd}

        post_resp = requests.post(f'{self.base_url}/users', json=body)
        if post_resp.status_code == 201:
            self.change_window(self.login_window)
            self.show_msg_dialog('Please confirm signup via email')
        else:
            self.show_msg_dialog('Username already exists')

    def to_admin(self):
        admin_window = QtWidgets.QMainWindow()
        ad_ui = Ui_admin_dialog()
        ad_ui.setupUi(admin_window)

        self.change_window(admin_window)

        # self.ui2 = Ui_Dialog()
        # self.ui2.setupUi(self)

    def to_users(self):
        print('in users')


def main():
    app = QtWidgets.QApplication([])
    window = MainWindow()
    # window.show()
    # window.showMaximized()
    app.exec_()


if __name__ == "__main__":
    main()
