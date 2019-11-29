# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from inventory import inventoryController
from equips import equipController
from stats import statsController
from itemIcon import itemIcon
from symbols import Symbols
from Mapler import Mapler


class mainController(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.resize(854, 360)
        # self.setMinimumWidth(854)
        # self.setMinimumHeight(360)
        self.setMinimumSize(854, 360)
        self.setMaximumSize(854, 360)
        self.equipCntrl = equipController(self, onClick=self.removeEquip)
        self.equipCntrl.setGeometry(QtCore.QRect(340, 10, 279, 258))
        self.equipCntrl.setObjectName("equips")
        self.statsCntrl = statsController(self)
        self.statsCntrl.setGeometry(QtCore.QRect(10, 10, 321, 341))
        self.statsCntrl.setObjectName("stats")
        self.invCntrl = inventoryController(self, onClick=self.swapEquip)
        self.invCntrl.setGeometry(QtCore.QRect(630, 10, 215, 341))
        self.invCntrl.setObjectName("inventory")
        self.symbCntrl = Symbols(self, valuesChanged=self.updateSymbols)
        self.symbCntrl.setGeometry(QtCore.QRect(340, 270, 233, 67))
        self.symbCntrl.setObjectName("symbols")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(570, 270, 51, 41))
        self.pushButton.setObjectName("pushButton")

        # self.retranslateUi(Form)
        # QtCore.QMetaObject.connectSlotsByName(Form)

    @property
    def mapler(self):
        return self._mapler

    def setupMapler(self, json):
        self._mapler = Mapler(json=json)
        self.statsCntrl.name = self.mapler.name
        self.statsCntrl.job = self.mapler.job
        self.statsCntrl.level = self.mapler.level

        for key in self.mapler.equips:
            eqp = self.mapler.equips.get(key)
            self.equipCntrl.updateEquip(eqp=eqp, eqpType=key)

        self.symbCntrl.updateLevels(self.mapler.symbols)

        for key,val in self.mapler.inventory.items():
            row = key[0]
            col = key[1]
            eqp = val
            self.invCntrl.addEquip(row, col, eqp)

        self.statsCntrl.update(json=self.mapler.getTotal())
        # self.update()

    def updateSymbols(self):
        self.mapler.symbols = self.symbCntrl.getLevels()
        self.statsCntrl.update(json=self.mapler.getTotal())

    #Equip in inventory -> Equipped
    def swapEquip(self, item):
        itemType = item.equip.eqpType
        if(itemType == 'PENDANT'):
            itemType = self.mapler.getOpenPendSlot()
        elif(itemType == 'TOTEM'):
            itemType = self.mapler.getOpenTotemSlot()
        elif(itemType == 'RING'):
            itemType = self.mapler.getOpenRingSlot()
        elif(itemType == 'PET'):
            itemType = self.mapler.getOpenPetSlot()
        oldEquipType = self.mapler.addEquip(item.equip)
        equipSlot = self.equipCntrl.findChild(itemIcon, itemType.lower())

        if(oldEquipType is not None):
            temp = itemIcon(self.invCntrl)
            temp.importFromOther(equipSlot)
            equipSlot.importFromOther(item)
            item.clearSlot()
            freeInvSlot = self.invCntrl.getFirstOpenSlot()
            freeInvSlot.importFromOther(temp)
            freeInvSlot.dummyPic()
        else:
            equipSlot.importFromOther(item)
            item.clearSlot()
        equipSlot.dummyPic()
        self.statsCntrl.update(json=self.mapler.getTotal())

    def removeEquip(self, item):
        freeInvSlot = self.invCntrl.getFirstOpenSlot()
        freeInvSlot.importFromOther(item)
        freeInvSlot.dummyPic()
        item.clearSlot()
        self.mapler.removeEquip(item.objectName())
        self.statsCntrl.update(json=self.mapler.getTotal())
        # self.mapler.removeEquip(item.name)

    def update(self):
        pass
        
    def equipClicked(self, event):
        pass
