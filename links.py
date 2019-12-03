# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'links.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from skillIcon import skillIcon
import json
import os

class linkSkillController(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.passive = []
        self.passiveSpin = []
        self.active = []
        self.activeSpin = []
        self.activeBox = []
        self.setupUi()

    def setupUi(self):
        self.resize(375, 215)
        linksFile = open('jobs/Links.json')
        linksJson = json.load(linksFile)
        for skill in linksJson:
            if(skill.get("passive")):
                link = skillIcon(self)
                link.setSkill(skill)
                # x = (20 + (70 * (len(self.passive) // 5))) % 370
                x = 20 + ((70 * len(self.passive)) % 350)
                print(x)
                y = 25 + (40 * (len(self.passive) // 5))
                link.setGeometry(QtCore.QRect(x, y, 32, 32))
                self.passive.append(link)
                spinbox = QtWidgets.QSpinBox(self)
                spinbox.setGeometry(QtCore.QRect(x + 35, y, 31, 22))
                spinbox.setMaximum(len(skill.get("stats")))
                spinbox.setProperty("value", 0)
                self.passiveSpin.append(spinbox)
            else:
                link = skillIcon(self)
                link.setSkill(skill)
                x = 20 + (70 * len(self.active))
                link.setGeometry(QtCore.QRect(x, 160, 32, 32))
                self.active.append(link)
                spinbox = QtWidgets.QSpinBox(self)
                spinbox.setGeometry(QtCore.QRect(x + 35, 160, 31, 22))
                spinbox.setMaximum(len(skill.get("stats")))
                spinbox.setProperty("value", 0)
                self.activeSpin.append(spinbox)
                checkbox = QtWidgets.QCheckBox(self)
                checkbox.setGeometry(QtCore.QRect(x + 8, 194, 16, 17))
                self.activeBox.append(checkbox)


        
        # self.actLabel1 = QtWidgets.QLabel(self)
        # self.actLabel1.setGeometry(QtCore.QRect(20, 160, 32, 32))
        # self.actLabel1.setStyleSheet("background-color: rgb(176, 176, 176);")
        # self.actLabel1.setText("")
        # self.actLabel1.setPixmap(QtGui.QPixmap("assets/skills/common/se.png"))
        # self.actLabel1.setObjectName("actLabel1")
        # self.actSpin1 = QtWidgets.QSpinBox(self)
        # self.actSpin1.setGeometry(QtCore.QRect(55, 160, 31, 22))
        # self.actSpin1.setMaximum(30)
        # self.actSpin1.setProperty("value", 0)
        # self.actSpin1.setObjectName("actSpin1")
        # self.actBox1 = QtWidgets.QCheckBox(self)
        # self.actBox1.setGeometry(QtCore.QRect(28, 194, 16, 17))
        # self.actBox1.setText("")
        # self.actBox1.setObjectName("actBox1")
        self.passiveLabel = QtWidgets.QLabel(self)
        self.passiveLabel.setGeometry(QtCore.QRect(10, 5, 181, 16))
        self.passiveLabel.setStyleSheet("font-size: 14px;")
        self.passiveLabel.setObjectName("passiveLabel")
        self.passiveLabel.setText("Passive Link Skills")
        self.activeLabel = QtWidgets.QLabel(self)
        self.activeLabel.setGeometry(QtCore.QRect(10, 140, 181, 16))
        self.activeLabel.setStyleSheet("font-size: 14px;")
        self.activeLabel.setObjectName("activeLabel")
        self.activeLabel.setText("Active Link Skills")
        # self.pas1Label = QtWidgets.QLabel(self)
        # self.pas1Label.setGeometry(QtCore.QRect(20, 25, 32, 32))
        # self.pas1Label.setStyleSheet("background-color: rgb(176, 176, 176);")
        # self.pas1Label.setText("")
        # self.pas1Label.setPixmap(QtGui.QPixmap("assets/skills/common/se.png"))
        # self.pas1Label.setObjectName("pas1Label")
        # self.pas1Spin = QtWidgets.QSpinBox(self)
        # self.pas1Spin.setGeometry(QtCore.QRect(55, 25, 31, 22))
        # self.pas1Spin.setMaximum(30)
        # self.pas1Spin.setProperty("value", 0)
        # self.pas1Spin.setObjectName("pas1Spin")
        # self.pas2Label = QtWidgets.QLabel(self)
        # self.pas2Label.setGeometry(QtCore.QRect(20, 65, 32, 32))
        # self.pas2Label.setStyleSheet("background-color: rgb(176, 176, 176);")
        # self.pas2Label.setText("")
        # self.pas2Label.setPixmap(QtGui.QPixmap("assets/skills/common/se.png"))
        # self.pas2Label.setObjectName("pas2Label")
        # self.pas2Spin = QtWidgets.QSpinBox(self)
        # self.pas2Spin.setGeometry(QtCore.QRect(55, 65, 31, 22))
        # self.pas2Spin.setMaximum(30)
        # self.pas2Spin.setProperty("value", 0)
        # self.pas2Spin.setObjectName("pas2Spin")
        # self.pas3Spin = QtWidgets.QSpinBox(self)
        # self.pas3Spin.setGeometry(QtCore.QRect(55, 105, 31, 22))
        # self.pas3Spin.setMaximum(30)
        # self.pas3Spin.setProperty("value", 0)
        # self.pas3Spin.setObjectName("pas3Spin")
        # self.pas3Label = QtWidgets.QLabel(self)
        # self.pas3Label.setGeometry(QtCore.QRect(20, 105, 32, 32))
        # self.pas3Label.setStyleSheet("background-color: rgb(176, 176, 176);")
        # self.pas3Label.setText("")
        # self.pas3Label.setPixmap(QtGui.QPixmap("assets/skills/common/se.png"))
        # self.pas3Label.setObjectName("pas3Label")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.passiveLabel.setText(_translate("Form", "Passive Link Skills"))
        self.activeLabel.setText(_translate("Form", "Active Link Skills"))
