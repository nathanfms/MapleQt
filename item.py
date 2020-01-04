# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'item.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

def countAttributes(json):
    values = []
    if(json.get("base") is not None):
        for str in json["base"]:
            if(str not in values):
                values.append(str)
    if(json.get("star") is not None):
        for str in json["star"]:
            if(str not in values):
                values.append(str)
        values.remove("amount")
    if(json.get("flame") is not None):
        for str in json["flame"]:
            if(str not in values):
                values.append(str)
    return values

#The json passed to this is not the whole json, but the part you are examining e.g. json["mpot"], json["bpot"]
def formatPotLines(json):
    lines = []
    vals = []
    for key in json:
        if type(json.get(key)) is list:
            for val in json.get(key):
                lines.append(key)
                if(val < 1 and val > 0):
                    val = str(int(val * 100)) + "%"
                vals.append(val)
        else:
            lines.append(key)
            if(json.get(key) < 1 and json.get(key) > 0):
                vals.append(str(int(json.get(key) * 100)) + "%")
            else:
                vals.append(json.get(key))
    return [lines, vals]

def getStatTotal(json, statArray):
    totals = [0] * len(statArray)
    for num, key in enumerate(statArray):

        if(json.get("base") is not None):
            baseVal = json["base"].get(key)
            if(baseVal is not None):
                totals[num] += baseVal
        if(json.get("star") is not None):
            starVal = json["star"].get(key)
            if(starVal is not None):
                totals[num] += starVal
        if(json.get("flame") is not None):
            flameVal = json["flame"].get(key)
            if(flameVal is not None):
                totals[num] += flameVal
                if(flameVal < 1 and flameVal > 0): #is percentage, format accordingly
                    totals[num] = str(int(totals[num] * 100)) + "%"
    return totals

#The json passed to this is not the whole json, but the part you are examining e.g. json["base"], json["star"]
def getStatSpecific(json, statArray):
    totals = [0] * len(statArray)
    for num, key in enumerate(statArray):
        val = json.get(key)
        if(val is not None):
            totals[num] += val
            if(val < 1 and val > 0): #is percentage, format accordingly
                totals[num] = str(int(totals[num] * 100)) + "%"
    #replace all 0's with a blank string. I want the UI to be blank in those spots, not have 0
    newTotals = [x if x != 0 else "" for x in totals]
    return newTotals

