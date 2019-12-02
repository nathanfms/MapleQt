# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import json
import os
from inventory import inventoryController
from equips import equipController
from stats import statsController
from itemIcon import itemIcon
from symbols import Symbols
from Mapler import Mapler
from skillWindow import skillController

class mainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.resize(960, 390)
        self.setMinimumSize(960, 390)
        self.setMaximumSize(960, 390)
        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 621, 381))
        self.tabWidget.setObjectName("tabWidget")

        self.equipTab = QtWidgets.QWidget()
        self.equipTab.setObjectName("equipTab")
        self.equipCntrl = equipController(self.equipTab, onClick=self.removeEquip)
        self.equipCntrl.setGeometry(QtCore.QRect(0, 0, 279, 258))
        self.equipCntrl.setObjectName("equips")

        self.invCntrl = inventoryController(self.equipTab, onClick=self.swapEquip)
        self.invCntrl.setGeometry(QtCore.QRect(290, 0, 215, 341))
        self.invCntrl.setObjectName("inventory")

        self.symbCntrl = Symbols(self.equipTab, valuesChanged=self.updateSymbols)
        self.symbCntrl.setGeometry(QtCore.QRect(20, 270, 233, 67))
        self.symbCntrl.setObjectName("symbols")

        self.pushButton = QtWidgets.QPushButton(self.equipTab)
        self.pushButton.setGeometry(QtCore.QRect(510, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.equipTab, "Equipment")

        self.hyperLinkTab = QtWidgets.QWidget()
        self.hyperLinkTab.setObjectName("hyperLinkTab")
        self.tabWidget.addTab(self.hyperLinkTab, "Hypers + Skills [1/2]")

        # self.tabWidget.addTab() what is this?
        self.skillTab = QtWidgets.QWidget()
        self.skillTab.setObjectName("skillTab")
        # self.skills = QtWidgets.QWidget(self.skillTab)
        self.skills = skillController(self.skillTab, valuesChanged=self.updateSkills)
        self.skills.setGeometry(QtCore.QRect(10, 10, 600, 335))
        self.skills.setObjectName("skills")
        self.tabWidget.addTab(self.skillTab, "Skills [2/2]")

        self.legionTab = QtWidgets.QWidget()
        self.legionTab.setObjectName("legionTab")
        self.tabWidget.addTab(self.legionTab, "Legion")

        self.statsCntrl = statsController(self)
        self.statsCntrl.setGeometry(QtCore.QRect(630, 20, 321, 341))
        self.statsCntrl.setObjectName("stats")

    #     self.tabWidget.setTabText(self.tabWidget.indexOf(self.equipTab), "Equipment")
    # self.tabWidget.setTabText(self.tabWidget.indexOf(self.hyperLinkTab), "Equipment")
    # self.tabWidget.setTabText(self.tabWidget.indexOf(self.skillTab), "Equipment")
    # self.tabWidget.setTabText(self.tabWidget.indexOf(self.legionTab), "Equipment")
        # self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        # QtCore.QMetaObject.connectSlotsByName(Form)

    @property
    def mapler(self):
        return self._mapler

    def setupMapler(self, passedJson):
        self._mapler = Mapler(json=passedJson)
        self.statsCntrl.name = self.mapler.name
        self.statsCntrl.job = self.mapler.job
        self.statsCntrl.level = self.mapler.level

        #Equips
        for key in self.mapler.equips:
            eqp = self.mapler.equips.get(key)
            self.equipCntrl.updateEquip(eqp=eqp, eqpType=key)

        self.symbCntrl.updateLevels(self.mapler.symbols)

        for key,val in self.mapler.inventory.items():
            row = key[0]
            col = key[1]
            eqp = val
            self.invCntrl.addEquip(row, col, eqp)

        #Skills
        jobName = self.mapler.job
        jobName.replace(" ", "")
        jsonFile = jobName + ".json"
        openSkills = open(os.path.join("jobs", jsonFile))
        jsonSkills = json.load(openSkills)
        self.skills.loadJobSkills(jsonSkills)

        self.statsCntrl.update(json=self.mapler.getTotal())
        # self.update()

    def updateSymbols(self):
        self.mapler.symbols = self.symbCntrl.getLevels()
        self.statsCntrl.update(json=self.mapler.getTotal())

    def updateSkills(self):
        self.mapler.skills = self.skills.total
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

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "add eqp"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.equipTab), _translate("Form", "Equipment"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.hyperLinkTab), _translate("Form", "Hyper + Links"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.skillTab), _translate("Form", "Skills"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.legionTab), _translate("Form", "Legion"))
