# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(750, 617)
        Dialog.setMinimumSize(QtCore.QSize(750, 617))
        Dialog.setMaximumSize(QtCore.QSize(750, 617))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../images/app-logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.background_img_label = QtWidgets.QLabel(Dialog)
        self.background_img_label.setGeometry(QtCore.QRect(-140, -30, 1041, 661))
        self.background_img_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.background_img_label.setText("")
        self.background_img_label.setPixmap(QtGui.QPixmap("../images/background users.jpg"))
        self.background_img_label.setObjectName("background_img_label")
        self.admin_frame = QtWidgets.QFrame(Dialog)
        self.admin_frame.setGeometry(QtCore.QRect(150, 80, 451, 471))
        self.admin_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.admin_frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.admin_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.admin_frame.setObjectName("admin_frame")
        self.list_label = QtWidgets.QLabel(self.admin_frame)
        self.list_label.setGeometry(QtCore.QRect(20, 30, 401, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.list_label.setFont(font)
        self.list_label.setAlignment(QtCore.Qt.AlignCenter)
        self.list_label.setObjectName("list_label")
        self.taxi_listWidget = QtWidgets.QListWidget(self.admin_frame)
        self.taxi_listWidget.setGeometry(QtCore.QRect(40, 120, 371, 301))
        self.taxi_listWidget.setObjectName("taxi_listWidget")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Admin Access"))
        self.list_label.setText(_translate("Dialog", "Taxi list"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

