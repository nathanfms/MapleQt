# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hypers.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import json


class hyperController(QtWidgets.QWidget):
    def __init__(self, parent=None, valuesChanged=None):
        super().__init__(parent)
        self.total = {}
        self.notifyParent = valuesChanged
        self.setupUi()

    def setupUi(self):
        labelStyle = "border-radius: 10px; border: 2px solid black; qproperty-alignment: AlignCenter; background-color: rgb(79, 238, 238); font-size: 12px;"
        self.resize(140, 265)

        statFile = open('jobs/Hypers.json')
        self.statJson = json.load(statFile)

        self.titleLabel = QtWidgets.QLabel(self)
        self.titleLabel.setGeometry(QtCore.QRect(0, 0, 141, 20))
        self.titleLabel.setStyleSheet("font-size: 14px;qproperty-alignment: AlignCenter;")
        self.titleLabel.setObjectName("titleLabel")
        self.titleLabel.setText("Hyper Stats")

        self.strLabel = QtWidgets.QLabel(self)
        self.strLabel.setGeometry(QtCore.QRect(0, 20, 81, 22))
        self.strLabel.setStyleSheet(labelStyle)
        self.strLabel.setObjectName("strLabel")
        self.strLabel.setText("STR")
        self.strSpinbox = QtWidgets.QSpinBox(self)
        self.strSpinbox.setGeometry(QtCore.QRect(90, 20, 42, 22))
        self.strSpinbox.setMaximum(15)
        self.strSpinbox.setObjectName("STR")
        self.strSpinbox.valueChanged.connect(self.updateTotal)

        self.dexLabel = QtWidgets.QLabel(self)
        self.dexLabel.setGeometry(QtCore.QRect(0, 40, 81, 22))
        self.dexLabel.setStyleSheet(labelStyle)
        self.dexLabel.setObjectName("dexLabel")
        self.dexLabel.setText("DEX")
        self.dexSpinbox = QtWidgets.QSpinBox(self)
        self.dexSpinbox.setGeometry(QtCore.QRect(90, 40, 42, 22))
        self.dexSpinbox.setMaximum(15)
        self.dexSpinbox.setObjectName("DEX")
        self.dexSpinbox.valueChanged.connect(self.updateTotal)
        
        self.intLabel = QtWidgets.QLabel(self)
        self.intLabel.setGeometry(QtCore.QRect(0, 60, 81, 22))
        self.intLabel.setStyleSheet(labelStyle)
        self.intLabel.setObjectName("intLabel")
        self.intLabel.setText("INT")
        self.intSpinbox = QtWidgets.QSpinBox(self)
        self.intSpinbox.setGeometry(QtCore.QRect(90, 60, 42, 22))
        self.intSpinbox.setMaximum(15)
        self.intSpinbox.setObjectName("INT")
        self.intSpinbox.valueChanged.connect(self.updateTotal)

        self.lukLabel = QtWidgets.QLabel(self)
        self.lukLabel.setGeometry(QtCore.QRect(0, 80, 81, 22))
        self.lukLabel.setStyleSheet(labelStyle)
        self.lukLabel.setObjectName("lukLabel")
        self.lukLabel.setText("LUK")
        self.lukSpinbox = QtWidgets.QSpinBox(self)
        self.lukSpinbox.setGeometry(QtCore.QRect(90, 80, 42, 22))
        self.lukSpinbox.setMaximum(15)
        self.lukSpinbox.setObjectName("LUK")
        self.lukSpinbox.valueChanged.connect(self.updateTotal)

        self.hpLabel = QtWidgets.QLabel(self)
        self.hpLabel.setGeometry(QtCore.QRect(0, 100, 81, 21))
        self.hpLabel.setStyleSheet(labelStyle)
        self.hpLabel.setObjectName("hpLabel")
        self.hpLabel.setText("HP")
        self.hpSpinbox = QtWidgets.QSpinBox(self)
        self.hpSpinbox.setGeometry(QtCore.QRect(90, 100, 42, 22))
        self.hpSpinbox.setMaximum(15)
        self.hpSpinbox.setObjectName("HPp")
        self.hpSpinbox.valueChanged.connect(self.updateTotal)

        self.mpLabel = QtWidgets.QLabel(self)
        self.mpLabel.setGeometry(QtCore.QRect(0, 120, 81, 22))
        self.mpLabel.setStyleSheet(labelStyle)
        self.mpLabel.setObjectName("mpLabel")
        self.mpLabel.setText("MP")
        self.mpSpinbox = QtWidgets.QSpinBox(self)
        self.mpSpinbox.setGeometry(QtCore.QRect(90, 120, 42, 22))
        self.mpSpinbox.setMaximum(15)
        self.mpSpinbox.setObjectName("MPp")
        self.mpSpinbox.valueChanged.connect(self.updateTotal)

        self.critrateLabel = QtWidgets.QLabel(self)
        self.critrateLabel.setGeometry(QtCore.QRect(0, 140, 81, 22))
        self.critrateLabel.setStyleSheet(labelStyle)
        self.critrateLabel.setObjectName("critrateLabel")
        self.critrateLabel.setText("CRIT RATE")
        self.critrateSpinbox = QtWidgets.QSpinBox(self)
        self.critrateSpinbox.setGeometry(QtCore.QRect(90, 140, 42, 22))
        self.critrateSpinbox.setMaximum(15)
        self.critrateSpinbox.setObjectName("CRITRATEp")
        self.critrateSpinbox.valueChanged.connect(self.updateTotal) 
        
        self.critdmgLabel = QtWidgets.QLabel(self)
        self.critdmgLabel.setGeometry(QtCore.QRect(0, 160, 81, 22))
        self.critdmgLabel.setStyleSheet(labelStyle)
        self.critdmgLabel.setObjectName("critdmgLabel")
        self.critdmgLabel.setText("CRIT DMG")
        self.critdmgSpinbox = QtWidgets.QSpinBox(self)
        self.critdmgSpinbox.setGeometry(QtCore.QRect(90, 160, 42, 22))
        self.critdmgSpinbox.setMaximum(15)
        self.critdmgSpinbox.setObjectName("CRITDMGp")
        self.critdmgSpinbox.valueChanged.connect(self.updateTotal)
        
        self.ignoreLabel = QtWidgets.QLabel(self)
        self.ignoreLabel.setGeometry(QtCore.QRect(0, 180, 81, 22))
        self.ignoreLabel.setStyleSheet(labelStyle)
        self.ignoreLabel.setObjectName("ignoreLabel")
        self.ignoreLabel.setText("IGNORE")
        self.ignoreSpinbox = QtWidgets.QSpinBox(self)
        self.ignoreSpinbox.setGeometry(QtCore.QRect(90, 180, 42, 22))
        self.ignoreSpinbox.setMaximum(15)
        self.ignoreSpinbox.setObjectName("IGNORE")
        self.ignoreSpinbox.valueChanged.connect(self.updateTotal)

        self.bossLabel = QtWidgets.QLabel(self)
        self.bossLabel.setGeometry(QtCore.QRect(0, 200, 81, 22))
        self.bossLabel.setStyleSheet(labelStyle)
        self.bossLabel.setObjectName("bossLabel")
        self.bossLabel.setText("BOSS")
        self.bossSpinbox = QtWidgets.QSpinBox(self)
        self.bossSpinbox.setGeometry(QtCore.QRect(90, 200, 42, 22))
        self.bossSpinbox.setMaximum(15)
        self.bossSpinbox.setObjectName("BOSSp")
        self.bossSpinbox.valueChanged.connect(self.updateTotal)

        self.dmgLabel = QtWidgets.QLabel(self)
        self.dmgLabel.setGeometry(QtCore.QRect(0, 220, 81, 22))
        self.dmgLabel.setStyleSheet(labelStyle)
        self.dmgLabel.setObjectName("dmgLabel")
        self.dmgLabel.setText("DMG")
        self.dmgSpinbox = QtWidgets.QSpinBox(self)
        self.dmgSpinbox.setGeometry(QtCore.QRect(90, 220, 42, 22))
        self.dmgSpinbox.setMaximum(15)
        self.dmgSpinbox.setObjectName("DMGp")
        self.dmgSpinbox.valueChanged.connect(self.updateTotal)

        self.atkLabel = QtWidgets.QLabel(self)
        self.atkLabel.setGeometry(QtCore.QRect(0, 240, 81, 22))
        self.atkLabel.setStyleSheet(labelStyle)
        self.atkLabel.setObjectName("atkLabel")
        self.atkLabel.setText("M/ATK")
        self.atkSpinbox = QtWidgets.QSpinBox(self)
        self.atkSpinbox.setGeometry(QtCore.QRect(90, 240, 42, 22))
        self.atkSpinbox.setMaximum(15)
        self.atkSpinbox.setObjectName("ATK")
        self.atkSpinbox.valueChanged.connect(self.updateTotal)

    def loadLevelsFromDb(self, data):
        self.strSpinbox.setProperty("value", data[0])
        self.dexSpinbox.setProperty("value", data[1])
        self.intSpinbox.setProperty("value", data[2])
        self.lukSpinbox.setProperty("value", data[3])
        self.hpSpinbox.setProperty("value", data[4])
        self.mpSpinbox.setProperty("value", data[5])
        self.critrateSpinbox.setProperty("value", data[6])
        self.critdmgSpinbox.setProperty("value", data[7])
        self.ignoreSpinbox.setProperty("value", data[8])
        self.bossSpinbox.setProperty("value", data[9])
        self.dmgSpinbox.setProperty("value", data[10])
        self.atkSpinbox.setProperty("value", data[11])
        self.updateTotal()

    def getJsonForDb(self):
        return [
            self.strSpinbox.value(),
            self.dexSpinbox.value(),
            self.intSpinbox.value(),
            self.lukSpinbox.value(),
            self.hpSpinbox.value(),
            self.mpSpinbox.value(),
            self.critrateSpinbox.value(),
            self.critdmgSpinbox.value(),
            self.ignoreSpinbox.value(),
            self.bossSpinbox.value(),
            self.dmgSpinbox.value(),
            self.atkSpinbox.value()
        ]
       
    def updateTotal(self):
        self.total.clear()
        for stat in self.statJson:
            statName = stat.get("stat")
            child = self.findChild(QtWidgets.QSpinBox, statName)
            base = stat.get("base")
            if(base is not None and child.value() > 0):
                step = stat.get("step")
                self.total.update({statName : base + ((child.value() - 1) * step)})
            elif(child.value() > 0):
                value = stat.get("stats")[child.value() - 1]
                for key in value:  
                    self.total.update({key : value.get(key)})
        self.notifyParent()