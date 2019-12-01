# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'skillWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from skillIcon import skillIcon
import json


class skillController(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.passiveSkills = []
        self.activeSkills = []
        self.activeBoxes = []
        self.setupUi()

    def setupUi(self):
        decentJson = open('jobs/DecentPotential.json')
        decentSkills = json.load(decentJson)

        fifthJson = open('jobs/DecentFifth.json')
        fifthSkills = json.load(fifthJson)

        self.resize(510, 335)
        self.setMinimumSize(QtCore.QSize(510, 335))

        #Labels
        self.passiveLabel = QtWidgets.QLabel(self)
        self.passiveLabel.setGeometry(QtCore.QRect(10, 0, 51, 16))
        self.passiveLabel.setStyleSheet("font-size: 14px;")
        self.passiveLabel.setObjectName("passiveLabel")
        self.activeLabel = QtWidgets.QLabel(self)
        self.activeLabel.setGeometry(QtCore.QRect(10, 60, 47, 13))
        self.activeLabel.setStyleSheet("font-size: 14px;")
        self.activeLabel.setObjectName("activeLabel")
        self.decentPotLabel = QtWidgets.QLabel(self)
        self.decentPotLabel.setGeometry(QtCore.QRect(10, 132, 131, 16))
        self.decentPotLabel.setStyleSheet("font-size: 14px;")
        self.decentPotLabel.setObjectName("decentPotLabel")
        self.decentFifthLabel = QtWidgets.QLabel(self)
        self.decentFifthLabel.setGeometry(QtCore.QRect(10, 210, 200, 16))
        self.decentFifthLabel.setStyleSheet("font-size: 14px;")
        self.decentFifthLabel.setObjectName("decentFifthLabel")
        self.tipLabel = QtWidgets.QLabel(self)
        self.tipLabel.setGeometry(QtCore.QRect(10, 290, 411, 41))
        self.tipLabel.setObjectName("tipLabel")
        self.commonLabel = QtWidgets.QLabel(self)
        self.commonLabel.setGeometry(QtCore.QRect(290, 132, 131, 16))
        self.commonLabel.setStyleSheet("font-size: 14px;")
        self.commonLabel.setObjectName("commonLabel")
        #Label Text
        self.passiveLabel.setText("Passives")
        self.activeLabel.setText("Actives")
        self.decentPotLabel.setText("Decent Actives")
        self.decentFifthLabel.setText("Decent/Common Passives")
        self.tipLabel.setText("<html><head/><body><p>*A non-zero value for common skills will apply the passive stat boost.</p></body></html>")
        self.commonLabel.setText("Common 5th Job")

        #Passive Skill 1
        # self.pasSkill1 = skillIcon(self)
        # self.pasSkill1.setGeometry(QtCore.QRect(20, 20, 32, 32))
        # self.pasSkill1.setStyleSheet("background-color: rgb(176, 176, 176);")
        # self.pasSkill1.setObjectName("pasSkill1")
        # self.passiveSkills.append(self.pasSkill1)

        #Enable all active skills
        self.allActivesBox = QtWidgets.QCheckBox(self)
        self.allActivesBox.setGeometry(QtCore.QRect(60, 58, 70, 17))
        self.allActivesBox.setObjectName("allActivesBox")
        self.allActivesBox.setText("Enable All")

        #Active Skill 1
        # self.actSkill1 = skillIcon(self)
        # self.actSkill1.setGeometry(QtCore.QRect(20, 80, 32, 32))
        # self.actSkill1.setStyleSheet("background-color: rgb(176, 176, 176);")
        # self.actSkill1.setObjectName("actSkill1")
        # self.activeSkills.append(self.actSkill1)
        # self.actBox1 = QtWidgets.QCheckBox(self)
        # self.actBox1.setGeometry(QtCore.QRect(28, 114, 16, 17))
        # self.actBox1.setObjectName("actBox1")
        # self.activeBoxes.append(self.actBox1)

        #Sharp Eyes (Potential)
        self.decSeLabel = skillIcon(self)
        self.decSeLabel.setSkill(decentSkills[0]) #Not a fan of just using the index...¯\_(ツ)_/¯
        self.decSeLabel.setGeometry(QtCore.QRect(20, 152, 32, 32))
        self.decSeLabel.setObjectName("decSeLabel")
        self.decSeBox = QtWidgets.QCheckBox(self)
        self.decSeBox.setGeometry(QtCore.QRect(28, 186, 16, 17))
        self.decSeBox.setObjectName("decSeBox")
        
        #Advanced Blessing (Potential)
        self.decAbLabel = skillIcon(self)
        self.decAbLabel.setSkill(decentSkills[1])
        self.decAbLabel.setGeometry(QtCore.QRect(60, 152, 32, 32))
        self.decAbLabel.setObjectName("decAbLabel")
        self.decAbBox = QtWidgets.QCheckBox(self)
        self.decAbBox.setGeometry(QtCore.QRect(68, 186, 16, 17))
        self.decAbBox.setObjectName("decAbBox")

        #Hyper Body (Potential)
        self.decHbLabel = skillIcon(self)
        self.decHbLabel.setSkill(decentSkills[2])
        self.decHbLabel.setGeometry(QtCore.QRect(100, 152, 32, 32))
        self.decHbLabel.setObjectName("decHbLabel")
        self.decHbBox = QtWidgets.QCheckBox(self)
        self.decHbBox.setGeometry(QtCore.QRect(108, 186, 16, 17))
        self.decHbBox.setObjectName("decHbBox")

        #Combat Orders (Potential)
        self.decCoLabel = skillIcon(self)
        self.decCoLabel.setSkill(decentSkills[3])
        self.decCoLabel.setGeometry(QtCore.QRect(140, 152, 32, 32))
        self.decCoLabel.setObjectName("decCoLabel")
        self.decCoBox = QtWidgets.QCheckBox(self)
        self.decCoBox.setGeometry(QtCore.QRect(148, 186, 16, 17))
        self.decCoBox.setObjectName("decCoBox")
        
        #Sharp Eyes (Fifth)
        self.fifthSeLabel = skillIcon(self)
        self.fifthSeLabel.setSkill(fifthSkills[0])
        self.fifthSeLabel.setGeometry(QtCore.QRect(20, 230, 32, 32))
        self.fifthSeLabel.setObjectName("fifthSeLabel")
        self.fifthSeSpin = QtWidgets.QSpinBox(self)
        self.fifthSeSpin.setGeometry(QtCore.QRect(55, 230, 31, 22))
        self.fifthSeSpin.setMaximum(30)
        self.fifthSeSpin.setProperty("value", 0)
        self.fifthSeSpin.setObjectName("fifthSeSpin")
        self.fifthSeSpin.valueChanged.connect(self.updateSkillToolTips)

        #Hyper Body (Fifth)
        self.fifthHbLabel = skillIcon(self)
        self.fifthHbLabel.setSkill(fifthSkills[1])
        self.fifthHbLabel.setGeometry(QtCore.QRect(90, 230, 32, 32))
        self.fifthHbLabel.setObjectName("fifthHbLabel")
        self.fifthHbSpin = QtWidgets.QSpinBox(self)
        self.fifthHbSpin.setGeometry(QtCore.QRect(125, 230, 31, 22))
        self.fifthHbSpin.setMaximum(30)
        self.fifthHbSpin.setProperty("value", 0)
        self.fifthHbSpin.setObjectName("fifthHbSpin")
        self.fifthHbSpin.valueChanged.connect(self.updateSkillToolTips)
        
        #Mystic Door (Fifth)
        self.fifthDoorLabel = skillIcon(self)
        self.fifthDoorLabel.setSkill(fifthSkills[2])
        self.fifthDoorLabel.setGeometry(QtCore.QRect(160, 230, 32, 32))
        self.fifthDoorLabel.setObjectName("fifthDoorLabel")
        # self.fifthDoorBox = QtWidgets.QCheckBox(self)
        # self.fifthDoorBox.setGeometry(QtCore.QRect(168, 264, 16, 17))
        # self.fifthDoorBox.setObjectName("fifthDoorBox")
        self.fifthDoorSpin = QtWidgets.QSpinBox(self)
        self.fifthDoorSpin.setGeometry(QtCore.QRect(195, 230, 31, 22))
        self.fifthDoorSpin.setMaximum(30)
        self.fifthDoorSpin.setProperty("value", 0)
        self.fifthDoorSpin.setObjectName("fifthDoorSpin")
        self.fifthDoorSpin.valueChanged.connect(self.updateSkillToolTips)

        #Blink (Fifth)
        self.fifthBlinkLabel = skillIcon(self)
        self.fifthBlinkLabel.setSkill(fifthSkills[3])
        self.fifthBlinkLabel.setGeometry(QtCore.QRect(230, 230, 32, 32))
        self.fifthBlinkLabel.setObjectName("fifthBlinkLabel")
        # self.fifthBlinkBox = QtWidgets.QCheckBox(self)
        # self.fifthBlinkBox.setGeometry(QtCore.QRect(238, 264, 16, 17))
        # self.fifthBlinkBox.setObjectName("fifthBlinkBox")
        self.fifthBlinkSpin = QtWidgets.QSpinBox(self)
        self.fifthBlinkSpin.setGeometry(QtCore.QRect(265, 230, 31, 22))
        self.fifthBlinkSpin.setMaximum(30)
        self.fifthBlinkSpin.setProperty("value", 0)
        self.fifthBlinkSpin.setObjectName("fifthBlinkSpin")
        self.fifthBlinkSpin.valueChanged.connect(self.updateSkillToolTips)

        #Rope Lift (Fifth)
        self.fifthRopeLabel = skillIcon(self)
        self.fifthRopeLabel.setSkill(fifthSkills[4])
        self.fifthRopeLabel.setGeometry(QtCore.QRect(300, 230, 32, 32))
        self.fifthRopeLabel.setObjectName("fifthRopeLabel")
        # self.fifthRopeBox = QtWidgets.QCheckBox(self)
        # self.fifthRopeBox.setGeometry(QtCore.QRect(308, 264, 16, 17))
        # self.fifthRopeBox.setObjectName("fifthRopeBox")
        self.fifthRopeSpin = QtWidgets.QSpinBox(self)
        self.fifthRopeSpin.setGeometry(QtCore.QRect(335, 230, 31, 22))
        self.fifthRopeSpin.setMaximum(30)
        self.fifthRopeSpin.setProperty("value", 0)
        self.fifthRopeSpin.setObjectName("fifthRopeSpin")
        self.fifthRopeSpin.valueChanged.connect(self.updateSkillToolTips)

        #Speed Infusion (Fifth)
        self.fifthSiLabel = skillIcon(self)
        self.fifthSiLabel.setSkill(fifthSkills[5])
        self.fifthSiLabel.setGeometry(QtCore.QRect(370, 230, 32, 32))
        self.fifthSiLabel.setObjectName("fifthSiLabel")
        # self.fifthSiBox = QtWidgets.QCheckBox(self)
        # self.fifthSiBox.setGeometry(QtCore.QRect(378, 264, 16, 17))
        # self.fifthSiBox.setObjectName("fifthSiBox")
        self.fifthSiSpin = QtWidgets.QSpinBox(self)
        self.fifthSiSpin.setGeometry(QtCore.QRect(405, 230, 31, 22))
        self.fifthSiSpin.setMaximum(30)
        self.fifthSiSpin.setProperty("value", 0)
        self.fifthSiSpin.setObjectName("fifthSiSpin")
        self.fifthSiSpin.valueChanged.connect(self.updateSkillToolTips)
        
        #Common Skill 1
        self.comSkill1 = skillIcon(self)
        self.comSkill1.setGeometry(QtCore.QRect(300, 152, 32, 32))
        self.comSkill1.setStyleSheet("background-color: rgb(176, 176, 176);")
        self.comSkill1.setObjectName("comSkill1")
        self.comSpin1 = QtWidgets.QSpinBox(self)
        self.comSpin1.setGeometry(QtCore.QRect(335, 152, 31, 22))
        self.comSpin1.setMaximum(30)
        self.comSpin1.setProperty("value", 0)
        self.comSpin1.setObjectName("comSpin1")
        self.comBox1 = QtWidgets.QCheckBox(self)
        self.comBox1.setGeometry(QtCore.QRect(308, 186, 16, 17))
        self.comBox1.setObjectName("comBox1")

    def loadJobSkills(self, json):
        for skill in json:
            if(skill.get("passive") is True):
                passive = skillIcon(self)
                passive.setSkill(skill)
                x = 20 + (40 * len(self.passiveSkills))
                passive.setGeometry(QtCore.QRect(x, 20, 32, 32))
                self.passiveSkills.append(passive)
            else:
                active = skillIcon(self)
                active.setSkill(skill)
                x = 20 + (40 * len(self.activeSkills))
                active.setGeometry(QtCore.QRect(x, 80, 32, 32))
                self.activeSkills.append(active)
                box = QtWidgets.QCheckBox(self)
                x += 8
                box.setGeometry(QtCore.QRect(x, 114, 16, 17))
                self.activeBoxes.append(box)
        
    def updateSkillToolTips(self):
        self.fifthSeLabel.updateLevel(self.fifthSeSpin.value())
        self.fifthHbLabel.updateLevel(self.fifthHbSpin.value())
        self.fifthDoorLabel.updateLevel(self.fifthDoorSpin.value())
        self.fifthBlinkLabel.updateLevel(self.fifthBlinkSpin.value())
        self.fifthRopeLabel.updateLevel(self.fifthRopeSpin.value())
        self.fifthSiLabel.updateLevel(self.fifthSiSpin.value())