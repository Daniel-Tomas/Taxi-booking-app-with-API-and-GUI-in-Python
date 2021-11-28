# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'msg_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_msg_dialog(object):
    def setupUi(self, msg_dialog):
        msg_dialog.setObjectName("msg_dialog")
        msg_dialog.resize(354, 264)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/app-logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg_dialog.setWindowIcon(icon)
        self.background_img_label = QtWidgets.QLabel(msg_dialog)
        self.background_img_label.setGeometry(QtCore.QRect(-190, -20, 600, 500))
        self.background_img_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.background_img_label.setText("")
        self.background_img_label.setPixmap(QtGui.QPixmap("../images/background users.jpg"))
        self.background_img_label.setObjectName("background_img_label")
        self.msg_label = QtWidgets.QLabel(msg_dialog)
        self.msg_label.setGeometry(QtCore.QRect(10, 110, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.msg_label.setFont(font)
        self.msg_label.setText("")
        self.msg_label.setAlignment(QtCore.Qt.AlignCenter)
        self.msg_label.setObjectName("msg_label")

        self.retranslateUi(msg_dialog)
        QtCore.QMetaObject.connectSlotsByName(msg_dialog)

    def retranslateUi(self, msg_dialog):
        _translate = QtCore.QCoreApplication.translate
        msg_dialog.setWindowTitle(_translate("msg_dialog", "Warning"))

