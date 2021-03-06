# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'skillTip.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt5 import QtCore, QtGui, QtWidgets

def format(text):
    if(text.endswith("p")):
        return text[0:-1]
    elif(text.endswith("lvl")):
        return text[0:-3] + " / lvl"
    return text

class skillInfo(QtWidgets.QWidget):
    def __init__(self, json=None, parent=None):
        super().__init__(parent)
        self.json = json
        self.currentStats = {}
        self.setupUi()

    def setupUi(self):
        self.setWindowFlags(
            QtCore.Qt.CustomizeWindowHint |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.ToolTip
        )

        height = 115
        if(len(self.json.get("stats")[0]) > 3):
            height += (len(self.json.get("stats")[0]) - 3) * 22
            if(self.json.get("stats")[0].get("passive") is not None):
                height -= 22

        self.setObjectName("Skill")
        self.resize(259, height)
        self.setStyleSheet("background-color: rgb(79, 79, 79);")

        self.skillName = QtWidgets.QLabel(self)
        self.skillName.setGeometry(QtCore.QRect(0, 10, 301, 21))
        self.skillName.setStyleSheet("color: rgb(255, 0, 255); font-size: 16px; padding-left: 7px;")
        self.skillName.setObjectName("skillName")
        self.skillName.setText(self.json.get("name"))
        self.skillImg = QtWidgets.QLabel(self)
        self.skillImg.setGeometry(QtCore.QRect(20, 40, 64, 64))
        pix = QtGui.QPixmap(os.path.join("assets/skills", self.json.get("img")))
        pixScale = pix.scaledToWidth(64)
        self.skillImg.setPixmap(pixScale)
        self.skillImg.setObjectName("skillImg")
        self.attributes = QtWidgets.QListWidget(self)
        self.attributes.setGeometry(QtCore.QRect(90, 40, 91, 22 * len(self.json.get("stats")[0]) + 5))
        self.attributes.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.attributes.setStyleSheet("color: rgb(227, 227, 227); font-size: 14px;")
        self.attributes.setFlow(QtWidgets.QListView.TopToBottom)
        self.attributes.setProperty("isWrapping", False)
        self.attributes.setResizeMode(QtWidgets.QListView.Fixed)
        self.attributes.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.attributes.setItemAlignment(QtCore.Qt.AlignAbsolute|QtCore.Qt.AlignHCenter|QtCore.Qt.AlignJustify|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.attributes.setObjectName("attributes")

        self.totalList = QtWidgets.QListWidget(self)
        self.totalList.setGeometry(QtCore.QRect(180, 40, 71, 22 * len(self.json.get("stats")[0]) + 5))
        self.totalList.setStyleSheet("color: rgb(0, 231, 231); font-size: 14px;")
        self.totalList.setObjectName("totalList")

        # for i in range(0, len(self.json.get("stats")[0])):
        #     item = QtWidgets.QListWidgetItem()
        #     item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        #     self.attributes.add(item)

        self.setLevel(0)

    def setDecentLevel(self, level):
        if(level != 0):
            level = level - 1
        self.setLevel(level)

    def setLevel(self, level):
        self.attributes.clear()
        self.totalList.clear()
        self.currentStats.clear()
        if(self.json.get("fifth") and level != 0):
            level = level - 1
        elif(level >= len(self.json.get("stats"))):
            level = 0
        for key in self.json.get("stats")[level]:
            if(key != "passive"):
                amount = self.json.get("stats")[level].get(key)
                self.addStat(key, amount)
        # passive = self.json.get("stats")[level].get("passive")
        # if(passive is not None):
        #     for key in passive:
        #         val = passive.get(key)
        #         self.addStat(key, val)

    def addStat(self, key, val):
        self.currentStats.update({key : val})
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignRight)
        item.setText(format(key))
        item.setSizeHint(QtCore.QSize(85, 21))
        self.attributes.addItem(item)
        itemVal = QtWidgets.QListWidgetItem()
        if(isinstance(val, float)): #percentage
            # val = int(val * 100)
            # val = str(val) + "%"
            val = '{:.0%}'.format(val) 
        val = "+" + str(val)
        itemVal.setText(val)
        itemVal.setSizeHint(QtCore.QSize(64, 21))
        self.totalList.addItem(itemVal)

