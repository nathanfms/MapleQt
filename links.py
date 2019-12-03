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

#Even though it's named after link skills, it also includes beginner skills

class linkSkillController(QtWidgets.QWidget):
    def __init__(self, parent=None, valuesChanged=None):
        super().__init__(parent)
        self.passive = []
        self.passiveSpin = []
        self.active = []
        self.activeSpin = []
        self.activeBox = []
        self.total = {}
        self.notifyParent = valuesChanged
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
        self.activeLinks.setGeometry(QtCore.QRect(140, 220, 130, 16))
        self.activeLinks.setStyleSheet("font-size: 14px;")
        self.activeLinks.setText("Active Links: 0")

        self.beginnerLabel = QtWidgets.QLabel(self)
        self.beginnerLabel.setGeometry(QtCore.QRect(233, 239, 181, 16))
        self.beginnerLabel.setStyleSheet("font-size: 14px;")
        self.beginnerLabel.setText("Beginner Passive Skills")

        blessFile = open('jobs/Blessings.json')
        blessJson = json.load(blessFile)

        self.blessingOfFairy = skillIcon(self)
        self.blessingOfFairy.setSkill(blessJson[0])
        self.blessingOfFairy.setGeometry(QtCore.QRect(233, 260, 32, 32))
        self.fairySpin = QtWidgets.QSpinBox(self)
        self.fairySpin.setGeometry(QtCore.QRect(268, 260, 31, 22))
        self.fairySpin.setMaximum(20)
        self.fairySpin.valueChanged.connect(self.updateTotal)

        self.blessingOfEmpress = skillIcon(self)
        self.blessingOfEmpress.setSkill(blessJson[1])
        self.blessingOfEmpress.setGeometry(QtCore.QRect(303, 260, 32, 32))
        self.empSpin = QtWidgets.QSpinBox(self)
        self.empSpin.setGeometry(QtCore.QRect(338, 260, 31, 22))
        self.empSpin.setMaximum(24)
        self.empSpin.valueChanged.connect(self.updateTotal)

        self.echoLabel = QtWidgets.QLabel(self)
        self.echoLabel.setGeometry(QtCore.QRect(233, 291, 181, 16))
        self.echoLabel.setStyleSheet("font-size: 14px;")
        self.echoLabel.setText("Echo of Hero")

        self.echo = skillIcon(self)
        self.echo.setSkill(blessJson[2])
        self.echo.setGeometry(QtCore.QRect(233, 310, 32, 32))
        self.echoBox = QtWidgets.QCheckBox(self)
        self.echoBox.setGeometry(QtCore.QRect(241, 345, 16, 17))
        self.echoBox.stateChanged.connect(self.updateTotal)

    def loadLevelsFromDb(self, data):
        passiveLevels = data.get("passive")
        activeLevels = data.get("active")
        jettValues = data.get("jett")
        beginnerLevels = data.get("beginner")
        for i in range(0, len(self.passive)):
            self.passiveSpin[i].setProperty("value", passiveLevels[i])
        for i in range(0, len(self.active)):
            self.activeBox[i].setChecked(activeLevels[i].get("enabled"))
            self.activeSpin[i].setProperty("value", activeLevels[i].get("level"))
        self.strSpin.setProperty("value", jettValues.get("STR"))
        self.dexSpin.setProperty("value", jettValues.get("DEX"))
        self.intSpin.setProperty("value", jettValues.get("INT"))
        self.lukSpin.setProperty("value", jettValues.get("LUK"))
        self.atkSpin.setProperty("value", jettValues.get("ATK"))
        self.matkSpin.setProperty("value", jettValues.get("MATK"))
        self.jettBox.setChecked(jettValues.get("enabled"))
        self.fairySpin.setProperty("value", beginnerLevels.get("fairy"))
        self.empSpin.setProperty("value", beginnerLevels.get("empress"))

    def getJsonForDb(self):
        passive = []
        for value in self.passiveSpin:
            passive.append(value.value())
        active = []
        for i in range(0, len(self.active)):
            obj = {
                "level": self.activeSpin[i].value(),
                "enabled": self.activeBox[i].isChecked()
            }
            active.append(obj)
        jett = self.getJett()
        jett.update({"enabled": self.jettBox.isChecked()})
        beginner = {
            "fairy": self.fairySpin.value(),
            "empress": self.empSpin.value()
        }
        return {
            "passive": passive,
            "active": active,
            "jett": jett,
            "beginner": beginner
        }


    def updateTotal(self):
        self.total.clear()
        linksApplied = 0
        for i in range(0, len(self.passive)):
            if(self.passiveSpin[i].value() != 0):
                self.total = addDicts(self.total, self.passive[i].getStats())
                linksApplied += 1
        for i in range(0, len(self.active)):
            if(self.activeBox[i].isChecked() and self.activeSpin[i].value() == 0):
                self.activeSpin[i].setProperty("value", 1)
            if(self.activeBox[i].isChecked() and self.activeSpin[i].value() != 0):
                self.total = addDicts(self.total, self.active[i].getStats())
                linksApplied += 1
        if(self.jettBox.isChecked()):
            # jett = {
            #     "STR": self.strSpin.value(),
            #     "DEX": self.dexSpin.value(),
            #     "INT": self.intSpin.value(),
            #     "LUK": self.lukSpin.value(),
            #     "ATK": self.atkSpin.value(),
            #     "MATK": self.matkSpin.value()
            # }
            self.total = addDicts(self.total, self.getJett())
            linksApplied += 1
        if(self.echoBox.isChecked()):
            self.total = addDicts(self.total, self.echo.getStats())
        if(self.fairySpin.value() > 0):
            self.blessingOfFairy.updateDecentLevel(self.fairySpin.value())
            self.total = addDicts(self.total, self.blessingOfFairy.getStats())
        if(self.empSpin.value() > 0):
            self.blessingOfEmpress.updateDecentLevel(self.empSpin.value())
            self.total = addDicts(self.total, self.blessingOfEmpress.getStats())
        activeString = "Active Links: " + str(linksApplied)
        self.activeLinks.setText(activeString)
        self.notifyParent()

    def getJett(self):
        return {
                "STR": self.strSpin.value(),
                "DEX": self.dexSpin.value(),
                "INT": self.intSpin.value(),
                "LUK": self.lukSpin.value(),
                "ATK": self.atkSpin.value(),
                "MATK": self.matkSpin.value()
            }

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

