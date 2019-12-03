# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'legion.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class legionController(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.grid = []
        self.characters = {
            "STR": [],
            "DEX": [],
            "INT": [],
            "LUK": [],
            "HP": [],
            "MP": [],
            "CRITRATE": [],
            "CRITDMG": [],
            "BOSS": [],
            "XENON": [],
            "LABSTANDARD": [],
            "LABENHANCED": []
        }
        self.setupUi()

    def setupUi(self):
        self.resize(621, 380)
        labelStyle = "border-radius: 10px; border: 2px solid black; qproperty-alignment: AlignCenter;background-color: rgb(79, 238, 238); font-size: 12px;"
        
        self.passiveLabel = QtWidgets.QLabel(self)
        self.passiveLabel.setGeometry(QtCore.QRect(10, 0, 81, 21))
        self.passiveLabel.setStyleSheet("font-size: 14px;")
        self.passiveLabel.setObjectName("passiveLabel")
        self.passiveLabel.setText("Legion Grid")

        #Legion Grid
        self.strLabel = QtWidgets.QLabel(self)
        self.strLabel.setGeometry(QtCore.QRect(20, 20, 81, 22))
        self.strLabel.setStyleSheet(labelStyle)
        self.strLabel.setObjectName("strLabel")
        self.strLabel.setText("STR")
        self.strSpinbox = QtWidgets.QSpinBox(self)
        self.strSpinbox.setGeometry(QtCore.QRect(110, 20, 42, 22))
        self.strSpinbox.setMaximum(15)
        self.strSpinbox.setObjectName("strSpinbox")

        self.dexLabel = QtWidgets.QLabel(self)
        self.dexLabel.setGeometry(QtCore.QRect(20, 40, 81, 22))
        self.dexLabel.setStyleSheet(labelStyle)
        self.dexLabel.setObjectName("dexLabel")
        self.dexLabel.setText("DEX")
        self.dexSpinbox = QtWidgets.QSpinBox(self)
        self.dexSpinbox.setGeometry(QtCore.QRect(110, 40, 42, 22))
        self.dexSpinbox.setMaximum(15)
        self.dexSpinbox.setObjectName("dexSpinbox")

        self.intLabel = QtWidgets.QLabel(self)
        self.intLabel.setGeometry(QtCore.QRect(20, 60, 81, 22))
        self.intLabel.setStyleSheet(labelStyle)
        self.intLabel.setObjectName("intLabel")
        self.intLabel.setText("INT")
        self.intSpinbox = QtWidgets.QSpinBox(self)
        self.intSpinbox.setGeometry(QtCore.QRect(110, 60, 42, 22))
        self.intSpinbox.setMaximum(15)
        self.intSpinbox.setObjectName("intSpinbox")

        self.lukLabel = QtWidgets.QLabel(self)
        self.lukLabel.setGeometry(QtCore.QRect(20, 80, 81, 22))
        self.lukLabel.setStyleSheet(labelStyle)
        self.lukLabel.setObjectName("lukLabel")
        self.lukLabel.setText("LUK")
        self.lukSpinbox = QtWidgets.QSpinBox(self)
        self.lukSpinbox.setGeometry(QtCore.QRect(110, 80, 42, 22))
        self.lukSpinbox.setMaximum(15)
        self.lukSpinbox.setObjectName("lukSpinbox")

        self.atkLabel = QtWidgets.QLabel(self)
        self.atkLabel.setGeometry(QtCore.QRect(20, 100, 81, 22))
        self.atkLabel.setStyleSheet(labelStyle)
        self.atkLabel.setObjectName("atkLabel")
        self.atkLabel.setText("ATK")
        self.atkSpinbox = QtWidgets.QSpinBox(self)
        self.atkSpinbox.setGeometry(QtCore.QRect(110, 100, 42, 22))
        self.atkSpinbox.setMaximum(15)
        self.atkSpinbox.setObjectName("atkSpinbox")

        self.matkLabel = QtWidgets.QLabel(self)
        self.matkLabel.setGeometry(QtCore.QRect(20, 120, 81, 22))
        self.matkLabel.setStyleSheet(labelStyle)
        self.matkLabel.setObjectName("matkLabel")
        self.matkLabel.setText("M. ATK")
        self.matkSpinbox = QtWidgets.QSpinBox(self)
        self.matkSpinbox.setGeometry(QtCore.QRect(110, 120, 42, 22))
        self.matkSpinbox.setMaximum(15)
        self.matkSpinbox.setObjectName("matkSpinbox")
        
        self.hpLabel = QtWidgets.QLabel(self)
        self.hpLabel.setGeometry(QtCore.QRect(20, 140, 81, 21))
        self.hpLabel.setStyleSheet(labelStyle)
        self.hpLabel.setObjectName("hpLabel")
        self.hpLabel.setText("HP")
        self.hpSpinbox = QtWidgets.QSpinBox(self)
        self.hpSpinbox.setGeometry(QtCore.QRect(110, 140, 42, 22))
        self.hpSpinbox.setMaximum(15)
        self.hpSpinbox.setObjectName("hpSpinbox")

        self.mpLabel = QtWidgets.QLabel(self)
        self.mpLabel.setGeometry(QtCore.QRect(20, 160, 81, 22))
        self.mpLabel.setStyleSheet(labelStyle)
        self.mpLabel.setObjectName("mpLabel")
        self.mpLabel.setText("MP")
        self.mpSpinbox = QtWidgets.QSpinBox(self)
        self.mpSpinbox.setGeometry(QtCore.QRect(110, 160, 42, 22))
        self.mpSpinbox.setMaximum(15)
        self.mpSpinbox.setObjectName("mpSpinbox")

        self.critrateLabel = QtWidgets.QLabel(self)
        self.critrateLabel.setGeometry(QtCore.QRect(20, 180, 81, 22))
        self.critrateLabel.setStyleSheet(labelStyle)
        self.critrateLabel.setObjectName("critrateLabel")
        self.critrateLabel.setText("CRIT RATE")
        self.critrateSpinbox = QtWidgets.QSpinBox(self)
        self.critrateSpinbox.setGeometry(QtCore.QRect(110, 180, 42, 22))
        self.critrateSpinbox.setMaximum(40)
        self.critrateSpinbox.setObjectName("critrateSpinbox")

        self.critdmgLabel = QtWidgets.QLabel(self)
        self.critdmgLabel.setGeometry(QtCore.QRect(20, 200, 81, 22))
        self.critdmgLabel.setStyleSheet(labelStyle)
        self.critdmgLabel.setObjectName("critdmgLabel")
        self.critdmgLabel.setText("CRIT DMG")
        self.critdmgSpinbox = QtWidgets.QSpinBox(self)
        self.critdmgSpinbox.setGeometry(QtCore.QRect(110, 200, 42, 22))
        self.critdmgSpinbox.setMaximum(40)
        self.critdmgSpinbox.setObjectName("critdmgSpinbox")

        self.ignoreLabel = QtWidgets.QLabel(self)
        self.ignoreLabel.setGeometry(QtCore.QRect(20, 220, 81, 22))
        self.ignoreLabel.setStyleSheet(labelStyle)
        self.ignoreLabel.setObjectName("ignoreLabel")
        self.ignoreLabel.setText("IGNORE")
        self.ignoreSpinbox = QtWidgets.QSpinBox(self)
        self.ignoreSpinbox.setGeometry(QtCore.QRect(110, 220, 42, 22))
        self.ignoreSpinbox.setMaximum(40)
        self.ignoreSpinbox.setObjectName("ignoreSpinbox")
        
        self.bossLabel = QtWidgets.QLabel(self)
        self.bossLabel.setGeometry(QtCore.QRect(20, 240, 81, 22))
        self.bossLabel.setStyleSheet(labelStyle)
        self.bossLabel.setObjectName("bossLabel")
        self.bossLabel.setText("BOSS")
        self.bossSpinbox = QtWidgets.QSpinBox(self)
        self.bossSpinbox.setGeometry(QtCore.QRect(110, 240, 42, 22))
        self.bossSpinbox.setMaximum(40)
        self.bossSpinbox.setObjectName("bossSpinbox")

        #Character Bonuses
        self.passiveLabel_2 = QtWidgets.QLabel(self)
        self.passiveLabel_2.setGeometry(QtCore.QRect(160, 0, 141, 21))
        self.passiveLabel_2.setStyleSheet("font-size: 14px;")
        self.passiveLabel_2.setObjectName("passiveLabel_2")
        self.passiveLabel_2.setText("Character Bonuses")

        labelStyle = "font-size: 14px;qproperty-alignment: AlignRight;"
        
        self.strCharLabel = QtWidgets.QLabel(self)
        self.strCharLabel.setGeometry(QtCore.QRect(176, 30, 61, 22))
        self.strCharLabel.setStyleSheet(labelStyle)
        self.strCharLabel.setText("STR:")
        
        #7 available STR characters
        self.populateComboBoxes("STR", 7, 28)

        self.dexCharLabel = QtWidgets.QLabel(self)
        self.dexCharLabel.setGeometry(QtCore.QRect(176, 60, 61, 22))
        self.dexCharLabel.setStyleSheet(labelStyle)
        self.dexCharLabel.setText("DEX:")

        #3 available DEX characters
        self.populateComboBoxes("DEX", 3, 58)

        self.intCharLabel = QtWidgets.QLabel(self)
        self.intCharLabel.setGeometry(QtCore.QRect(176, 90, 61, 22))
        self.intCharLabel.setStyleSheet(labelStyle)
        self.intCharLabel.setText("INT:")

        #7 available INT characters
        self.populateComboBoxes("INT", 7, 88)

        self.lukCharLabel = QtWidgets.QLabel(self)
        self.lukCharLabel.setGeometry(QtCore.QRect(176, 120, 61, 22))
        self.lukCharLabel.setStyleSheet(labelStyle)
        self.lukCharLabel.setText("LUK:")

        #5 available LUK characters
        self.populateComboBoxes("LUK", 5, 118)

        self.hpCharLabel = QtWidgets.QLabel(self)
        self.hpCharLabel.setGeometry(QtCore.QRect(176, 150, 61, 22))
        self.hpCharLabel.setStyleSheet(labelStyle)
        self.hpCharLabel.setText("HP:")

        #3 available HP characters
        self.populateComboBoxes("HP", 3, 148)

        self.mpCharLabel = QtWidgets.QLabel(self)
        self.mpCharLabel.setGeometry(QtCore.QRect(176, 180, 61, 22))
        self.mpCharLabel.setStyleSheet(labelStyle)
        self.mpCharLabel.setText("MP:")

        #1 available MP character
        self.populateComboBoxes("MP", 1, 178)

        self.critrateCharLabel = QtWidgets.QLabel(self)
        self.critrateCharLabel.setGeometry(QtCore.QRect(176, 210, 61, 22))
        self.critrateCharLabel.setStyleSheet(labelStyle)
        self.critrateCharLabel.setText("C. RATE:")

        #2 available crit rate characters
        self.populateComboBoxes("CRITRATE", 2, 208)

        self.critdmgCharLabel = QtWidgets.QLabel(self)
        self.critdmgCharLabel.setGeometry(QtCore.QRect(176, 240, 61, 22))
        self.critdmgCharLabel.setStyleSheet(labelStyle)
        self.critdmgCharLabel.setText("C. DMG:")

        #3 available crit dmg characters
        self.populateComboBoxes("CRITDMG", 3, 238)

        self.bossCharLabel = QtWidgets.QLabel(self)
        self.bossCharLabel.setGeometry(QtCore.QRect(176, 270, 61, 22))
        self.bossCharLabel.setStyleSheet(labelStyle)
        self.bossCharLabel.setText("BOSS:")

        #2 available boss characters
        self.populateComboBoxes("BOSS", 2, 268)

        self.xenonLabel = QtWidgets.QLabel(self)
        self.xenonLabel.setGeometry(QtCore.QRect(176, 300, 61, 22))
        self.xenonLabel.setStyleSheet(labelStyle)
        self.xenonLabel.setText("XENON:")

        #1 xenon 😂
        self.populateComboBoxes("XENON", 1, 298)
    
        self.lab1Label = QtWidgets.QLabel(self)
        self.lab1Label.setGeometry(QtCore.QRect(291, 300, 91, 22))
        self.lab1Label.setStyleSheet(labelStyle)
        self.lab1Label.setText("LAB Standard:")

        #1 lab standard, can't use method due to placement
        box = QtWidgets.QComboBox(self)
        box.setGeometry(QtCore.QRect(385, 298, 42, 22))
        box.addItem("250")
        box.addItem("200")
        box.addItem("140")
        box.addItem("100")
        box.addItem("60")
        box.addItem("0")
        box.setCurrentIndex(5)
        self.characters.get("LABSTANDARD").append(box)

        self.lab2Label = QtWidgets.QLabel(self)
        self.lab2Label.setGeometry(QtCore.QRect(430, 300, 101, 22))
        self.lab2Label.setStyleSheet(labelStyle)
        self.lab2Label.setText("LAB Enhanced:")

        #1 lab enhanced, can't use method due to placement
        box = QtWidgets.QComboBox(self)
        box.setGeometry(QtCore.QRect(534, 298, 42, 22))
        box.addItem("250")
        box.addItem("200")
        box.addItem("140")
        box.addItem("100")
        box.addItem("60")
        box.addItem("0")
        box.setCurrentIndex(5)
        self.characters.get("LABENHANCED").append(box)

        self.clear = QtWidgets.QPushButton(self)
        self.clear.setGeometry(QtCore.QRect(280, 330, 101, 31))
        self.clear.setText("CLEAR ALL")
        self.clear.clicked.connect(self.clearCombos)
        

        self.all140 = QtWidgets.QPushButton(self)
        self.all140.setGeometry(QtCore.QRect(390, 330, 101, 31))
        self.all140.setText("SET ALL TO 140")
        self.all140.clicked.connect(self.combosTo140)

        self.all200 = QtWidgets.QPushButton(self)
        self.all200.setGeometry(QtCore.QRect(500, 330, 101, 31))
        self.all200.setText("SET ALL TO 200")
        self.all200.clicked.connect(self.combosTo200)

    def clearCombos(self):
        for key in self.characters:
            arr = self.characters.get(key)
            for box in arr:
                box.setCurrentIndex(5)

    def combosTo140(self):
        for key in self.characters:
            arr = self.characters.get(key)
            for box in arr:
                box.setCurrentIndex(2)

    def combosTo200(self):
        for key in self.characters:
            arr = self.characters.get(key)
            for box in arr:
                box.setCurrentIndex(1)

    def populateComboBoxes(self, statName, amount, yCoord):
        for i in range(0, amount):
            combo = QtWidgets.QComboBox(self)
            combo.setGeometry(QtCore.QRect(240 + (50 * i), yCoord, 42, 22))
            combo.addItem("250")
            combo.addItem("200")
            combo.addItem("140")
            combo.addItem("100")
            combo.addItem("60")
            combo.addItem("0")
            combo.setCurrentIndex(5)
            self.characters.get(statName).append(combo)
