# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sign_up.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_sign_up_dialog(object):
    def setupUi(self, sign_up_dialog):
        sign_up_dialog.setObjectName("sign_up_dialog")
        sign_up_dialog.resize(729, 629)
        font = QtGui.QFont()
        font.setPointSize(19)
        sign_up_dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/app-logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        sign_up_dialog.setWindowIcon(icon)
        self.login_frame = QtWidgets.QFrame(sign_up_dialog)
        self.login_frame.setGeometry(QtCore.QRect(200, 170, 331, 241))
        self.login_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.login_frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.login_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.login_frame.setObjectName("login_frame")
        self.username_lineEdit = QtWidgets.QLineEdit(self.login_frame)
        self.username_lineEdit.setGeometry(QtCore.QRect(160, 60, 141, 20))
        self.username_lineEdit.setObjectName("username_lineEdit")
        self.passwd_lineEdit = QtWidgets.QLineEdit(self.login_frame)
        self.passwd_lineEdit.setGeometry(QtCore.QRect(160, 100, 141, 20))
        self.passwd_lineEdit.setObjectName("passwd_lineEdit")
        self.username_label = QtWidgets.QLabel(self.login_frame)
        self.username_label.setGeometry(QtCore.QRect(60, 60, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.username_label.setFont(font)
        self.username_label.setObjectName("username_label")
        self.passwd_label = QtWidgets.QLabel(self.login_frame)
        self.passwd_label.setGeometry(QtCore.QRect(60, 100, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.passwd_label.setFont(font)
        self.passwd_label.setObjectName("passwd_label")
        self.login_button = QtWidgets.QPushButton(self.login_frame)
        self.login_button.setGeometry(QtCore.QRect(70, 150, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.login_button.setFont(font)
        self.login_button.setObjectName("login_button")
        self.sign_up_button = QtWidgets.QPushButton(self.login_frame)
        self.sign_up_button.setGeometry(QtCore.QRect(180, 150, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sign_up_button.setFont(font)
        self.sign_up_button.setObjectName("sign_up_button")
        self.label = QtWidgets.QLabel(sign_up_dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 731, 631))
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../images/background.jpg"))
        self.label.setObjectName("label")
        self.label.raise_()
        self.login_frame.raise_()

        self.retranslateUi(sign_up_dialog)
        QtCore.QMetaObject.connectSlotsByName(sign_up_dialog)

    def retranslateUi(self, sign_up_dialog):
        _translate = QtCore.QCoreApplication.translate
        sign_up_dialog.setWindowTitle(_translate("sign_up_dialog", "Sign up"))
        self.username_lineEdit.setPlaceholderText(_translate("sign_up_dialog", "Please enter your username"))
        self.passwd_lineEdit.setPlaceholderText(_translate("sign_up_dialog", "Please enter your password"))
        self.username_label.setText(_translate("sign_up_dialog", "Username"))
        self.passwd_label.setText(_translate("sign_up_dialog", "Password"))
        self.login_button.setText(_translate("sign_up_dialog", "Login"))
        self.sign_up_button.setText(_translate("sign_up_dialog", "Sign up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sign_up_dialog = QtWidgets.QDialog()
    ui = Ui_sign_up_dialog()
    ui.setupUi(sign_up_dialog)
    sign_up_dialog.show()
    sys.exit(app.exec_())