class itemInfo(QtWidgets.QWidget):
    def __init__(self, eqp=None, parent=None):
        super().__init__(parent)
        self.eqp = eqp
        self.json = eqp.json
        self.jsonVals = countAttributes(self.json)
        self.setupUi()
        

    def setupUi(self):
        self.setWindowFlags(
            QtCore.Qt.CustomizeWindowHint |
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.ToolTip
        )
        statHeight = 22 * len(self.jsonVals) + 5
        self.setObjectName("Item")
        self.resize(294, 695)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setAutoFillBackground(False)
        self.setStyleSheet("background-color: rgb(79, 79, 79);")

        self.stars = QtWidgets.QLabel(self)
        self.stars.setGeometry(QtCore.QRect(0, 10, 301, 31))
        self.stars.setStyleSheet("color: rgb(229, 229, 0); font-size: 20px; qproperty-alignment: AlignCenter;")
        self.stars.setObjectName("stars")

        self.itemName = QtWidgets.QLabel(self)
        self.itemName.setGeometry(QtCore.QRect(0, 40, 301, 21))
        self.itemName.setStyleSheet("color: rgb(255, 0, 255); font-size: 16px; padding-left: 7px;")
        self.itemName.setObjectName("itemName")

        self.itemImg = QtWidgets.QLabel(self)
        self.itemImg.setGeometry(QtCore.QRect(10, 70, 80, 80))
        self.itemImg.setText("")
        img = 'assets/equips/' + self.eqp.id + '.png'
        self.itemImg.setPixmap(QtGui.QPixmap(img))
        self.itemImg.setObjectName("itemImg")

        self.range = QtWidgets.QLabel(self)
        self.range.setGeometry(QtCore.QRect(100, 70, 191, 51))
        self.range.setStyleSheet("color: rgb(223, 223, 223); font-size: 32px; qproperty-alignment: AlignRight;")
        self.range.setObjectName("range")

        self.attributes = QtWidgets.QListWidget(self)
        self.attributes.setGeometry(QtCore.QRect(0, 170, 71, statHeight))
        self.attributes.setMinimumWidth(self.attributes.sizeHintForColumn(0))
        self.attributes.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.attributes.setStyleSheet("color: rgb(227, 227, 227); font-size: 14px;")
        self.attributes.setFlow(QtWidgets.QListView.TopToBottom)
        self.attributes.setProperty("isWrapping", False)
        self.attributes.setResizeMode(QtWidgets.QListView.Fixed)
        self.attributes.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.attributes.setItemAlignment(QtCore.Qt.AlignAbsolute|QtCore.Qt.AlignHCenter|QtCore.Qt.AlignJustify|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.attributes.setObjectName("attributes")
        for i in range (0, len(self.jsonVals)):
            item = QtWidgets.QListWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            self.attributes.addItem(item)
        # item = QtWidgets.QListWidgetItem()
        # item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        # self.attributes.addItem(item)

        self.totalList = QtWidgets.QListWidget(self)
        self.totalList.setGeometry(QtCore.QRect(70, 170, 52, statHeight))
        self.totalList.setStyleSheet("color: rgb(0, 231, 231); font-size: 14px;")
        self.totalList.setObjectName("totalList")
        for i in range (0, len(self.jsonVals)):
            item = QtWidgets.QListWidgetItem()
            self.totalList.addItem(item)
        # item = QtWidgets.QListWidgetItem()
        # self.totalList.addItem(item)

        self.baseList = QtWidgets.QListWidget(self)
        self.baseList.setGeometry(QtCore.QRect(120, 170, 52, statHeight))
        self.baseList.setStyleSheet("color: rgb(227, 227, 227); font-size: 14px;")
        self.baseList.setObjectName("baseList")
        for i in range (0, len(self.jsonVals)):
            item = QtWidgets.QListWidgetItem()
            self.baseList.addItem(item)
        # item = QtWidgets.QListWidgetItem()
        # self.baseList.addItem(item)

        self.flameList = QtWidgets.QListWidget(self)
        self.flameList.setGeometry(QtCore.QRect(165, 170, 52, statHeight))
        self.flameList.setStyleSheet("color: rgb(0, 226, 0); font-size: 14px;")
        self.flameList.setObjectName("flameList")
        for i in range (0, len(self.jsonVals)):
            item = QtWidgets.QListWidgetItem()
            self.flameList.addItem(item)
        # item = QtWidgets.QListWidgetItem()
        # self.flameList.addItem(item)

        self.starList = QtWidgets.QListWidget(self)
        self.starList.setGeometry(QtCore.QRect(210, 170, 51, statHeight))
        self.starList.setStyleSheet("color: rgb(0, 231, 231); font-size: 14px;")
        self.starList.setObjectName("starList")
        for i in range (0, len(self.jsonVals)):
            item = QtWidgets.QListWidgetItem()
            self.starList.addItem(item)
        # item = QtWidgets.QListWidgetItem()
        # self.starList.addItem(item)

        self.totalLabel = QtWidgets.QLabel(self)
        self.totalLabel.setGeometry(QtCore.QRect(70, 150, 47, 13))
        self.totalLabel.setStyleSheet("color: rgb(0, 231, 231); font-size: 10px; qproperty-alignment: AlignCenter;")
        self.totalLabel.setObjectName("totalLabel")

        self.baseLabel = QtWidgets.QLabel(self)
        self.baseLabel.setGeometry(QtCore.QRect(116, 150, 47, 13))
        self.baseLabel.setStyleSheet("color: rgb(223, 223, 223); font-size: 10px; qproperty-alignment: AlignCenter;")
        self.baseLabel.setObjectName("baseLabel")

        self.flameLabel = QtWidgets.QLabel(self)
        self.flameLabel.setGeometry(QtCore.QRect(157, 150, 47, 13))
        self.flameLabel.setStyleSheet("color: rgb(0, 226, 0); font-size: 10px; qproperty-alignment: AlignCenter;")
        self.flameLabel.setObjectName("flameLabel")

        self.starLabel = QtWidgets.QLabel(self)
        self.starLabel.setGeometry(QtCore.QRect(200, 150, 47, 13))
        self.starLabel.setStyleSheet("color: rgb(0, 231, 231); font-size: 10px; qproperty-alignment: AlignCenter;")
        self.starLabel.setObjectName("starLabel")

        mpotHeight = 0
        if(self.json.get("mpot") is not None):
            self.mpot = formatPotLines(self.json["mpot"])
            mpotHeight = 22 * len(self.mpot[0]) + 21 #16 + 5
            self.mpotLabel = QtWidgets.QLabel(self)
            self.mpotLabel.setGeometry(QtCore.QRect(5, statHeight + 170, 91, 16)) #170 = Y coordinate of lists
            self.mpotLabel.setStyleSheet("color: rgb(0, 226, 0); font-size: 10px; qproperty-alignment: AlignCenter;")
            self.mpotLabel.setObjectName("mpotLabel")

            self.mpotLines = QtWidgets.QListWidget(self)
            self.mpotLines.setGeometry(QtCore.QRect(0, statHeight + 170 + 16, 161, 22 * len(self.mpot[0]) + 5))
            self.mpotLines.setStyleSheet("color: rgb(227, 227, 227); font-size: 14px;")
            self.mpotLines.setObjectName("mpotLines")
            for val in self.mpot[0]:
                item = QtWidgets.QListWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.mpotLines.addItem(item)
            # item = QtWidgets.QListWidgetItem()
            # item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            # self.mpotLines.addItem(item)


            self.mpotVals = QtWidgets.QListWidget(self)
            self.mpotVals.setGeometry(QtCore.QRect(160, statHeight + 170 + 16, 51, 22 * len(self.mpot[0]) + 5))
            self.mpotVals.setStyleSheet("color: rgb(227, 227, 227); font-size: 14px;")
            self.mpotVals.setObjectName("mpotVals")
            for val in self.mpot[0]:
                item = QtWidgets.QListWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.mpotVals.addItem(item)
            # item = QtWidgets.QListWidgetItem()
            # item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
            # self.mpotVals.addItem(item)

        bpotHeight = 0
        if(self.json.get("bpot") is not None):
            self.bpot = formatPotLines(self.json["bpot"])
            bpotHeight = 22 * len(self.bpot[0]) + 21
            self.bpotLabel = QtWidgets.QLabel(self)
            self.bpotLabel.setGeometry(QtCore.QRect(5, statHeight + mpotHeight + 170, 101, 16))
            self.bpotLabel.setStyleSheet("color: rgb(0, 226, 0); font-size: 10px; qproperty-alignment: AlignCenter;")
            self.bpotLabel.setObjectName("bpotLabel")

            self.bpotLines = QtWidgets.QListWidget(self)
            self.bpotLines.setGeometry(QtCore.QRect(0, statHeight + mpotHeight + 170 + 16, 161, 22 * len(self.bpot[0]) + 5))
            self.bpotLines.setStyleSheet("color: rgb(227, 227, 227); font-size: 14px;")
            self.bpotLines.setObjectName("bpotLines")
            for val in self.bpot[0]:
                item = QtWidgets.QListWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.bpotLines.addItem(item)
            # item = QtWidgets.QListWidgetItem()
            # item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            # self.bpotLines.addItem(item)

            self.bpotVals = QtWidgets.QListWidget(self)
            self.bpotVals.setGeometry(QtCore.QRect(160, statHeight + mpotHeight + 170 + 16, 51, 22 * len(self.bpot[0]) + 5))
            self.bpotVals.setStyleSheet("color: rgb(227, 227, 227); font-size: 14px;")
            self.bpotVals.setObjectName("bpotVals")
            for val in self.bpot[0]:
                item = QtWidgets.QListWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
                self.bpotVals.addItem(item)
            # item = QtWidgets.QListWidgetItem()
            # item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
            # self.bpotVals.addItem(item)

        soulHeight = 0
        if(self.json.get("soul") is not None):
            soulHeight = 32
            self.soulLabel = QtWidgets.QLabel(self)
            self.soulLabel.setGeometry(QtCore.QRect(7, statHeight + mpotHeight + bpotHeight + 170, 31, 16))
            self.soulLabel.setStyleSheet("color: rgb(241, 241, 0); font-size: 10px; qproperty-alignment: AlignCenter;")
            self.soulLabel.setObjectName("soulLabel")

            self.soulLine = QtWidgets.QListWidget(self)
            self.soulLine.setGeometry(QtCore.QRect(0, statHeight + mpotHeight + bpotHeight + 170 + 16, 161, 27))
            self.soulLine.setStyleSheet("color: rgb(227, 227, 227); font-size: 14px;")
            self.soulLine.setObjectName("soulLine")
            item = QtWidgets.QListWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            self.soulLine.addItem(item)

            self.soulVal = QtWidgets.QListWidget(self)
            self.soulVal.setGeometry(QtCore.QRect(160, statHeight + mpotHeight + bpotHeight + 170 + 16, 51, 27))
            self.soulVal.setStyleSheet("color: rgb(227, 227, 227); font-size: 14px;")
            self.soulVal.setObjectName("soulVal")
            item = QtWidgets.QListWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
            self.soulVal.addItem(item)

        self.typeLabel = QtWidgets.QLabel(self)
        self.typeLabel.setGeometry(QtCore.QRect(90, 130, 47, 13))
        self.typeLabel.setStyleSheet("color: rgb(223, 223, 223); font-size: 10px; qproperty-alignment: AlignCenter;")
        self.typeLabel.setObjectName("typeLabel")

        self.itemType = QtWidgets.QLabel(self)
        self.itemType.setGeometry(QtCore.QRect(130, 131, 111, 16))
        self.itemType.setStyleSheet("font-size: 10px; color: rgb(255, 0, 255); qproperty-alignment: AlignLeft;")
        self.itemType.setObjectName("itemType")

        self.retranslateUi()
        # self.retranslateUi(Form)
        # QtCore.QMetaObject.connectSlotsByName(Form)
        
        self.resize(294, statHeight + mpotHeight + bpotHeight + soulHeight + 170 + 16)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        if(self.json.get("star") is not None):
            starAmount = self.json.get("star").get("amount")
            self.stars.setText(_translate("Form", str(starAmount) + '*'))
        else:
            self.stars.setText(_translate("Form", "0*"))
        # self.stars.setText(_translate("Form", str(self.json["star"]["amount"]) + '*'))
        self.itemName.setText(_translate("Form", self.json["name"]))
        self.range.setText(_translate("Form", "+99,999,999"))
        __sortingEnabled = self.attributes.isSortingEnabled()
        self.attributes.setSortingEnabled(False)

        jsonVals = countAttributes(self.json)

        for num in range(0, len(jsonVals)):
            item = self.attributes.item(num)
            name = jsonVals[num]
            item.setText(_translate("Form", name))
        # item = self.attributes.item(0)
        # item.setText(_translate("Form", "STR:"))
        # item = self.attributes.item(1)
        # item.setText(_translate("Form", "DEX:"))
        # item = self.attributes.item(2)
        # item.setText(_translate("Form", "INT:"))
        # item = self.attributes.item(3)
        # item.setText(_translate("Form", "LUK:"))
        # item = self.attributes.item(4)
        # item.setText(_translate("Form", "HP:"))
        # item = self.attributes.item(5)
        # item.setText(_translate("Form", "MP:"))
        # item = self.attributes.item(6)
        # item.setText(_translate("Form", "ATK:"))
        # item = self.attributes.item(7)
        # item.setText(_translate("Form", "M.ATK:"))
        # item = self.attributes.item(8)
        # item.setText(_translate("Form", "DEF:"))
        # item = self.attributes.item(9)
        # item.setText(_translate("Form", "SPEED:"))
        # item = self.attributes.item(10)
        # item.setText(_translate("Form", "JUMP:"))
        # item = self.attributes.item(11)
        # item.setText(_translate("Form", "BOSS:"))
        # item = self.attributes.item(12)
        # item.setText(_translate("Form", "IGNORE:"))
        # item = self.attributes.item(13)
        # item.setText(_translate("Form", "ALL%:"))
        self.attributes.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.totalList.isSortingEnabled()
        self.totalList.setSortingEnabled(False)

        totalStatValues = getStatTotal(self.json, jsonVals)
        for i in range(0, len(totalStatValues)):
            item = self.totalList.item(i)
            stringVal = "+" + str(totalStatValues[i])
            item.setText(_translate("Form", stringVal))

        # item = self.totalList.item(0)
        # item.setText(_translate("Form", "+555"))
        self.totalList.setSortingEnabled(__sortingEnabled)

        __sortingEnabled = self.baseList.isSortingEnabled()
        self.baseList.setSortingEnabled(False)

        if(self.json.get("base") is not None):
            baseVals = getStatSpecific(self.json["base"], jsonVals)
            for i in range(0, len(baseVals)):
                item = self.baseList.item(i)
                stringVal =  str(baseVals[i])
                if(stringVal != ""):
                    stringVal = "+" + stringVal
                item.setText(_translate("Form", stringVal))
            # item = self.baseList.item(0)
            # item.setText(_translate("Form", "(222"))
            self.baseList.setSortingEnabled(__sortingEnabled)

        __sortingEnabled = self.flameList.isSortingEnabled()
        self.flameList.setSortingEnabled(False)

        if(self.json.get("flame") is not None):
            flameVals = getStatSpecific(self.json["flame"], jsonVals)
            for i in range(0, len(flameVals)):
                item = self.flameList.item(i)
                stringVal = str(flameVals[i])
                if(stringVal != ""):
                    stringVal = "+" + stringVal
                item.setText(_translate("Form", stringVal))
            # item = self.flameList.item(0)
            # item.setText(_translate("Form", "+888"))
            self.flameList.setSortingEnabled(__sortingEnabled)

        __sortingEnabled = self.starList.isSortingEnabled()
        self.starList.setSortingEnabled(False)

        if(self.json.get("star") is not None):
            starVals = getStatSpecific(self.json["star"], jsonVals)
            for i in range(0, len(starVals)):
                item = self.starList.item(i)
                stringVal = str(starVals[i])
                if(stringVal != ""):
                    stringVal = "+" + stringVal
                item.setText(_translate("Form", stringVal))
        # item = self.starList.item(0)
        # item.setText(_translate("Form", "+245)"))
        self.starList.setSortingEnabled(__sortingEnabled)
        self.totalLabel.setText(_translate("Form", "TOTAL"))
        self.baseLabel.setText(_translate("Form", "BASE"))
        self.flameLabel.setText(_translate("Form", "FLAME"))
        self.starLabel.setText(_translate("Form", "STAR"))

        if(self.json.get("mpot") is not None):
            __sortingEnabled = self.mpotLines.isSortingEnabled()
            self.mpotLines.setSortingEnabled(False)

            for i in range(0, len(self.mpot[0])):
                item = self.mpotLines.item(i)
                item.setText(_translate("Form", self.mpot[0][i]))

            self.mpotLines.setSortingEnabled(__sortingEnabled)
            __sortingEnabled = self.mpotVals.isSortingEnabled()
            self.mpotVals.setSortingEnabled(False)

            for i in range(0, len(self.mpot[1])):
                text = "+" + self.mpot[1][i]
                item = self.mpotVals.item(i)
                item.setText(_translate("Form", text))

            self.mpotVals.setSortingEnabled(__sortingEnabled)
            self.mpotLabel.setText(_translate("Form", "MAIN POTENTIAL"))

        if(self.json.get("bpot") is not None):
            self.bpotLabel.setText(_translate("Form", "BONUS  POTENTIAL"))
            __sortingEnabled = self.bpotLines.isSortingEnabled()
            self.bpotLines.setSortingEnabled(False)

            for i in range(0, len(self.bpot[0])):
                item = self.bpotLines.item(i)
                item.setText(_translate("Form", self.bpot[0][i]))

            self.bpotLines.setSortingEnabled(__sortingEnabled)
            __sortingEnabled = self.bpotVals.isSortingEnabled()
            self.bpotVals.setSortingEnabled(False)
            for i in range(0, len(self.bpot[1])):
                item = self.bpotVals.item(i)
                text = "+" + str(self.bpot[1][i])
                item.setText(_translate("Form", text))
            self.bpotVals.setSortingEnabled(__sortingEnabled)

        if(self.json.get("soul") is not None and any(self.json.get("soul"))):
            soul = formatPotLines(self.json["soul"])
            self.soulLabel.setText(_translate("Form", "SOUL"))
            __sortingEnabled = self.soulLine.isSortingEnabled()
            self.soulLine.setSortingEnabled(False)

            item = self.soulLine.item(0)
            item.setText(_translate("Form", soul[0][0]))

            self.soulLine.setSortingEnabled(__sortingEnabled)
            __sortingEnabled = self.soulVal.isSortingEnabled()
            self.soulVal.setSortingEnabled(False)

            item = self.soulVal.item(0)
            text = "+" + str(soul[1][0])
            item.setText(_translate("Form", text))

            self.soulVal.setSortingEnabled(__sortingEnabled)
            
        self.typeLabel.setText(_translate("Form", "TYPE:"))
        self.itemType.setText(_translate("Form", self.json["type"]))
        # self.show()
        # self.setVisible(True)
