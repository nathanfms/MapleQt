# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'skillWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(510, 335)
        Form.setMinimumSize(QtCore.QSize(132, 139))
        self.passiveLabel = QtWidgets.QLabel(Form)
        self.passiveLabel.setGeometry(QtCore.QRect(10, 0, 51, 16))
        self.passiveLabel.setStyleSheet("font-size: 14px;")
        self.passiveLabel.setObjectName("passiveLabel")
        self.activeLabel = QtWidgets.QLabel(Form)
        self.activeLabel.setGeometry(QtCore.QRect(10, 60, 47, 13))
        self.activeLabel.setStyleSheet("font-size: 14px;")
        self.activeLabel.setObjectName("activeLabel")
        self.pasSkill1 = QtWidgets.QLabel(Form)
        self.pasSkill1.setGeometry(QtCore.QRect(20, 20, 32, 32))
        self.pasSkill1.setStyleSheet("background-color: rgb(176, 176, 176);")
        self.pasSkill1.setText("")
        self.pasSkill1.setPixmap(QtGui.QPixmap("qt-creator-files/dummy-item.png"))
        self.pasSkill1.setObjectName("pasSkill1")
        self.actSkill1 = QtWidgets.QLabel(Form)
        self.actSkill1.setGeometry(QtCore.QRect(20, 80, 32, 32))
        self.actSkill1.setStyleSheet("background-color: rgb(176, 176, 176);")
        self.actSkill1.setText("")
        self.actSkill1.setPixmap(QtGui.QPixmap("qt-creator-files/dummy-item.png"))
        self.actSkill1.setObjectName("actSkill1")
        self.actBox1 = QtWidgets.QCheckBox(Form)
        self.actBox1.setGeometry(QtCore.QRect(28, 114, 16, 17))
        self.actBox1.setText("")
        self.actBox1.setObjectName("actBox1")
        self.allActivesBox = QtWidgets.QCheckBox(Form)
        self.allActivesBox.setGeometry(QtCore.QRect(60, 58, 70, 17))
        self.allActivesBox.setObjectName("allActivesBox")
        self.decentPotLabel = QtWidgets.QLabel(Form)
        self.decentPotLabel.setGeometry(QtCore.QRect(10, 132, 131, 16))
        self.decentPotLabel.setStyleSheet("font-size: 14px;")
        self.decentPotLabel.setObjectName("decentPotLabel")
        self.decSeBox = QtWidgets.QCheckBox(Form)
        self.decSeBox.setGeometry(QtCore.QRect(28, 186, 16, 17))
        self.decSeBox.setText("")
        self.decSeBox.setObjectName("decSeBox")
        self.decSeLabel = QtWidgets.QLabel(Form)
        self.decSeLabel.setGeometry(QtCore.QRect(20, 152, 32, 32))
        self.decSeLabel.setStyleSheet("background-color: rgb(176, 176, 176);")
        self.decSeLabel.setText("")
        self.decSeLabel.setPixmap(QtGui.QPixmap("assets/skills/common/se.png"))
        self.decSeLabel.setObjectName("decSeLabel")
        self.fifthSeLabel = QtWidgets.QLabel(Form)
        self.fifthSeLabel.setGeometry(QtCore.QRect(20, 230, 32, 32))
        self.fifthSeLabel.setStyleSheet("background-color: rgb(176, 176, 176);")
        self.fifthSeLabel.setText("")
        self.fifthSeLabel.setPixmap(QtGui.QPixmap("assets/skills/common/se.png"))
        self.fifthSeLabel.setObjectName("fifthSeLabel")
        self.fifthSeBox = QtWidgets.QCheckBox(Form)
        self.fifthSeBox.setGeometry(QtCore.QRect(28, 264, 16, 17))
        self.fifthSeBox.setText("")
        self.fifthSeBox.setObjectName("fifthSeBox")
        self.decentFifthLabel = QtWidgets.QLabel(Form)
        self.decentFifthLabel.setGeometry(QtCore.QRect(10, 210, 121, 16))
        self.decentFifthLabel.setStyleSheet("font-size: 14px;")
        self.decentFifthLabel.setObjectName("decentFifthLabel")
        self.decAbLabel = QtWidgets.QLabel(Form)
        self.decAbLabel.setGeometry(QtCore.QRect(60, 152, 32, 32))
        self.decAbLabel.setStyleSheet("background-color: rgb(176, 176, 176);")
        self.decAbLabel.setText("")
        self.decAbLabel.setPixmap(QtGui.QPixmap("assets/skills/common/ab.png"))
        self.decAbLabel.setObjectName("decAbLabel")
        self.decAbBox = QtWidgets.QCheckBox(Form)
        self.decAbBox.setGeometry(QtCore.QRect(68, 186, 16, 17))
        self.decAbBox.setText("")
        self.decAbBox.setObjectName("decAbBox")
        self.decCoBox = QtWidgets.QCheckBox(Form)
        self.decCoBox.setGeometry(QtCore.QRect(148, 186, 16, 17))
        self.decCoBox.setText("")
        self.decCoBox.setObjectName("decCoBox")
        self.decHbBox = QtWidgets.QCheckBox(Form)
        self.decHbBox.setGeometry(QtCore.QRect(108, 186, 16, 17))
        self.decHbBox.setText("")
        self.decHbBox.setObjectName("decHbBox")
        self.decHbLabel = QtWidgets.QLabel(Form)
        self.decHbLabel.setGeometry(QtCore.QRect(100, 152, 32, 32))
        self.decHbLabel.setStyleSheet("background-color: rgb(176, 176, 176);")
        self.decHbLabel.setText("")
        self.decHbLabel.setPixmap(QtGui.QPixmap("assets/skills/common/hb.png"))
        self.decHbLabel.setObjectName("decHbLabel")
        self.decCoLabel = QtWidgets.QLabel(Form)
        self.decCoLabel.setGeometry(QtCore.QRect(140, 152, 32, 32))
        self.decCoLabel.setStyleSheet("background-color: rgb(176, 176, 176);")
        self.decCoLabel.setText("")
        self.decCoLabel.setPixmap(QtGui.QPixmap("assets/skills/common/co.png"))
        self.decCoLabel.setObjectName("decCoLabel")
        self.fifthAbBox = QtWidgets.QCheckBox(Form)
        self.fifthAbBox.setGeometry(QtCore.QRect(98, 264, 16, 17))
        self.fifthAbBox.setText("")
        self.fifthAbBox.setObjectName("fifthAbBox")
        self.fifthAbLabel = QtWidgets.QLabel(Form)
        self.fifthAbLabel.setGeometry(QtCore.QRect(90, 230, 32, 32))
        self.fifthAbLabel.setStyleSheet("background-color: rgb(176, 176, 176);")
        self.fifthAbLabel.setText("")
        self.fifthAbLabel.setPixmap(QtGui.QPixmap("assets/skills/common/ab.png"))
        self.fifthAbLabel.setObjectName("fifthAbLabel")
        self.fifthDoorLabel = QtWidgets.QLabel(Form)
        self.fifthDoorLabel.setGeometry(QtCore.QRect(230, 230, 32, 32))
        self.fifthDoorLabel.setStyleSheet("background-color: rgb(176, 176, 176);")
        self.fifthDoorLabel.setText("")
        self.fifthDoorLabel.setPixmap(QtGui.QPixmap("assets/skills/common/door.png"))
        self.fifthDoorLabel.setObjectName("fifthDoorLabel")
        self.fifthHbLabel = QtWidgets.QLabel(Form)
        self.fifthHbLabel.setGeometry(QtCore.QRect(160, 230, 32, 32))
        self.fifthHbLabel.setStyleSheet("background-color: rgb(176, 176, 176);")
        self.fifthHbLabel.setText("")
        self.fifthHbLabel.setPixmap(QtGui.QPixmap("assets/skills/common/hb.png"))
        self.fifthHbLabel.setObjectName("fifthHbLabel")
        self.fifthHbBox = QtWidgets.QCheckBox(Form)
        self.fifthHbBox.setGeometry(QtCore.QRect(168, 264, 16, 17))
        self.fifthHbBox.setText("")
        self.fifthHbBox.setObjectName("fifthHbBox")
        self.fifthDoorBox = QtWidgets.QCheckBox(Form)
        self.fifthDoorBox.setGeometry(QtCore.QRect(238, 264, 16, 17))
        self.fifthDoorBox.setText("")
        self.fifthDoorBox.setObjectName("fifthDoorBox")
        self.fifthRopeBox = QtWidgets.QCheckBox(Form)
        self.fifthRopeBox.setGeometry(QtCore.QRect(378, 264, 16, 17))
        self.fifthRopeBox.setText("")
        self.fifthRopeBox.setObjectName("fifthRopeBox")
        self.fifthRopeLabel = QtWidgets.QLabel(Form)
        self.fifthRopeLabel.setGeometry(QtCore.QRect(370, 230, 32, 32))
        self.fifthRopeLabel.setStyleSheet("background-color: rgb(176, 176, 176);")
        self.fifthRopeLabel.setText("")
        self.fifthRopeLabel.setPixmap(QtGui.QPixmap("assets/skills/common/ropelift.png"))
        self.fifthRopeLabel.setObjectName("fifthRopeLabel")
        self.fifthBlinkBox = QtWidgets.QCheckBox(Form)
        self.fifthBlinkBox.setGeometry(QtCore.QRect(308, 264, 16, 17))
        self.fifthBlinkBox.setText("")
        self.fifthBlinkBox.setObjectName("fifthBlinkBox")
        self.fifthBlinkLabel = QtWidgets.QLabel(Form)
        self.fifthBlinkLabel.setGeometry(QtCore.QRect(300, 230, 32, 32))
        self.fifthBlinkLabel.setStyleSheet("background-color: rgb(176, 176, 176);")
        self.fifthBlinkLabel.setText("")
        self.fifthBlinkLabel.setPixmap(QtGui.QPixmap("assets/skills/common/blink.png"))
        self.fifthBlinkLabel.setObjectName("fifthBlinkLabel")
        self.fifthSiLabel = QtWidgets.QLabel(Form)
        self.fifthSiLabel.setGeometry(QtCore.QRect(440, 230, 32, 32))
        self.fifthSiLabel.setStyleSheet("background-color: rgb(176, 176, 176);")
        self.fifthSiLabel.setText("")
        self.fifthSiLabel.setPixmap(QtGui.QPixmap("assets/skills/common/si.png"))
        self.fifthSiLabel.setObjectName("fifthSiLabel")
        self.fifthSiBox = QtWidgets.QCheckBox(Form)
        self.fifthSiBox.setGeometry(QtCore.QRect(448, 264, 16, 17))
        self.fifthSiBox.setText("")
        self.fifthSiBox.setObjectName("fifthSiBox")
        self.tipLabel = QtWidgets.QLabel(Form)
        self.tipLabel.setGeometry(QtCore.QRect(10, 290, 411, 41))
        self.tipLabel.setObjectName("tipLabel")
        self.fifthRopeSpin = QtWidgets.QSpinBox(Form)
        self.fifthRopeSpin.setGeometry(QtCore.QRect(405, 230, 31, 22))
        self.fifthRopeSpin.setMaximum(30)
        self.fifthRopeSpin.setProperty("value", 0)
        self.fifthRopeSpin.setObjectName("fifthRopeSpin")
        self.fifthSiSpin = QtWidgets.QSpinBox(Form)
        self.fifthSiSpin.setGeometry(QtCore.QRect(475, 230, 31, 22))
        self.fifthSiSpin.setMaximum(30)
        self.fifthSiSpin.setProperty("value", 0)
        self.fifthSiSpin.setObjectName("fifthSiSpin")
        self.fifthSeSpin = QtWidgets.QSpinBox(Form)
        self.fifthSeSpin.setGeometry(QtCore.QRect(55, 230, 31, 22))
        self.fifthSeSpin.setMaximum(30)
        self.fifthSeSpin.setProperty("value", 0)
        self.fifthSeSpin.setObjectName("fifthSeSpin")
        self.fifthAbSpin = QtWidgets.QSpinBox(Form)
        self.fifthAbSpin.setGeometry(QtCore.QRect(125, 230, 31, 22))
        self.fifthAbSpin.setMaximum(30)
        self.fifthAbSpin.setProperty("value", 0)
        self.fifthAbSpin.setObjectName("fifthAbSpin")
        self.fifthHbSpin = QtWidgets.QSpinBox(Form)
        self.fifthHbSpin.setGeometry(QtCore.QRect(195, 230, 31, 22))
        self.fifthHbSpin.setMaximum(30)
        self.fifthHbSpin.setProperty("value", 0)
        self.fifthHbSpin.setObjectName("fifthHbSpin")
        self.fifthDoorSpin = QtWidgets.QSpinBox(Form)
        self.fifthDoorSpin.setGeometry(QtCore.QRect(265, 230, 31, 22))
        self.fifthDoorSpin.setMaximum(30)
        self.fifthDoorSpin.setProperty("value", 0)
        self.fifthDoorSpin.setObjectName("fifthDoorSpin")
        self.fifthBlinkSpin = QtWidgets.QSpinBox(Form)
        self.fifthBlinkSpin.setGeometry(QtCore.QRect(335, 230, 31, 22))
        self.fifthBlinkSpin.setMaximum(30)
        self.fifthBlinkSpin.setProperty("value", 0)
        self.fifthBlinkSpin.setObjectName("fifthBlinkSpin")
        self.commonLabel = QtWidgets.QLabel(Form)
        self.commonLabel.setGeometry(QtCore.QRect(290, 132, 131, 16))
        self.commonLabel.setStyleSheet("font-size: 14px;")
        self.commonLabel.setObjectName("commonLabel")
        self.comSpin1 = QtWidgets.QSpinBox(Form)
        self.comSpin1.setGeometry(QtCore.QRect(335, 152, 31, 22))
        self.comSpin1.setMaximum(30)
        self.comSpin1.setProperty("value", 0)
        self.comSpin1.setObjectName("comSpin1")
        self.comBox1 = QtWidgets.QCheckBox(Form)
        self.comBox1.setGeometry(QtCore.QRect(308, 186, 16, 17))
        self.comBox1.setText("")
        self.comBox1.setObjectName("comBox1")
        self.comSkill1 = QtWidgets.QLabel(Form)
        self.comSkill1.setGeometry(QtCore.QRect(300, 152, 32, 32))
        self.comSkill1.setStyleSheet("background-color: rgb(176, 176, 176);")
        self.comSkill1.setText("")
        self.comSkill1.setObjectName("comSkill1")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.passiveLabel.setText(_translate("Form", "Passives"))
        self.activeLabel.setText(_translate("Form", "Actives"))
        self.allActivesBox.setText(_translate("Form", "Enable All"))
        self.decentPotLabel.setText(_translate("Form", "Decents (Potential)"))
        self.decentFifthLabel.setText(_translate("Form", "Decents (Fifth Job)"))
        self.tipLabel.setText(_translate("Form", "<html><head/><body><p>*For 5th job Combat Orders, just use the Decent (Potential) one.</p><p>*Fifth Job Decents are included because they passively give a small amount of stat.</p></body></html>"))
        self.commonLabel.setText(_translate("Form", "Common 5th Job"))