# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'skillIcon.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt5 import QtCore, QtGui, QtWidgets
from skillInfo import skillInfo

class skillIcon(QtWidgets.QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.json = None
        self.toolTip = None
        self.setupUi()

    def setupUi(self):
        # self.setGeometry(0, 0, 32, 32)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(0, 0, 32, 32))

        # self.retranslateUi(Form)
        # QtCore.QMetaObject.connectSlotsByName(Form)

    def getStats(self):
        return self.toolTip.currentStats

    def setSkill(self, skill):
        self.json = skill
        self.label.setPixmap(QtGui.QPixmap(os.path.join("assets/skills", self.json.get("img"))))
        self.toolTip = skillInfo(json=self.json, parent=self)

    def updateDecentLevel(self, level):
        self.toolTip.setDecentLevel(level)

    def updateLevel(self, level):
        self.toolTip.setLevel(level)

    def enterEvent(self, event):
        myCoords = self.mapToGlobal(QtCore.QPoint(self.label.x(), self.label.y()))
        if(self.json is not None):
            self.toolTip.move(myCoords.x() + 40, myCoords.y() - (self.toolTip.height()/3))
            self.toolTip.show()

    def leaveEvent(self, event):
        if(self.json is not None):
            self.toolTip.hide()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "-"))
