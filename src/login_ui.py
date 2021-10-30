# -*- coding: utf-8 -*-

# Form implementation generated from reading login_ui file 'login.login_ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_login_dialog(object):
    def setupUi(self, login_dialog):
        login_dialog.setObjectName("login_dialog")
        login_dialog.resize(729, 629)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(login_dialog.sizePolicy().hasHeightForWidth())
        login_dialog.setSizePolicy(sizePolicy)
        login_dialog.setMinimumSize(QtCore.QSize(729, 629))
        login_dialog.setMaximumSize(QtCore.QSize(729, 629))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/app-logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        login_dialog.setWindowIcon(icon)
        self.login_frame = QtWidgets.QFrame(login_dialog)
        self.login_frame.setGeometry(QtCore.QRect(200, 150, 331, 281))
        self.login_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.login_frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.login_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.login_frame.setObjectName("login_frame")
        self.username_lineEdit = QtWidgets.QLineEdit(self.login_frame)
        self.username_lineEdit.setGeometry(QtCore.QRect(160, 120, 141, 20))
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.passwd_lineEdit = QtWidgets.QLineEdit(self.login_frame)
        self.passwd_lineEdit.setGeometry(QtCore.QRect(160, 160, 141, 20))
        self.passwd_lineEdit.setObjectName("passwd_lineEdit")
        self.username_label = QtWidgets.QLabel(self.login_frame)
        self.username_label.setGeometry(QtCore.QRect(60, 120, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.username_label.setFont(font)
        self.username_label.setObjectName("username_label")
        self.passwd_label = QtWidgets.QLabel(self.login_frame)
        self.passwd_label.setGeometry(QtCore.QRect(60, 160, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.passwd_label.setFont(font)
        self.passwd_label.setObjectName("passwd_label")
        self.login_button = QtWidgets.QPushButton(self.login_frame)
        self.login_button.setGeometry(QtCore.QRect(70, 210, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.login_button.setFont(font)
        self.login_button.setObjectName("login_button")
        self.sign_up_button = QtWidgets.QPushButton(self.login_frame)
        self.sign_up_button.setGeometry(QtCore.QRect(180, 210, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sign_up_button.setFont(font)
        self.sign_up_button.setObjectName("sign_up_button")
        self.app_title_label = QtWidgets.QLabel(self.login_frame)
        self.app_title_label.setGeometry(QtCore.QRect(20, 50, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.app_title_label.setFont(font)
        self.app_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.app_title_label.setObjectName("app_title_label")
        self.background_img_label = QtWidgets.QLabel(login_dialog)
        self.background_img_label.setGeometry(QtCore.QRect(0, 0, 731, 631))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.background_img_label.sizePolicy().hasHeightForWidth())
        self.background_img_label.setSizePolicy(sizePolicy)
        self.background_img_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.background_img_label.setText("")
        self.background_img_label.setPixmap(QtGui.QPixmap("../images/background.jpg"))
        self.background_img_label.setObjectName("background_img_label")
        self.background_img_label.raise_()
        self.login_frame.raise_()

        self.retranslateUi(login_dialog)
        QtCore.QMetaObject.connectSlotsByName(login_dialog)

    def retranslateUi(self, login_dialog):
        _translate = QtCore.QCoreApplication.translate
        login_dialog.setWindowTitle(_translate("login_dialog", "Login"))
        self.username_lineEdit.setPlaceholderText(_translate("login_dialog", "Please enter your username"))
        self.passwd_lineEdit.setPlaceholderText(_translate("login_dialog", "Please enter your password"))
        self.username_label.setText(_translate("login_dialog", "Username"))
        self.passwd_label.setText(_translate("login_dialog", "Password"))
        self.login_button.setText(_translate("login_dialog", "Login"))
        self.sign_up_button.setText(_translate("login_dialog", "Sign up"))
        self.app_title_label.setText(_translate("login_dialog", "Welcome to Taxi App"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login_dialog = QtWidgets.QDialog()
    ui = Ui_login_dialog()
    ui.setupUi(login_dialog)
    login_dialog.show()
    sys.exit(app.exec_())

