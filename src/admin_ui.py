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
        self.admin_frame.setGeometry(QtCore.QRect(150, 80, 450, 471))
        self.admin_frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.admin_frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.admin_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.admin_frame.setObjectName("admin_frame")
        self.list_label = QtWidgets.QLabel(self.admin_frame)
        self.list_label.setGeometry(QtCore.QRect(40, 40, 370, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.list_label.setFont(font)
        self.list_label.setAlignment(QtCore.Qt.AlignCenter)
        self.list_label.setObjectName("list_label")
        self.taxi_listWidget = QtWidgets.QListWidget(self.admin_frame)
        self.taxi_listWidget.setGeometry(QtCore.QRect(40, 120, 370, 221))
        self.taxi_listWidget.setObjectName("taxi_listWidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.admin_frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 350, 371, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_status = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame_status.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_status.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_status.setObjectName("frame_status")
        self.label_status_response = QtWidgets.QLabel(self.frame_status)
        self.label_status_response.setGeometry(QtCore.QRect(60, 0, 310, 30))
        self.label_status_response.setText("")
        self.label_status_response.setObjectName("label_status_response")
        self.label_status = QtWidgets.QLabel(self.frame_status)
        self.label_status.setGeometry(QtCore.QRect(0, 0, 60, 30))
        self.label_status.setObjectName("label_status")
        self.verticalLayout.addWidget(self.frame_status)
        self.frame_location = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame_location.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_location.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_location.setObjectName("frame_location")
        self.label_location_response = QtWidgets.QLabel(self.frame_location)
        self.label_location_response.setGeometry(QtCore.QRect(60, 0, 310, 30))
        self.label_location_response.setText("")
        self.label_location_response.setObjectName("label_location_response")
        self.label_location = QtWidgets.QLabel(self.frame_location)
        self.label_location.setGeometry(QtCore.QRect(0, 0, 60, 30))
        self.label_location.setObjectName("label_location")
        self.verticalLayout.addWidget(self.frame_location)
        self.frame_destination = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame_destination.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_destination.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_destination.setObjectName("frame_destination")
        self.label_destination_response = QtWidgets.QLabel(self.frame_destination)
        self.label_destination_response.setGeometry(QtCore.QRect(60, 0, 310, 30))
        self.label_destination_response.setText("")
        self.label_destination_response.setObjectName("label_destination_response")
        self.label_destination = QtWidgets.QLabel(self.frame_destination)
        self.label_destination.setGeometry(QtCore.QRect(0, 0, 60, 30))
        self.label_destination.setObjectName("label_destination")
        self.verticalLayout.addWidget(self.frame_destination)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Testing (delete)
        self.list()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Admin Access"))
        self.list_label.setText(_translate("Dialog", "Taxi list"))
        self.label_status.setText(_translate("Dialog", "Estado"))
        self.label_location.setText(_translate("Dialog", "Ubicacion"))
        self.label_destination.setText(_translate("Dialog", "Destino"))

    def list(self):
        self.myList = QtWidgets.QListWidget(self.taxi_listWidget)
        self.myList.setMinimumSize(370, 220)
        self.myList.setAlternatingRowColors(True)
        self.taxis = ['taxi1', 'taxi2', 'taxi3', 'taxi4', 'taxi5', 'taxi6', 'taxi7', 'taxi8', 'taxi9', 'taxi10',
                      'taxi11', 'taxi12', 'taxi13', 'taxi14', 'taxi15']
        # self.myList.addItems(self.taxis)

        count = 1
        for i in self.taxis:
            taxi = QtWidgets.QListWidgetItem(i, self.myList)
            taxi.setToolTip("Este es el taxi" + str(count))
            count = count + 1

        print('aqui llego')
        self.myList.itemClicked.connect(self.show_info)
        print('aqui tambn')

    def show_info(self):
        print('show')
        self.label_status_response.setText("Ocupado")
        self.label_location_response.setText("Perdido")
        self.label_destination_response.setText("Pa casa")
        print(self.myList.currentItem().text())
        print('fin show')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

