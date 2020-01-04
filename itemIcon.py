# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'itemIcon.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from item import itemInfo
import inventory

class itemIcon(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.json = None
        self.equip = None
        self.text = None
        self.setupUi()

    def setupUi(self):
        self.setGeometry(0, 0, 37, 37)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(0, 0, 37, 37)
        self.setStyleSheet("background-color: rgb(182, 182, 182);")
        self.mouseDoubleClickEvent = self.notifyParent

    #Tell my parent I was clicked on
    def notifyParent(self, event):
        #Shift + double right click to remove item
        if(QtWidgets.QApplication.keyboardModifiers() == QtCore.Qt.ShiftModifier and event.button() == 2 and type(self.parent) is inventory.inventoryController):
            # print(QtWidgets.QApplication.keyboardModifiers())
            self.parent.removeItem(self.objectName())
        self.parent.childClicked(self.objectName())

    #Copy values from another itemIcon. Used for inventory -> equip and vice versa
    def importFromOther(self, theOther):
        self.json = theOther.json
        self.equip = theOther.equip
        self.toolTip = theOther.toolTip

    def setText(self, text):
        self.label.setStyleSheet("background-color: rgb(182, 182, 182); qproperty-alignment: AlignCenter; font-size: 9px;")
        self.label.setText(text)
        self.text = text

    def setEquip(self, equip):
        self.equip = equip
        self.equip.recalcTotal()
        self.setJson(equip.json)

    def setJson(self, json):
        self.json = json
        self.toolTip = itemInfo(eqp=self.equip, parent=self)

    def clearSlot(self):
        self.json = None
        self.toolTip.hide()
        self.toolTip = None
        self.equip = None
        self.clearPic()

    def dummyPic(self):
        self.label.setPixmap(QtGui.QPixmap("assets/dummy-icon.png"))

    def clearPic(self):
        self.label.clear()
        if(self.text is not None):
            self.setText(self.text)

    def setPic(self, location):
        self.label.setScaledContents(True)
        self.label.setPixmap(QtGui.QPixmap(location))

    def enterEvent(self, event):
        myCoords = self.mapToGlobal(QtCore.QPoint(self.label.x(), self.label.y()))
        if(self.json is not None):
            self.toolTip.move(myCoords.x() + 40, myCoords.y() - (self.toolTip.height()/3))
            self.toolTip.show()

    def leaveEvent(self, event):
        if(self.json is not None):
            self.toolTip.hide()
        


