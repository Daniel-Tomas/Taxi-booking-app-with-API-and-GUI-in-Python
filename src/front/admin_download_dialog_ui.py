# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_download_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_admin_download_dialog(object):
    def setupUi(self, admin_download_dialog):
        admin_download_dialog.setObjectName("admin_download_dialog")
        admin_download_dialog.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/app-logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        admin_download_dialog.setWindowIcon(icon)
        self.background_img_label = QtWidgets.QLabel(admin_download_dialog)
        self.background_img_label.setGeometry(QtCore.QRect(-190, -20, 600, 500))
        self.background_img_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.background_img_label.setText("")
        self.background_img_label.setPixmap(QtGui.QPixmap("../images/background users.jpg"))
        self.background_img_label.setObjectName("background_img_label")
        self.cancel_button = QtWidgets.QPushButton(admin_download_dialog)
        self.cancel_button.setGeometry(QtCore.QRect(220, 220, 75, 23))
        self.cancel_button.setObjectName("cancel_button")
        self.progressBar = QtWidgets.QProgressBar(admin_download_dialog)
        self.progressBar.setGeometry(QtCore.QRect(50, 130, 281, 31))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.start_button = QtWidgets.QPushButton(admin_download_dialog)
        self.start_button.setGeometry(QtCore.QRect(80, 220, 75, 23))
        self.start_button.setObjectName("start_button")

        self.retranslateUi(admin_download_dialog)
        QtCore.QMetaObject.connectSlotsByName(admin_download_dialog)

    def retranslateUi(self, admin_download_dialog):
        _translate = QtCore.QCoreApplication.translate
        admin_download_dialog.setWindowTitle(_translate("admin_download_dialog", "Download"))
        self.cancel_button.setText(_translate("admin_download_dialog", "Cancel"))
        self.start_button.setText(_translate("admin_download_dialog", "Start"))

