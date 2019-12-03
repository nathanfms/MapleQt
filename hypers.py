# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hypers.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class hyperController(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        labelStyle = "border-radius: 10px; border: 2px solid black; qproperty-alignment: AlignCenter; background-color: rgb(79, 238, 238); font-size: 12px;"
        self.resize(140, 265)

        statFile = open('jobs/Hypers.json')

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
        self.strSpinbox.setObjectName("strSpinbox")

        self.dexLabel = QtWidgets.QLabel(self)
        self.dexLabel.setGeometry(QtCore.QRect(0, 40, 81, 22))
        self.dexLabel.setStyleSheet(labelStyle)
        self.dexLabel.setObjectName("dexLabel")
        self.dexLabel.setText("DEX")
        self.dexSpinbox = QtWidgets.QSpinBox(self)
        self.dexSpinbox.setGeometry(QtCore.QRect(90, 40, 42, 22))
        self.dexSpinbox.setMaximum(15)
        self.dexSpinbox.setObjectName("dexSpinbox")
        
        self.intLabel = QtWidgets.QLabel(self)
        self.intLabel.setGeometry(QtCore.QRect(0, 60, 81, 22))
        self.intLabel.setStyleSheet(labelStyle)
        self.intLabel.setObjectName("intLabel")
        self.intLabel.setText("INT")
        self.intSpinbox = QtWidgets.QSpinBox(self)
        self.intSpinbox.setGeometry(QtCore.QRect(90, 60, 42, 22))
        self.intSpinbox.setMaximum(15)
        self.intSpinbox.setObjectName("intSpinbox")

        self.lukLabel = QtWidgets.QLabel(self)
        self.lukLabel.setGeometry(QtCore.QRect(0, 80, 81, 22))
        self.lukLabel.setStyleSheet(labelStyle)
        self.lukLabel.setObjectName("lukLabel")
        self.lukLabel.setText("LUK")
        self.lukSpinbox = QtWidgets.QSpinBox(self)
        self.lukSpinbox.setGeometry(QtCore.QRect(90, 80, 42, 22))
        self.lukSpinbox.setMaximum(15)
        self.lukSpinbox.setObjectName("lukSpinbox")

        self.hpLabel = QtWidgets.QLabel(self)
        self.hpLabel.setGeometry(QtCore.QRect(0, 100, 81, 21))
        self.hpLabel.setStyleSheet(labelStyle)
        self.hpLabel.setObjectName("hpLabel")
        self.hpLabel.setText("HP")
        self.hpSpinbox = QtWidgets.QSpinBox(self)
        self.hpSpinbox.setGeometry(QtCore.QRect(90, 100, 42, 22))
        self.hpSpinbox.setMaximum(15)
        self.hpSpinbox.setObjectName("hpSpinbox")

        self.mpLabel = QtWidgets.QLabel(self)
        self.mpLabel.setGeometry(QtCore.QRect(0, 120, 81, 22))
        self.mpLabel.setStyleSheet(labelStyle)
        self.mpLabel.setObjectName("mpLabel")
        self.mpLabel.setText("MP")
        self.mpSpinbox = QtWidgets.QSpinBox(self)
        self.mpSpinbox.setGeometry(QtCore.QRect(90, 120, 42, 22))
        self.mpSpinbox.setMaximum(15)
        self.mpSpinbox.setObjectName("mpSpinbox")

        self.critrateLabel = QtWidgets.QLabel(self)
        self.critrateLabel.setGeometry(QtCore.QRect(0, 140, 81, 22))
        self.critrateLabel.setStyleSheet(labelStyle)
        self.critrateLabel.setObjectName("critrateLabel")
        self.critrateLabel.setText("CRIT RATE")
        self.critrateSpinbox = QtWidgets.QSpinBox(self)
        self.critrateSpinbox.setGeometry(QtCore.QRect(90, 140, 42, 22))
        self.critrateSpinbox.setMaximum(15)
        self.critrateSpinbox.setObjectName("critrateSpinbox")   
        
        self.critdmgLabel = QtWidgets.QLabel(self)
        self.critdmgLabel.setGeometry(QtCore.QRect(0, 160, 81, 22))
        self.critdmgLabel.setStyleSheet(labelStyle)
        self.critdmgLabel.setObjectName("critdmgLabel")
        self.critdmgLabel.setText("CRIT DMG")
        self.critdmgSpinbox = QtWidgets.QSpinBox(self)
        self.critdmgSpinbox.setGeometry(QtCore.QRect(90, 160, 42, 22))
        self.critdmgSpinbox.setMaximum(15)
        self.critdmgSpinbox.setObjectName("critdmgSpinbox")
        
        self.ignoreLabel = QtWidgets.QLabel(self)
        self.ignoreLabel.setGeometry(QtCore.QRect(0, 180, 81, 22))
        self.ignoreLabel.setStyleSheet(labelStyle)
        self.ignoreLabel.setObjectName("ignoreLabel")
        self.ignoreLabel.setText("IGNORE")
        self.ignoreSpinbox = QtWidgets.QSpinBox(self)
        self.ignoreSpinbox.setGeometry(QtCore.QRect(90, 180, 42, 22))
        self.ignoreSpinbox.setMaximum(15)
        self.ignoreSpinbox.setObjectName("ignoreSpinbox")

        self.bossLabel = QtWidgets.QLabel(self)
        self.bossLabel.setGeometry(QtCore.QRect(0, 200, 81, 22))
        self.bossLabel.setStyleSheet(labelStyle)
        self.bossLabel.setObjectName("bossLabel")
        self.bossLabel.setText("BOSS")
        self.bossSpinbox = QtWidgets.QSpinBox(self)
        self.bossSpinbox.setGeometry(QtCore.QRect(90, 200, 42, 22))
        self.bossSpinbox.setMaximum(15)
        self.bossSpinbox.setObjectName("bossSpinbox")

        self.dmgLabel = QtWidgets.QLabel(self)
        self.dmgLabel.setGeometry(QtCore.QRect(0, 220, 81, 22))
        self.dmgLabel.setStyleSheet(labelStyle)
        self.dmgLabel.setObjectName("dmgLabel")
        self.dmgLabel.setText("DMG")
        self.dmgSpinbox = QtWidgets.QSpinBox(self)
        self.dmgSpinbox.setGeometry(QtCore.QRect(90, 220, 42, 22))
        self.dmgSpinbox.setMaximum(15)
        self.dmgSpinbox.setObjectName("dmgSpinbox")

        self.atkLabel = QtWidgets.QLabel(self)
        self.atkLabel.setGeometry(QtCore.QRect(0, 240, 81, 22))
        self.atkLabel.setStyleSheet(labelStyle)
        self.atkLabel.setObjectName("atkLabel")
        self.atkLabel.setText("M/ATK")
        self.atkSpinbox = QtWidgets.QSpinBox(self)
        self.atkSpinbox.setGeometry(QtCore.QRect(90, 240, 42, 22))
        self.atkSpinbox.setMaximum(15)
        self.atkSpinbox.setObjectName("atkSpinbox")
       
