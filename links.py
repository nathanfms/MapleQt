# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'links.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from skillIcon import skillIcon
from Mapler import addDicts
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
        self.total = {}
        self.setupUi()

    def setupUi(self):
        labelStyle = "border-radius: 10px; border: 2px solid black; qproperty-alignment: AlignCenter; background-color: rgb(79, 238, 238); font-size: 12px;"
        self.resize(375, 370)
        linksFile = open('jobs/Links.json')
        linksJson = json.load(linksFile)
        for skill in linksJson:
            if(skill.get("passive")):
                link = skillIcon(self)
                link.setSkill(skill)
                # x = (20 + (70 * (len(self.passive) // 5))) % 370
                x = 20 + ((70 * len(self.passive)) % 350)
                y = 25 + (40 * (len(self.passive) // 5))
                link.setGeometry(QtCore.QRect(x, y, 32, 32))
                self.passive.append(link)
                spinbox = QtWidgets.QSpinBox(self)
                spinbox.setGeometry(QtCore.QRect(x + 35, y, 31, 22))
                spinbox.setMaximum(len(skill.get("stats")))
                spinbox.setProperty("value", 0)
                spinbox.valueChanged.connect(self.updatePassiveLinks)
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
                spinbox.valueChanged.connect(self.updateActiveLinks)
                self.activeSpin.append(spinbox)
                checkbox = QtWidgets.QCheckBox(self)
                checkbox.setGeometry(QtCore.QRect(x + 8, 194, 16, 17))
                checkbox.stateChanged.connect(self.updateTotal)
                self.activeBox.append(checkbox)

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

        self.jettLabel = QtWidgets.QLabel(self)
        self.jettLabel.setGeometry(QtCore.QRect(10, 219, 51, 16))
        self.jettLabel.setStyleSheet("font-size: 14px;")
        self.jettLabel.setText("Jett")
        self.jettBox = QtWidgets.QCheckBox(self)
        self.jettBox.setGeometry(QtCore.QRect(40, 220, 16, 17))
        self.jettBox.stateChanged.connect(self.updateTotal)

        self.strLabel = QtWidgets.QLabel(self)
        self.strLabel.setGeometry(QtCore.QRect(10, 239, 81, 22))
        self.strLabel.setStyleSheet(labelStyle)
        self.strLabel.setText("STR")
        self.strSpin = QtWidgets.QSpinBox(self)
        self.strSpin.setGeometry(QtCore.QRect(100, 239, 42, 22))
        self.strSpin.setMaximum(35)
        self.strSpin.valueChanged.connect(self.updateTotal)

        self.dexLabel = QtWidgets.QLabel(self)
        self.dexLabel.setGeometry(QtCore.QRect(10, 259, 81, 22))
        self.dexLabel.setStyleSheet(labelStyle)
        self.dexLabel.setText("DEX")
        self.dexSpin = QtWidgets.QSpinBox(self)
        self.dexSpin.setGeometry(QtCore.QRect(100, 259, 42, 22))
        self.dexSpin.setMaximum(35)
        self.dexSpin.valueChanged.connect(self.updateTotal)

        self.intLabel = QtWidgets.QLabel(self)
        self.intLabel.setGeometry(QtCore.QRect(10, 279, 81, 22))
        self.intLabel.setStyleSheet(labelStyle)
        self.intLabel.setText("INT")
        self.intSpin = QtWidgets.QSpinBox(self)
        self.intSpin.setGeometry(QtCore.QRect(100, 279, 42, 22))
        self.intSpin.setMaximum(35)
        self.intSpin.valueChanged.connect(self.updateTotal)

        self.lukLabel = QtWidgets.QLabel(self)
        self.lukLabel.setGeometry(QtCore.QRect(10, 299, 81, 22))
        self.lukLabel.setStyleSheet(labelStyle)
        self.lukLabel.setText("LUK")
        self.lukSpin = QtWidgets.QSpinBox(self)
        self.lukSpin.setGeometry(QtCore.QRect(100, 299, 42, 22))
        self.lukSpin.setMaximum(35)
        self.lukSpin.valueChanged.connect(self.updateTotal)

        self.atkLabel = QtWidgets.QLabel(self)
        self.atkLabel.setGeometry(QtCore.QRect(10, 319, 81, 22))
        self.atkLabel.setStyleSheet(labelStyle)
        self.atkLabel.setText("ATK")
        self.atkSpin = QtWidgets.QSpinBox(self)
        self.atkSpin.setGeometry(QtCore.QRect(100, 319, 42, 22))
        self.atkSpin.setMaximum(35)
        self.atkSpin.valueChanged.connect(self.updateTotal)

        self.matkLabel = QtWidgets.QLabel(self)
        self.matkLabel.setGeometry(QtCore.QRect(10, 339, 81, 22))
        self.matkLabel.setStyleSheet(labelStyle)
        self.matkLabel.setText("M. ATK")
        self.matkSpin = QtWidgets.QSpinBox(self)
        self.matkSpin.setGeometry(QtCore.QRect(100, 339, 42, 22))
        self.matkSpin.setMaximum(35)
        self.matkSpin.valueChanged.connect(self.updateTotal)

        self.activeLinks = QtWidgets.QLabel(self)
        self.activeLinks.setGeometry(QtCore.QRect(280, 220, 130, 16))
        self.activeLinks.setStyleSheet("font-size: 14px;")
        self.activeLinks.setText("Active Links: 0")

        self.beginnerLabel = QtWidgets.QLabel(self)
        self.beginnerLabel.setGeometry(QtCore.QRect(233, 239, 181, 16))
        self.beginnerLabel.setStyleSheet("font-size: 14px;")
        self.beginnerLabel.setText("Beginner Passive Skills")

        self.blessingOfFairy = skillIcon(self)
        

        self.rebootLabel = QtWidgets.QLabel(self)
        self.rebootLabel.setGeometry(QtCore.QRect(233, 291, 181, 16))
        self.rebootLabel.setStyleSheet("font-size: 14px;")
        self.rebootLabel.setText("Reboot & Echo of Hero")



    def updateTotal(self):
        self.total.clear()
        linksApplied = 0
        for i in range(0, len(self.passive)):
            if(self.passiveSpin[i].value() != 0):
                self.total = addDicts(self.total, self.passive[i].getStats())
                linksApplied += 1
        for i in range(0, len(self.active)):
            if(self.activeBox[i].isChecked() and self.activeSpin[i].value() != 0):
                self.total = addDicts(self.total, self.active[i].getStats())
                linksApplied += 1
        if(self.jettBox.isChecked()):
            jett = {
                "STR": self.strSpin.value(),
                "DEX": self.dexSpin.value(),
                "INT": self.intSpin.value(),
                "LUK": self.lukSpin.value(),
                "ATK": self.atkSpin.value(),
                "MATK": self.matkSpin.value()
            }
            self.total = addDicts(self.total, jett)
            linksApplied += 1
        activeString = "Active Links: " + str(linksApplied)
        self.activeLinks.setText(activeString)

    def updatePassiveLinks(self):
        for i in range(0, len(self.passive)):
            skill = self.passive[i]
            spin = self.passiveSpin[i]
            skill.updateDecentLevel(spin.value())
        self.updateTotal()

    def updateActiveLinks(self):
        for i in range(0, len(self.active)):
            skill = self.active[i]
            spin = self.activeSpin[i]
            skill.updateDecentLevel(spin.value())
        self.updateTotal()

