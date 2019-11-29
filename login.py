# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(221, 208)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-10, 170, 221, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.pwordEdit = QtWidgets.QLineEdit(Dialog)
        self.pwordEdit.setGeometry(QtCore.QRect(10, 120, 201, 20))
        self.pwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwordEdit.setObjectName("pwordEdit")
        self.userEdit = QtWidgets.QLineEdit(Dialog)
        self.userEdit.setGeometry(QtCore.QRect(10, 90, 201, 20))
        self.userEdit.setObjectName("userEdit")
        self.welcomeLabel = QtWidgets.QLabel(Dialog)
        self.welcomeLabel.setGeometry(QtCore.QRect(0, 10, 221, 20))
        self.welcomeLabel.setStyleSheet("text: \"testing\";")
        self.welcomeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.welcomeLabel.setObjectName("welcomeLabel")
        self.helpLabel = QtWidgets.QLabel(Dialog)
        self.helpLabel.setGeometry(QtCore.QRect(0, 40, 221, 41))
        self.helpLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.helpLabel.setWordWrap(True)
        self.helpLabel.setObjectName("helpLabel")
        self.showPasswordBox = QtWidgets.QCheckBox(Dialog)
        self.showPasswordBox.setGeometry(QtCore.QRect(10, 150, 101, 17))
        self.showPasswordBox.setObjectName("showPasswordBox")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pwordEdit.setPlaceholderText(_translate("Dialog", "password"))
        self.userEdit.setPlaceholderText(_translate("Dialog", "username"))
        self.welcomeLabel.setText(_translate("Dialog", "Welcome to MapleQt"))
        self.helpLabel.setText(_translate("Dialog", "Please login with your username and password. If you do not have one, it will be created upon logging in the first time."))
        self.showPasswordBox.setText(_translate("Dialog", "Show password"))
