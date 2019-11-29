# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createMapler.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class createMaplerWindow(QtWidgets.QWidget):
    def __init__(self, onClick=None, parent=None):
        super().__init__(parent)
        self.onClick = onClick
        print("onClick is ", onClick)
        self.setupUi()

    def setupUi(self):
        self.setWindowFlags(
            QtCore.Qt.WindowStaysOnTopHint
        )
        # Form.setObjectName("Form")
        self.setObjectName("Create Mapler")
        self.resize(240, 208)
        self.setMinimumHeight(208)
        self.setMaximumHeight(208)
        self.setMinimumWidth(240)
        self.setMaximumWidth(240)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 10, 221, 61))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.nameEdit = QtWidgets.QLineEdit(self)
        self.nameEdit.setGeometry(QtCore.QRect(20, 80, 131, 20))
        self.nameEdit.setText("")
        self.nameEdit.setObjectName("nameEdit")
        self.jobBox = QtWidgets.QComboBox(self)
        self.jobBox.setGeometry(QtCore.QRect(20, 110, 201, 22))
        self.jobBox.setObjectName("jobBox")
        for i in range(0, 45):
            self.jobBox.addItem("")
        self.levelBox = QtWidgets.QSpinBox(self)
        self.levelBox.setGeometry(QtCore.QRect(160, 80, 61, 22))
        self.levelBox.setMinimum(100)
        self.levelBox.setMaximum(275)
        self.levelBox.setProperty("value", 250)
        self.levelBox.setObjectName("levelBox")
        self.okButton = QtWidgets.QPushButton(self)
        self.okButton.setGeometry(QtCore.QRect(80, 180, 75, 23))
        self.okButton.setObjectName("okButton")
        
        self.validateWarn = QtWidgets.QLabel(self)
        self.validateWarn.setGeometry(QtCore.QRect(10, 140, 221, 31))
        self.validateWarn.setStyleSheet("color: rgb(255, 0, 0);")
        self.validateWarn.setAlignment(QtCore.Qt.AlignCenter)
        self.validateWarn.setWordWrap(True)
        self.validateWarn.setObjectName("validateWarn")
        self.validateWarn.setText("Please choose a valid job and/or enter a valid name")
        self.validateWarn.hide()

        self.retranslateUi()

        self.okButton.clicked.connect(self.okButtonPressed)
        # QtCore.QMetaObject.connectSlotsByName(Form)

    def okButtonPressed(self):
        if(self.nameEdit.text() == "" or self.jobBox.currentText() == "Job"):
            self.validateWarn.show()
        else:
            self.validateWarn.hide()
            self.onClick()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "form"))
        # Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Hello!\n"" It looks like it\'s your first time using MapleQt. To get started, please enter your IGN, Job, and Level."))
        self.nameEdit.setPlaceholderText(_translate("Form", "IGN"))
        self.jobBox.setItemText(0, _translate("Form", "Job"))
        self.jobBox.setItemText(1, _translate("Form", "Angelic Buster"))
        self.jobBox.setItemText(2, _translate("Form", "Aran"))
        self.jobBox.setItemText(3, _translate("Form", "Ark"))
        self.jobBox.setItemText(4, _translate("Form", "Battle Mage"))
        self.jobBox.setItemText(5, _translate("Form", "Beast Tamer"))
        self.jobBox.setItemText(6, _translate("Form", "Bishop"))
        self.jobBox.setItemText(7, _translate("Form", "Blaster"))
        self.jobBox.setItemText(8, _translate("Form", "Blaze Wizard"))
        self.jobBox.setItemText(9, _translate("Form", "Bowmaster"))
        self.jobBox.setItemText(10, _translate("Form", "Buccaneer"))
        self.jobBox.setItemText(11, _translate("Form", "Cadena"))
        self.jobBox.setItemText(12, _translate("Form", "Cannoneer"))
        self.jobBox.setItemText(13, _translate("Form", "Corsair"))
        self.jobBox.setItemText(14, _translate("Form", "Dark Knight"))
        self.jobBox.setItemText(15, _translate("Form", "Dawn Warrior"))
        self.jobBox.setItemText(16, _translate("Form", "Dual Blade"))
        self.jobBox.setItemText(17, _translate("Form", "Evan"))
        self.jobBox.setItemText(18, _translate("Form", "Fire/Poison"))
        self.jobBox.setItemText(19, _translate("Form", "Hayato"))
        self.jobBox.setItemText(20, _translate("Form", "Hero"))
        self.jobBox.setItemText(21, _translate("Form", "Ho Young"))
        self.jobBox.setItemText(22, _translate("Form", "Ice/Lightning"))
        self.jobBox.setItemText(23, _translate("Form", "Illium"))
        self.jobBox.setItemText(24, _translate("Form", "Jett"))
        self.jobBox.setItemText(25, _translate("Form", "Kaiser"))
        self.jobBox.setItemText(26, _translate("Form", "Kanna"))
        self.jobBox.setItemText(27, _translate("Form", "Kinesis"))
        self.jobBox.setItemText(28, _translate("Form", "Luminous"))
        self.jobBox.setItemText(29, _translate("Form", "Marksman"))
        self.jobBox.setItemText(30, _translate("Form", "Mechanic"))
        self.jobBox.setItemText(31, _translate("Form", "Mercedes"))
        self.jobBox.setItemText(32, _translate("Form", "Mihile"))
        self.jobBox.setItemText(33, _translate("Form", "Night Lord"))
        self.jobBox.setItemText(34, _translate("Form", "Night Walker"))
        self.jobBox.setItemText(35, _translate("Form", "Paladin"))
        self.jobBox.setItemText(36, _translate("Form", "Pathfinder"))
        self.jobBox.setItemText(37, _translate("Form", "Phantom"))
        self.jobBox.setItemText(38, _translate("Form", "Shade"))
        self.jobBox.setItemText(39, _translate("Form", "Shadower"))
        self.jobBox.setItemText(40, _translate("Form", "Thunder Breaker"))
        self.jobBox.setItemText(41, _translate("Form", "Wild Hunter"))
        self.jobBox.setItemText(42, _translate("Form", "Wind Archer"))
        self.jobBox.setItemText(43, _translate("Form", "Xenon"))
        self.jobBox.setItemText(44, _translate("Form", "Zero"))
        self.okButton.setText(_translate("Form", "OK"))
