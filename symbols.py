# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'symbols.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Symbols(QtWidgets.QWidget):
    #valuesChanged = method to call when values change
    def __init__(self, parent=None, valuesChanged=None):
        super().__init__(parent)
        self.valuesChanged = valuesChanged
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Symbols")
        self.resize(233, 67)
        self.vjImg = QtWidgets.QLabel(self)
        self.vjImg.setGeometry(QtCore.QRect(0, 0, 33, 33))
        self.vjImg.setText("")
        self.vjImg.setPixmap(QtGui.QPixmap("assets/symbols/vj.png"))
        self.vjImg.setObjectName("vjImg")
        self.chuImg = QtWidgets.QLabel(self)
        self.chuImg.setGeometry(QtCore.QRect(40, 0, 33, 33))
        self.chuImg.setText("")
        self.chuImg.setPixmap(QtGui.QPixmap("assets/symbols/chu.png"))
        self.chuImg.setObjectName("chuImg")
        self.lachImg = QtWidgets.QLabel(self)
        self.lachImg.setGeometry(QtCore.QRect(80, 0, 33, 33))
        self.lachImg.setText("")
        self.lachImg.setPixmap(QtGui.QPixmap("assets/symbols/lach.png"))
        self.lachImg.setObjectName("lachImg")
        self.arcImg = QtWidgets.QLabel(self)
        self.arcImg.setGeometry(QtCore.QRect(120, 0, 33, 33))
        self.arcImg.setText("")
        self.arcImg.setPixmap(QtGui.QPixmap("assets/symbols/arc.png"))
        self.arcImg.setObjectName("arcImg")
        self.morImg = QtWidgets.QLabel(self)
        self.morImg.setGeometry(QtCore.QRect(160, 0, 33, 33))
        self.morImg.setText("")
        self.morImg.setPixmap(QtGui.QPixmap("assets/symbols/mor.png"))
        self.morImg.setObjectName("morImg")
        self.esfImg = QtWidgets.QLabel(self)
        self.esfImg.setGeometry(QtCore.QRect(200, 0, 33, 33))
        self.esfImg.setText("")
        self.esfImg.setPixmap(QtGui.QPixmap("assets/symbols/esf.png"))
        self.esfImg.setObjectName("esfImg")
        self.vjSpinBox = QtWidgets.QSpinBox(self)
        self.vjSpinBox.setGeometry(QtCore.QRect(0, 40, 33, 22))
        self.vjSpinBox.setMaximum(20)
        self.vjSpinBox.setProperty("value", 0)
        self.vjSpinBox.setObjectName("vjSpinBox")
        self.chuSpinBox = QtWidgets.QSpinBox(self)
        self.chuSpinBox.setGeometry(QtCore.QRect(40, 40, 33, 22))
        self.chuSpinBox.setMaximum(20)
        self.chuSpinBox.setProperty("value", 0)
        self.chuSpinBox.setObjectName("chuSpinBox")
        self.lachSpinBox = QtWidgets.QSpinBox(self)
        self.lachSpinBox.setGeometry(QtCore.QRect(80, 40, 33, 22))
        self.lachSpinBox.setMaximum(20)
        self.lachSpinBox.setProperty("value", 0)
        self.lachSpinBox.setObjectName("lachSpinBox")
        self.arcSpinBox = QtWidgets.QSpinBox(self)
        self.arcSpinBox.setGeometry(QtCore.QRect(120, 40, 33, 22))
        self.arcSpinBox.setMaximum(20)
        self.arcSpinBox.setProperty("value", 0)
        self.arcSpinBox.setObjectName("arcSpinBox")
        self.morSpinBox = QtWidgets.QSpinBox(self)
        self.morSpinBox.setGeometry(QtCore.QRect(160, 40, 33, 22))
        self.morSpinBox.setMaximum(20)
        self.morSpinBox.setProperty("value", 0)
        self.morSpinBox.setObjectName("morSpinBox")
        self.esfSpinBox = QtWidgets.QSpinBox(self)
        self.esfSpinBox.setGeometry(QtCore.QRect(200, 40, 33, 22))
        self.esfSpinBox.setMaximum(20)
        self.esfSpinBox.setProperty("value", 0)
        self.esfSpinBox.setObjectName("esfSpinBox")
        self.vjSpinBox.valueChanged.connect(self.valuesChanged)
        self.chuSpinBox.valueChanged.connect(self.valuesChanged)
        self.lachSpinBox.valueChanged.connect(self.valuesChanged)
        self.arcSpinBox.valueChanged.connect(self.valuesChanged)
        self.morSpinBox.valueChanged.connect(self.valuesChanged)
        self.esfSpinBox.valueChanged.connect(self.valuesChanged)

        # self.retranslateUi(Form)
        # QtCore.QMetaObject.connectSlotsByName(Form)

    # def retranslateUi(self, Form):
    #     _translate = QtCore.QCoreApplication.translate
    #     Form.setWindowTitle(_translate("Form", "Form"))

    def updateLevels(self, levels):
        self.vjSpinBox.setProperty("value", levels[0])
        self.chuSpinBox.setProperty("value", levels[1])
        self.lachSpinBox.setProperty("value", levels[2])
        self.arcSpinBox.setProperty("value", levels[3])
        self.morSpinBox.setProperty("value", levels[4])
        self.esfSpinBox.setProperty("value", levels[5])

    def getLevels(self):
        return [self.vjSpinBox.value(), self.chuSpinBox.value(), self.lachSpinBox.value(),
                self.arcSpinBox.value(), self.morSpinBox.value(), self.esfSpinBox.value()]

