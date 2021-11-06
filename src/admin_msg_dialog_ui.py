# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_msg_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_admin_msg_dialog(object):
    def setupUi(self, admin_msg_dialog):
        admin_msg_dialog.setObjectName("admin_msg_dialog")
        admin_msg_dialog.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/app-logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        admin_msg_dialog.setWindowIcon(icon)
        self.background_img_label = QtWidgets.QLabel(admin_msg_dialog)
        self.background_img_label.setGeometry(QtCore.QRect(-190, -20, 600, 500))
        self.background_img_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.background_img_label.setText("")
        self.background_img_label.setPixmap(QtGui.QPixmap("../images/background users.jpg"))
        self.background_img_label.setObjectName("background_img_label")
        self.msg_label = QtWidgets.QLabel(admin_msg_dialog)
        self.msg_label.setGeometry(QtCore.QRect(10, 100, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.msg_label.setFont(font)
        self.msg_label.setText("")
        self.msg_label.setAlignment(QtCore.Qt.AlignCenter)
        self.msg_label.setObjectName("msg_label")
        self.accept_button = QtWidgets.QPushButton(admin_msg_dialog)
        self.accept_button.setGeometry(QtCore.QRect(60, 210, 75, 23))
        self.accept_button.setObjectName("accept_button")
        self.decline_button = QtWidgets.QPushButton(admin_msg_dialog)
        self.decline_button.setGeometry(QtCore.QRect(250, 210, 75, 23))
        self.decline_button.setObjectName("decline_button")

        self.retranslateUi(admin_msg_dialog)
        QtCore.QMetaObject.connectSlotsByName(admin_msg_dialog)

    def retranslateUi(self, admin_msg_dialog):
        _translate = QtCore.QCoreApplication.translate
        admin_msg_dialog.setWindowTitle(_translate("admin_msg_dialog", "Warning"))
        self.accept_button.setText(_translate("admin_msg_dialog", "Accept"))
        self.decline_button.setText(_translate("admin_msg_dialog", "Decline"))

