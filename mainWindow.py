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
from links import linkSkillController
from hypers import hyperController
from legion import legionController
import shutil
import gameReader

class mainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._db = None
        self.setupUi()
    
    @property
    def db(self):
        return self._db

    @db.setter
    def db(self, value):
        self._db = value

    def setupUi(self):
        self.resize(960, 410)
        self.setMinimumSize(960, 410)
        self.setMaximumSize(960, 410)
        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 621, 410))
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

        self.readerButton = QtWidgets.QPushButton(self.equipTab)
        self.readerButton.setGeometry(QtCore.QRect(510, 10, 100, 23))
        self.readerButton.setObjectName("readerButton")
        self.readerButton.setText("Read in Equips")
        self.readerButton.clicked.connect(self.readGame)
        self.stopButton = QtWidgets.QPushButton(self.equipTab)
        self.stopButton.setGeometry(QtCore.QRect(510, 40, 100, 23))
        self.stopButton.setText("Stop Reading")
        self.stopButton.setEnabled(False)
        self.stopButton.clicked.connect(self.stopReading)
        self.readLabel = QtWidgets.QLabel(self.equipTab)
        self.readLabel.setGeometry(QtCore.QRect(512, 55, 100, 40))
        self.readLabel.setText("Read Equips: 0")

        self.tabWidget.addTab(self.equipTab, "Equipment")

        self.hyperLinkTab = QtWidgets.QWidget()
        self.hyperLinkTab.setObjectName("hyperLinkTab")
        self.links = linkSkillController(self.hyperLinkTab, valuesChanged=self.updateLinkSkills)
        self.links.setGeometry(10, 10, 375, 365)
        self.hypers = hyperController(self.hyperLinkTab, valuesChanged=self.updateHypers)
        self.hypers.setGeometry(440, 10, 140, 265)
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
        self.legion = legionController(self.legionTab, valuesChanged=self.updateLegion)
        self.legion.setGeometry(QtCore.QRect(5, 5, 621, 380))
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

    def readGame(self):
        self.stopButton.setEnabled(True)
        gameReader.keepReading = True
        
        gameReader.screen_record(self.successfullyReadEquip)
        # for e in equips:
        #     print(e.name)

    def successfullyReadEquip(self, equip):
        print(equip.name)
        slot = self.invCntrl.getFirstOpenSlot()

        if(slot is not None and slot[0] is not None):
            id = self.db.addEquip(equip.json)
            moveFile = './assets/equips/' + str(id) + '.png'
            shutil.copy('./temp-vision-files/itemIcon.png', moveFile)
            info = {'row':slot[1], 'col':slot[2], 'id':str(id)}
            self.db.addEquipToInventory(info) 

            before = self.readLabel.text()
            num = int(before[before.find(':') + 1:])
            after = 'Read Equips: ' + str(num + 1)
            self.readLabel.setText(after)




    def stopReading(self):
        self.stopButton.setEnabled(False)
        gameReader.keepReading = False
        # equips = gameReader.readEquips
        # gameReader.readEquips.clear()
        # for e in equips:
        #     print(e.name)

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
            print('main: ', val.id)
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
        self.skills.loadLevelsFromDb(passedJson.get("skills"))

        self.links.loadLevelsFromDb(passedJson.get("links"))

        self.hypers.loadLevelsFromDb(passedJson.get("hypers"))

        self.legion.loadLevelsFromDb(passedJson.get("legion"))

        self.statsCntrl.update(json=self.mapler.getTotal())
        # self.update()

    def updateSymbols(self):
        self.mapler.symbols = self.symbCntrl.getLevels()
        self.statsCntrl.update(json=self.mapler.getTotal())

    def updateSkills(self):
        self.mapler.skills = self.skills.total
        self.statsCntrl.update(json=self.mapler.getTotal())

    def updateLinkSkills(self):
        self.mapler.links = self.links.total
        self.statsCntrl.update(json=self.mapler.getTotal())

    def updateHypers(self):
        self.mapler.hypers = self.hypers.total
        self.statsCntrl.update(json=self.mapler.getTotal())

    def updateLegion(self):
        self.mapler.legion = self.legion.total
        self.statsCntrl.update(json=self.mapler.getTotal())

    #Equip in inventory -> Equipped
    def swapEquip(self, item, rightClick=False):
        if(rightClick):
            self.deleteEquip(item)
            return
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
        print(itemType.lower())
        if(oldEquipType is not None):
            temp = itemIcon(self.invCntrl)
            temp.importFromOther(equipSlot)
            equipSlot.importFromOther(item)
            item.clearSlot()
            freeInvSlot = self.invCntrl.getFirstOpenSlot()[0]
            freeInvSlot.importFromOther(temp)
            img = 'assets/equips/' + temp.equip.id + '.png'
            freeInvSlot.setPic(img)
            # freeInvSlot.dummyPic()
        else:
            equipSlot.importFromOther(item)
            item.clearSlot()
        # equipSlot.dummyPic()
        # print(equipSlot.equip.name)
        img = 'assets/equips/' + equipSlot.equip.id + '.png'
        equipSlot.setPic(img)
        self.statsCntrl.update(json=self.mapler.getTotal())

    def removeEquip(self, item):
        print('called')
        freeInvSlot = self.invCntrl.getFirstOpenSlot()[0]
        freeInvSlot.importFromOther(item)
        # freeInvSlot.dummyPic()
        img = 'assets/equips/' + item.equip.id + '.png'
        freeInvSlot.setPic(img)
        item.clearSlot()
        self.mapler.removeEquip(item.objectName())
        self.statsCntrl.update(json=self.mapler.getTotal())
        # self.mapler.removeEquip(item.name)

    def deleteEquip(self, id):
        self.db.removeEquip(id)

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

    def save(self):
        print("i'm saving")
        self.db.updateLinks(self.links.getJsonForDb())
        self.db.updateSkills(self.skills.getJsonForDb())
        self.db.updateHypers(self.hypers.getJsonForDb())
        self.db.updateLegion(self.legion.getJsonForDb())
        self.db.updateInventory(self.invCntrl.getJsonForDb())
        self.db.updateEquips(self.mapler.getEquipJsonForDb())
