# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'links.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(375, 215)
        self.actLabel1 = QtWidgets.QLabel(Form)
        self.actLabel1.setGeometry(QtCore.QRect(20, 160, 32, 32))
        self.actLabel1.setStyleSheet("background-color: rgb(176, 176, 176);")
        self.actLabel1.setText("")
        self.actLabel1.setPixmap(QtGui.QPixmap("assets/skills/common/se.png"))
        self.actLabel1.setObjectName("actLabel1")
        self.actSpin1 = QtWidgets.QSpinBox(Form)
        self.actSpin1.setGeometry(QtCore.QRect(55, 160, 31, 22))
        self.actSpin1.setMaximum(30)
        self.actSpin1.setProperty("value", 0)
        self.actSpin1.setObjectName("actSpin1")
        self.actBox1 = QtWidgets.QCheckBox(Form)
        self.actBox1.setGeometry(QtCore.QRect(28, 194, 16, 17))
        self.actBox1.setText("")
        self.actBox1.setObjectName("actBox1")
        self.passiveLabel = QtWidgets.QLabel(Form)
        self.passiveLabel.setGeometry(QtCore.QRect(10, 5, 181, 16))
        self.passiveLabel.setStyleSheet("font-size: 14px;")
        self.passiveLabel.setObjectName("passiveLabel")
        self.activeLabel = QtWidgets.QLabel(Form)
        self.activeLabel.setGeometry(QtCore.QRect(10, 140, 181, 16))
        self.activeLabel.setStyleSheet("font-size: 14px;")
        self.activeLabel.setObjectName("activeLabel")
        self.pas1Label = QtWidgets.QLabel(Form)
        self.pas1Label.setGeometry(QtCore.QRect(20, 25, 32, 32))
        self.pas1Label.setStyleSheet("background-color: rgb(176, 176, 176);")
        self.pas1Label.setText("")
        self.pas1Label.setPixmap(QtGui.QPixmap("assets/skills/common/se.png"))
        self.pas1Label.setObjectName("pas1Label")
        self.pas1Spin = QtWidgets.QSpinBox(Form)
        self.pas1Spin.setGeometry(QtCore.QRect(55, 25, 31, 22))
        self.pas1Spin.setMaximum(30)
        self.pas1Spin.setProperty("value", 0)
        self.pas1Spin.setObjectName("pas1Spin")
        self.pas2Label = QtWidgets.QLabel(Form)
        self.pas2Label.setGeometry(QtCore.QRect(20, 65, 32, 32))
        self.pas2Label.setStyleSheet("background-color: rgb(176, 176, 176);")
        self.pas2Label.setText("")
        self.pas2Label.setPixmap(QtGui.QPixmap("assets/skills/common/se.png"))
        self.pas2Label.setObjectName("pas2Label")
        self.pas2Spin = QtWidgets.QSpinBox(Form)
        self.pas2Spin.setGeometry(QtCore.QRect(55, 65, 31, 22))
        self.pas2Spin.setMaximum(30)
        self.pas2Spin.setProperty("value", 0)
        self.pas2Spin.setObjectName("pas2Spin")
        self.pas3Spin = QtWidgets.QSpinBox(Form)
        self.pas3Spin.setGeometry(QtCore.QRect(55, 105, 31, 22))
        self.pas3Spin.setMaximum(30)
        self.pas3Spin.setProperty("value", 0)
        self.pas3Spin.setObjectName("pas3Spin")
        self.pas3Label = QtWidgets.QLabel(Form)
        self.pas3Label.setGeometry(QtCore.QRect(20, 105, 32, 32))
        self.pas3Label.setStyleSheet("background-color: rgb(176, 176, 176);")
        self.pas3Label.setText("")
        self.pas3Label.setPixmap(QtGui.QPixmap("assets/skills/common/se.png"))
        self.pas3Label.setObjectName("pas3Label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.passiveLabel.setText(_translate("Form", "Passive Link Skills"))
        self.activeLabel.setText(_translate("Form", "Active Link Skills"))
