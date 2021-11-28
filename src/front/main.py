import asyncio

import requests
import yaml
from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal

from admin_download_dialog_ui import Ui_admin_download_dialog
from admin_msg_dialog_ui import Ui_admin_msg_dialog
from admin_ui import Ui_admin_dialog
from login_ui import Ui_login_dialog
from msg_dialog_ui import Ui_msg_dialog
from signup_ui import Ui_signup_dialog
from users_ui import Ui_users_dialog


# import src.admin_ui
class MyThread(QThread):
    def run(self):
        self.exec_()


class DownloadWorker(QObject):
    download_progress_sgn = pyqtSignal(int)

    def run(self):
        self._isRunning = True
        self.completed = 0

        while self.completed <= 100 and self._isRunning:
            self.completed += 0.0001
            self.download_progress_sgn.emit(int(self.completed))
            QtWidgets.QApplication.processEvents()

    def stop(self):
        self._isRunning = False
        # self.download_progress_sgn.emit(0)


class ServerWorker(QObject):
    # finished = pyqtSignal()
    taxi_name_sgn = pyqtSignal(str, object)

    def run(self):
        #  SYNCHRONOUS VERSION (TO UNDERSTAND IT EASILY)
        #
        #        HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
        #        PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
        #
        #        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        #            s.bind((HOST, PORT))
        #            s.listen()
        #            conn, addr = s.accept()
        #            with conn:
        #                print('Connected by', addr)
        #                data = conn.recv(1024)
        #                print(data)
        #                conn.sendall(b'taxi request response')
        async def handle_echo(reader, writer):
            data = await reader.read(100)
            taxi_name = data.decode()
            addr = writer.get_extra_info('peername')

            print(f"Received {taxi_name!r} from {addr!r}")

            # self.writer_conn = writer

            self.taxi_name_sgn.emit(taxi_name, writer)

            # print(f"Send: {taxi_name!r}")
            # writer.write(data)
            # await writer.drain()
            #
            # print("Close the connection")
            # writer.close()

        async def main():
            server = await asyncio.start_server(
                handle_echo, '127.0.0.1', 8080)

            addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
            print(f'Serving on {addrs}')

            async with server:
                await server.serve_forever()

        asyncio.run(main())
        # self.finished.emit()

    # async def send_admin_response(self, accepted):
    #
    #     print(f"Send: {accepted!r}")
    #     self.writer_conn.write(f'{accepted}'.encode())
    #     await self.writer_conn.drain()
    #
    #     print("Close the connection")
    #     self.writer_conn.close()


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

        self.login_ui.passwd_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

        self.login_ui.login_button.clicked.connect(self.login_logic)
        self.login_ui.sign_up_button.clicked.connect(self.to_signup)

        self.change_window(self.login_window)

    def login_logic(self):
        username = self.login_ui.username_lineEdit.text()
        passwd = self.login_ui.passwd_lineEdit.text()

        login_resp = requests.post(f'{self.base_url}/users/{username}/login', json={'password': passwd})
        if login_resp.status_code == 200:
            if username == 'admin':
                self.to_admin()
            else:
                self.username_logged_in = username
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

        self.signup_ui.passwd_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signup_ui.signup_button.clicked.connect(self.signup_logic)

        self.change_window(signup_window)

    def signup_logic(self):
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
        self.admin_ui = Ui_admin_dialog()
        self.admin_ui.setupUi(admin_window)

        self.admin_logic()

        self.change_window(admin_window)

        self.start_admin_server_thread()

    def admin_logic(self):
        self.update_taxies_list()

        self.admin_ui.download_button.clicked.connect(self.download_history)
        self.admin_ui.taxi_listWidget.setAlternatingRowColors(True)
        self.admin_ui.taxi_listWidget.itemClicked.connect(self.show_taxi_info)

    def update_taxies_list(self):
        self.admin_ui.taxi_listWidget.clear()
        get_resp = requests.get(f'{self.base_url}/taxies/')
        self.taxies = get_resp.json()

        for taxi in self.taxies:
            taxi_item = QtWidgets.QListWidgetItem(taxi['name'], self.admin_ui.taxi_listWidget)
            taxi_state = 'Libre' if taxi['is_free'] is True else 'Ocupado'
            taxi_item.setToolTip(taxi_state)

    def download_history(self):
        self.admin_download_dialog = QtWidgets.QDialog()
        self.admin_download_dialog_ui = Ui_admin_download_dialog()
        self.admin_download_dialog_ui.setupUi(self.admin_download_dialog)

        self.admin_download_dialog_ui.progressBar.setValue(0)
        self.admin_download_dialog_ui.cancel_button.clicked.connect(self.cancel_download)
        self.admin_download_dialog_ui.start_button.clicked.connect(self.start_download)

        self.admin_download_dialog.show()

    def start_download(self):
        self.thread_download = MyThread()
        self.worker_download = DownloadWorker()

        self.worker_download.moveToThread(self.thread_download)

        self.thread_download.started.connect(self.worker_download.run)
        # self.worker.finished.connect(self.thread.quit)
        # self.worker.finished.connect(self.worker.deleteLater)
        # self.thread.finished.connect(self.thread.deleteLater)
        self.worker_download.download_progress_sgn.connect(self.update_progress_bar)
        # self.admin_response_sgn.connect(self.worker.send_admin_response)

        self.thread_download.start()
        # self.thread_download.terminate()
        # self.thread_download.quit()

    def update_progress_bar(self, progress):
        self.admin_download_dialog_ui.progressBar.setValue(progress)
        if progress == 100:
            self.download_completed()

    def download_completed(self):

        get_resp = requests.get(f'{self.base_url}/requests/')
        requests_dict = get_resp.json()

        with open('history.txt', 'w') as f:
            s = 'Taxies history'
            fixed_len = 50
            f.write(f'{s.center(len(s) + 2).center(fixed_len, "=")}\n\n')
            f.write(yaml.dump(requests_dict, sort_keys=False, default_flow_style=False))

        self.show_msg_dialog('Download completed')
        self.admin_download_dialog.hide()

    def cancel_download(self):

        self.worker_download.stop()
        self.thread_download.quit()

        self.show_msg_dialog('Download canceled')

        # self.admin_download_dialog_ui.progressBar.setValue(0)

    def start_admin_server_thread(self):
        self.thread = QThread()
        self.worker = ServerWorker()

        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        # self.worker.finished.connect(self.thread.quit)
        # self.worker.finished.connect(self.worker.deleteLater)
        # self.thread.finished.connect(self.thread.deleteLater)
        self.worker.taxi_name_sgn.connect(self.ask_req_admin)
        # self.admin_response_sgn.connect(self.worker.send_admin_response)

        self.thread.start()

        # # Final resets
        # self.longRunningBtn.setEnabled(False)
        # self.thread.finished.connect(
        #     lambda: self.longRunningBtn.setEnabled(True)
        # )
        # self.thread.finished.connect(
        #     lambda: self.stepLabel.setText("Long-Running Step: 0")
        # )

    def ask_req_admin(self, taxi_name, writer):
        self.writer = writer

        self.show_admin_dialog(f'The taxi "{taxi_name}" has been requested')

        # self.admin_response_sgn.emit('True')

    def show_admin_dialog(self, msg):
        self.admin_msg_dialog = QtWidgets.QDialog()
        self.admin_msg_dialog_ui = Ui_admin_msg_dialog()
        self.admin_msg_dialog_ui.setupUi(self.admin_msg_dialog)

        self.admin_msg_dialog_ui.accept_button.clicked.connect(self.process_accept_resp_admin)
        self.admin_msg_dialog_ui.decline_button.clicked.connect(self.process_decline_resp_admin)

        self.admin_msg_dialog_ui.msg_label.setText(msg)

        self.admin_msg_dialog.show()

    def process_accept_resp_admin(self):
        self.process_resp_admin(True)
        self.update_taxies_list()

    def process_decline_resp_admin(self):
        self.process_resp_admin(False)

    def process_resp_admin(self, resp):

        accepted = resp
        print(f"Send: {accepted!r}")
        self.writer.write(f'{accepted}'.encode())
        # writer.drain()

        print("Close the connection")
        self.writer.close()

        self.admin_msg_dialog.hide()
        self.show_msg_dialog('The response has been processed successfully')

    def show_taxi_info(self):
        taxi_name = self.admin_ui.taxi_listWidget.currentItem().text()
        for taxi in self.taxies:
            if taxi['name'] == taxi_name:
                taxi_state = 'Libre' if taxi['is_free'] is True else 'Ocupado'
                self.admin_ui.label_status_response.setText(taxi_state)
                self.admin_ui.label_location_response.setText(taxi['actual'])
                self.admin_ui.label_destination_response.setText(taxi['destination'])
                break

    def to_users(self):
        users_window = QtWidgets.QMainWindow()
        self.users_ui = Ui_users_dialog()
        self.users_ui.setupUi(users_window)

        self.users_ui.request_button.clicked.connect(self.users_logic)

        self.change_window(users_window)

    def users_logic(self):

        def empty_users_fields(self):
            self.users_ui.origin_lineEdit.setText('')
            self.users_ui.destination_lineEdit.setText('')
            self.users_ui.date_lineEdit.setText('')
            self.users_ui.time_lineEdit.setText('')

        origin = self.users_ui.origin_lineEdit.text()
        destination = self.users_ui.destination_lineEdit.text()
        date = self.users_ui.date_lineEdit.text()
        time = self.users_ui.time_lineEdit.text()
        body = {'origin': origin, 'date': date, 'time': time,
                'destination': destination}

        post_resp = requests.post(f'{self.base_url}/users/{self.username_logged_in}/requests', json=body)
        if post_resp.status_code == 201:
            empty_users_fields(self)
            self.show_msg_dialog('Request accepted')
        elif post_resp.status_code == 403:
            self.show_msg_dialog('Request declined')
        elif post_resp.status_code == 503:
            self.show_msg_dialog('There are no free taxies')


def main():
    app = QtWidgets.QApplication([])
    window = MainWindow()
    # window.show()
    # window.showMaximized()
    app.exec_()


if __name__ == "__main__":
    main()
