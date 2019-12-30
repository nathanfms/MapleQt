# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inventory.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from itemIcon import itemIcon
from DatabaseController import Database
import json

class inventoryController(QtWidgets.QWidget):
    def __init__(self, parent=None, onClick=None):
        super().__init__(parent)
        self.onClick = onClick
        self.filledSlots = []
        self.setupUi()

    def setupUi(self):
        # Form.setObjectName("Form")
        self.resize(215, 341)
        self.setMinimumSize(QtCore.QSize(215, 341))
        self.setMaximumSize(QtCore.QSize(215, 341))
        # self.inv1_1 = itemIcon(self)
        # self.inv1_1.setGeometry(QtCore.QRect(5, 5, 37, 37))
        # self.inv1_1.setStyleSheet("background-color: rgb(182, 182, 182);")
        # self.inv1_1.setText("")
        # self.inv1_1.setObjectName("inv1_1")

        self.inv1_1 = itemIcon(self)
        self.inv1_1.setGeometry(QtCore.QRect(5, 5, 37, 37))
        self.inv1_1.setObjectName("inv1_1")

        self.inv1_2 = itemIcon(self)
        self.inv1_2.setGeometry(QtCore.QRect(47, 5, 37, 37))
        self.inv1_2.setObjectName("inv1_2")

        self.inv1_3 = itemIcon(self)
        self.inv1_3.setGeometry(QtCore.QRect(89, 5, 37, 37))
        self.inv1_3.setObjectName("inv1_3")
        self.inv1_4 = itemIcon(self)
        self.inv1_4.setGeometry(QtCore.QRect(131, 5, 37, 37))
        self.inv1_4.setObjectName("inv1_4")
        self.inv1_5 = itemIcon(self)
        self.inv1_5.setGeometry(QtCore.QRect(173, 5, 37, 37))
        self.inv1_5.setObjectName("inv1_5")
        self.inv2_2 = itemIcon(self)
        self.inv2_2.setGeometry(QtCore.QRect(47, 47, 37, 37))
        self.inv2_2.setObjectName("inv2_2")
        self.inv2_5 = itemIcon(self)
        self.inv2_5.setGeometry(QtCore.QRect(173, 47, 37, 37))
        self.inv2_5.setObjectName("inv2_5")
        self.inv2_1 = itemIcon(self)
        self.inv2_1.setGeometry(QtCore.QRect(5, 47, 37, 37))
        self.inv2_1.setObjectName("inv2_1")
        self.inv2_3 = itemIcon(self)
        self.inv2_3.setGeometry(QtCore.QRect(89, 47, 37, 37))
        self.inv2_3.setObjectName("inv2_3")
        self.inv2_4 = itemIcon(self)
        self.inv2_4.setGeometry(QtCore.QRect(131, 47, 37, 37))
        self.inv2_4.setObjectName("inv2_4")
        self.inv3_2 = itemIcon(self)
        self.inv3_2.setGeometry(QtCore.QRect(47, 89, 37, 37))
        self.inv3_2.setObjectName("inv3_2")
        self.inv4_4 = itemIcon(self)
        self.inv4_4.setGeometry(QtCore.QRect(131, 131, 37, 37))
        self.inv4_4.setObjectName("inv4_4")
        self.inv4_1 = itemIcon(self)
        self.inv4_1.setGeometry(QtCore.QRect(5, 131, 37, 37))
        self.inv4_1.setObjectName("inv4_1")
        self.inv3_5 = itemIcon(self)
        self.inv3_5.setGeometry(QtCore.QRect(173, 89, 37, 37))
        self.inv3_5.setObjectName("inv3_5")
        self.inv3_1 = itemIcon(self)
        self.inv3_1.setGeometry(QtCore.QRect(5, 89, 37, 37))
        self.inv3_1.setObjectName("inv3_1")
        self.inv3_3 = itemIcon(self)
        self.inv3_3.setGeometry(QtCore.QRect(89, 89, 37, 37))
        self.inv3_3.setObjectName("inv3_3")
        self.inv3_4 = itemIcon(self)
        self.inv3_4.setGeometry(QtCore.QRect(131, 89, 37, 37))
        self.inv3_4.setObjectName("inv3_4")
        self.inv4_5 = itemIcon(self)
        self.inv4_5.setGeometry(QtCore.QRect(173, 131, 37, 37))
        self.inv4_5.setObjectName("inv4_5")
        self.inv4_2 = itemIcon(self)
        self.inv4_2.setGeometry(QtCore.QRect(47, 131, 37, 37))
        self.inv4_2.setObjectName("inv4_2")
        self.inv4_3 = itemIcon(self)
        self.inv4_3.setGeometry(QtCore.QRect(89, 131, 37, 37))
        self.inv4_3.setObjectName("inv4_3")
        self.inv7_5 = itemIcon(self)
        self.inv7_5.setGeometry(QtCore.QRect(173, 257, 37, 37))
        self.inv7_5.setObjectName("inv7_5")
        self.inv7_1 = itemIcon(self)
        self.inv7_1.setGeometry(QtCore.QRect(5, 257, 37, 37))
        self.inv7_1.setObjectName("inv7_1")
        self.inv6_5 = itemIcon(self)
        self.inv6_5.setGeometry(QtCore.QRect(173, 215, 37, 37))
        self.inv6_5.setObjectName("inv6_5")
        self.inv8_5 = itemIcon(self)
        self.inv8_5.setGeometry(QtCore.QRect(173, 299, 37, 37))
        self.inv8_5.setObjectName("inv8_5")
        self.inv7_2 = itemIcon(self)
        self.inv7_2.setGeometry(QtCore.QRect(47, 257, 37, 37))
        self.inv7_2.setObjectName("inv7_2")
        self.inv5_3 = itemIcon(self)
        self.inv5_3.setGeometry(QtCore.QRect(89, 173, 37, 37))
        self.inv5_3.setObjectName("inv5_3")
        self.inv6_2 = itemIcon(self)
        self.inv6_2.setGeometry(QtCore.QRect(47, 215, 37, 37))
        self.inv6_2.setObjectName("inv6_2")
        self.inv5_4 = itemIcon(self)
        self.inv5_4.setGeometry(QtCore.QRect(131, 173, 37, 37))
        self.inv5_4.setObjectName("inv5_4")
        self.inv6_1 = itemIcon(self)
        self.inv6_1.setGeometry(QtCore.QRect(5, 215, 37, 37))
        self.inv6_1.setObjectName("inv6_1")
        self.inv5_1 = itemIcon(self)
        self.inv5_1.setGeometry(QtCore.QRect(5, 173, 37, 37))
        self.inv5_1.setObjectName("inv5_1")
        self.inv7_4 = itemIcon(self)
        self.inv7_4.setGeometry(QtCore.QRect(131, 257, 37, 37))
        self.inv7_4.setObjectName("inv7_4")
        self.inv5_2 = itemIcon(self)
        self.inv5_2.setGeometry(QtCore.QRect(47, 173, 37, 37))
        self.inv5_2.setObjectName("inv5_2")
        self.inv5_5 = itemIcon(self)
        self.inv5_5.setGeometry(QtCore.QRect(173, 173, 37, 37))
        self.inv5_5.setObjectName("inv5_5")
        self.inv8_2 = itemIcon(self)
        self.inv8_2.setGeometry(QtCore.QRect(47, 299, 37, 37))
        self.inv8_2.setObjectName("inv8_2")
        self.inv8_4 = itemIcon(self)
        self.inv8_4.setGeometry(QtCore.QRect(131, 299, 37, 37))
        self.inv8_4.setObjectName("inv8_4")
        self.inv6_3 = itemIcon(self)
        self.inv6_3.setGeometry(QtCore.QRect(89, 215, 37, 37))
        self.inv6_3.setObjectName("inv6_3")
        self.inv8_1 = itemIcon(self)
        self.inv8_1.setGeometry(QtCore.QRect(5, 299, 37, 37))
        self.inv8_1.setObjectName("inv8_1")
        self.inv7_3 = itemIcon(self)
        self.inv7_3.setGeometry(QtCore.QRect(89, 257, 37, 37))
        self.inv7_3.setObjectName("inv7_3")
        self.inv6_4 = itemIcon(self)
        self.inv6_4.setGeometry(QtCore.QRect(131, 215, 37, 37))
        self.inv6_4.setObjectName("inv6_4")
        self.inv8_3 = itemIcon(self)
        self.inv8_3.setGeometry(QtCore.QRect(89, 299, 37, 37))
        self.inv8_3.setObjectName("inv8_3")

        self.allSlots = [
            self.inv1_1, self.inv1_2, self.inv1_3, self.inv1_4, self.inv1_5,
            self.inv2_1, self.inv2_2, self.inv2_3, self.inv2_4, self.inv2_5,
            self.inv3_1, self.inv3_2, self.inv3_3, self.inv3_4, self.inv3_5,
            self.inv4_1, self.inv4_2, self.inv4_3, self.inv4_4, self.inv4_5,
            self.inv5_1, self.inv5_2, self.inv5_3, self.inv5_4, self.inv5_5,
            self.inv6_1, self.inv6_2, self.inv6_3, self.inv6_4, self.inv6_5,
            self.inv7_1, self.inv7_2, self.inv7_3, self.inv7_4, self.inv7_5,
            self.inv8_1, self.inv8_2, self.inv8_3, self.inv8_4, self.inv8_5,
        ]

    def addEquip(self, row, col, equip):
        slotName = 'inv' + str(row + 1) + '_' + str(col + 1)
        self.filledSlots.append(slotName)
        slot = self.findChild(itemIcon, slotName)
        slot.setEquip(equip)
        slot.dummyPic()

    def getFirstOpenSlot(self):
        empty = None
        for slot in self.allSlots:
            if(slot.equip is None):
                return slot
        return empty

    def removeItem(self, name):
        child = self.findChild(itemIcon, name)
        child.clearSlot()


    def childClicked(self, name):
        child = self.findChild(itemIcon, name)
        if(child.equip is None):
            return
        self.onClick(child)