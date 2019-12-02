# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'skillWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from skillIcon import skillIcon
import json
import os
from Mapler import addDicts

#I hate Combat Orders

class skillController(QtWidgets.QWidget):
    def __init__(self, parent=None, valuesChanged=None):
        super().__init__(parent)
        self.passiveSkills = []
        self.activeSkills = []
        self.activeBoxes = []
        self.passiveFifth = []
        self.passiveFifthSpins = []
        self.activeFifth = []
        self.activeFifthBoxes = []
        self.activeFifthSpins = []
        self.allSkill = 0
        self.co = False #Combat Orders
        self.dco = False #Decent Combat Orders
        self.total = {}
        self.notifyParent = valuesChanged
        self.setupUi()

    def setupUi(self):
        decentJson = open('jobs/DecentPotential.json')
        decentSkills = json.load(decentJson)

        fifthJson = open('jobs/DecentFifth.json')
        fifthSkills = json.load(fifthJson)

        self.resize(510, 335)
        self.setMinimumSize(QtCore.QSize(510, 335))

        #Labels
        self.passiveLabel = QtWidgets.QLabel(self)
        self.passiveLabel.setGeometry(QtCore.QRect(10, 0, 51, 16))
        self.passiveLabel.setStyleSheet("font-size: 14px;")
        self.passiveLabel.setObjectName("passiveLabel")
        self.activeLabel = QtWidgets.QLabel(self)
        self.activeLabel.setGeometry(QtCore.QRect(10, 60, 47, 13))
        self.activeLabel.setStyleSheet("font-size: 14px;")
        self.activeLabel.setObjectName("activeLabel")
        self.decentPotLabel = QtWidgets.QLabel(self)
        self.decentPotLabel.setGeometry(QtCore.QRect(10, 132, 131, 16))
        self.decentPotLabel.setStyleSheet("font-size: 14px;")
        self.decentPotLabel.setObjectName("decentPotLabel")
        self.decentFifthLabel = QtWidgets.QLabel(self)
        self.decentFifthLabel.setGeometry(QtCore.QRect(10, 210, 200, 16))
        self.decentFifthLabel.setStyleSheet("font-size: 14px;")
        self.decentFifthLabel.setObjectName("decentFifthLabel")
        self.tipLabel = QtWidgets.QLabel(self)
        self.tipLabel.setGeometry(QtCore.QRect(10, 308, 411, 41))
        self.tipLabel.setObjectName("tipLabel")
        self.commonLabel = QtWidgets.QLabel(self)
        self.commonLabel.setGeometry(QtCore.QRect(200, 132, 131, 16))
        self.commonLabel.setStyleSheet("font-size: 14px;")
        self.commonLabel.setObjectName("commonLabel")
        #Label Text
        self.passiveLabel.setText("Passives")
        self.activeLabel.setText("Actives")
        self.decentPotLabel.setText("Decent Actives")
        self.decentFifthLabel.setText("Fifth Job Passives")
        self.tipLabel.setText("<html><head/><body><p>*A non-zero value for common skills will apply the passive stat boost.</p></body></html>")
        self.commonLabel.setText("Fifth Job Actives")

        #Passive Skill 1
        # self.pasSkill1 = skillIcon(self)
        # self.pasSkill1.setGeometry(QtCore.QRect(20, 20, 32, 32))
        # self.pasSkill1.setStyleSheet("background-color: rgb(176, 176, 176);")
        # self.pasSkill1.setObjectName("pasSkill1")
        # self.passiveSkills.append(self.pasSkill1)

        #Enable all active skills
        self.allActivesBox = QtWidgets.QCheckBox(self)
        self.allActivesBox.setGeometry(QtCore.QRect(60, 58, 70, 17))
        self.allActivesBox.setObjectName("allActivesBox")
        self.allActivesBox.setText("Enable All")
        self.allActivesBox.stateChanged.connect(self.toggleActives)

        #Active Skill 1
        # self.actSkill1 = skillIcon(self)
        # self.actSkill1.setGeometry(QtCore.QRect(20, 80, 32, 32))
        # self.actSkill1.setStyleSheet("background-color: rgb(176, 176, 176);")
        # self.actSkill1.setObjectName("actSkill1")
        # self.activeSkills.append(self.actSkill1)
        # self.actBox1 = QtWidgets.QCheckBox(self)
        # self.actBox1.setGeometry(QtCore.QRect(28, 114, 16, 17))
        # self.actBox1.setObjectName("actBox1")
        # self.activeBoxes.append(self.actBox1)

        #Sharp Eyes (Potential)
        self.decSeLabel = skillIcon(self)
        self.decSeLabel.setSkill(decentSkills[0]) #Not a fan of just using the index...¯\_(ツ)_/¯
        self.decSeLabel.setGeometry(QtCore.QRect(20, 152, 32, 32))
        self.decSeLabel.setObjectName("decSeLabel")
        self.decSeBox = QtWidgets.QCheckBox(self)
        self.decSeBox.setGeometry(QtCore.QRect(28, 186, 16, 17))
        self.decSeBox.setObjectName("decSeBox")
        self.decSeBox.stateChanged.connect(self.updateTotal)
        
        #Advanced Blessing (Potential)
        self.decAbLabel = skillIcon(self)
        self.decAbLabel.setSkill(decentSkills[1])
        self.decAbLabel.setGeometry(QtCore.QRect(60, 152, 32, 32))
        self.decAbLabel.setObjectName("decAbLabel")
        self.decAbBox = QtWidgets.QCheckBox(self)
        self.decAbBox.setGeometry(QtCore.QRect(68, 186, 16, 17))
        self.decAbBox.setObjectName("decAbBox")
        self.decAbBox.stateChanged.connect(self.updateTotal)

        #Hyper Body (Potential)
        self.decHbLabel = skillIcon(self)
        self.decHbLabel.setSkill(decentSkills[2])
        self.decHbLabel.setGeometry(QtCore.QRect(100, 152, 32, 32))
        self.decHbLabel.setObjectName("decHbLabel")
        self.decHbBox = QtWidgets.QCheckBox(self)
        self.decHbBox.setGeometry(QtCore.QRect(108, 186, 16, 17))
        self.decHbBox.setObjectName("decHbBox")
        self.decHbBox.stateChanged.connect(self.updateTotal)

        #Combat Orders (Potential)
        self.decCoLabel = skillIcon(self)
        self.decCoLabel.setSkill(decentSkills[3])
        self.decCoLabel.setGeometry(QtCore.QRect(140, 152, 32, 32))
        self.decCoLabel.setObjectName("decCoLabel")
        self.decCoBox = QtWidgets.QCheckBox(self)
        self.decCoBox.setGeometry(QtCore.QRect(148, 186, 16, 17))
        self.decCoBox.setObjectName("decCoBox")
        self.decCoBox.stateChanged.connect(self.decentCombatOrders)
        
        #Sharp Eyes (Fifth)
        self.fifthSeLabel = skillIcon(self)
        self.fifthSeLabel.setSkill(fifthSkills[0])
        self.fifthSeLabel.setGeometry(QtCore.QRect(20, 270, 32, 32))
        self.fifthSeLabel.setObjectName("fifthSeLabel")
        self.fifthSeSpin = QtWidgets.QSpinBox(self)
        self.fifthSeSpin.setGeometry(QtCore.QRect(55, 270, 31, 22))
        self.fifthSeSpin.setMaximum(30)
        self.fifthSeSpin.setProperty("value", 0)
        self.fifthSeSpin.setObjectName("fifthSeSpin")
        self.fifthSeSpin.valueChanged.connect(self.updateSkillToolTips)

        #Hyper Body (Fifth)
        self.fifthHbLabel = skillIcon(self)
        self.fifthHbLabel.setSkill(fifthSkills[1])
        self.fifthHbLabel.setGeometry(QtCore.QRect(90, 270, 32, 32))
        self.fifthHbLabel.setObjectName("fifthHbLabel")
        self.fifthHbSpin = QtWidgets.QSpinBox(self)
        self.fifthHbSpin.setGeometry(QtCore.QRect(125, 270, 31, 22))
        self.fifthHbSpin.setMaximum(30)
        self.fifthHbSpin.setProperty("value", 0)
        self.fifthHbSpin.setObjectName("fifthHbSpin")
        self.fifthHbSpin.valueChanged.connect(self.updateSkillToolTips)
        
        #Mystic Door (Fifth)
        self.fifthDoorLabel = skillIcon(self)
        self.fifthDoorLabel.setSkill(fifthSkills[2])
        self.fifthDoorLabel.setGeometry(QtCore.QRect(160, 270, 32, 32))
        self.fifthDoorLabel.setObjectName("fifthDoorLabel")
        # self.fifthDoorBox = QtWidgets.QCheckBox(self)
        # self.fifthDoorBox.setGeometry(QtCore.QRect(168, 264, 16, 17))
        # self.fifthDoorBox.setObjectName("fifthDoorBox")
        self.fifthDoorSpin = QtWidgets.QSpinBox(self)
        self.fifthDoorSpin.setGeometry(QtCore.QRect(195, 270, 31, 22))
        self.fifthDoorSpin.setMaximum(30)
        self.fifthDoorSpin.setProperty("value", 0)
        self.fifthDoorSpin.setObjectName("fifthDoorSpin")
        self.fifthDoorSpin.valueChanged.connect(self.updateSkillToolTips)

        #Blink (Fifth)
        self.fifthBlinkLabel = skillIcon(self)
        self.fifthBlinkLabel.setSkill(fifthSkills[3])
        self.fifthBlinkLabel.setGeometry(QtCore.QRect(230, 270, 32, 32))
        self.fifthBlinkLabel.setObjectName("fifthBlinkLabel")
        # self.fifthBlinkBox = QtWidgets.QCheckBox(self)
        # self.fifthBlinkBox.setGeometry(QtCore.QRect(238, 264, 16, 17))
        # self.fifthBlinkBox.setObjectName("fifthBlinkBox")
        self.fifthBlinkSpin = QtWidgets.QSpinBox(self)
        self.fifthBlinkSpin.setGeometry(QtCore.QRect(265, 270, 31, 22))
        self.fifthBlinkSpin.setMaximum(30)
        self.fifthBlinkSpin.setProperty("value", 0)
        self.fifthBlinkSpin.setObjectName("fifthBlinkSpin")
        self.fifthBlinkSpin.valueChanged.connect(self.updateSkillToolTips)

        #Rope Lift (Fifth)
        self.fifthRopeLabel = skillIcon(self)
        self.fifthRopeLabel.setSkill(fifthSkills[4])
        self.fifthRopeLabel.setGeometry(QtCore.QRect(300, 270, 32, 32))
        self.fifthRopeLabel.setObjectName("fifthRopeLabel")
        # self.fifthRopeBox = QtWidgets.QCheckBox(self)
        # self.fifthRopeBox.setGeometry(QtCore.QRect(308, 264, 16, 17))
        # self.fifthRopeBox.setObjectName("fifthRopeBox")
        self.fifthRopeSpin = QtWidgets.QSpinBox(self)
        self.fifthRopeSpin.setGeometry(QtCore.QRect(335, 270, 31, 22))
        self.fifthRopeSpin.setMaximum(30)
        self.fifthRopeSpin.setProperty("value", 0)
        self.fifthRopeSpin.setObjectName("fifthRopeSpin")
        self.fifthRopeSpin.valueChanged.connect(self.updateSkillToolTips)

        #Speed Infusion (Fifth)
        self.fifthSiLabel = skillIcon(self)
        self.fifthSiLabel.setSkill(fifthSkills[5])
        self.fifthSiLabel.setGeometry(QtCore.QRect(370, 270, 32, 32))
        self.fifthSiLabel.setObjectName("fifthSiLabel")
        # self.fifthSiBox = QtWidgets.QCheckBox(self)
        # self.fifthSiBox.setGeometry(QtCore.QRect(378, 264, 16, 17))
        # self.fifthSiBox.setObjectName("fifthSiBox")
        self.fifthSiSpin = QtWidgets.QSpinBox(self)
        self.fifthSiSpin.setGeometry(QtCore.QRect(405, 270, 31, 22))
        self.fifthSiSpin.setMaximum(30)
        self.fifthSiSpin.setProperty("value", 0)
        self.fifthSiSpin.setObjectName("fifthSiSpin")
        self.fifthSiSpin.valueChanged.connect(self.updateSkillToolTips)
        
        #Common Skill 1
        # self.comSkill1 = skillIcon(self)
        # self.comSkill1.setGeometry(QtCore.QRect(210, 152, 32, 32))
        # self.comSkill1.setStyleSheet("background-color: rgb(176, 176, 176);")
        # self.comSkill1.setObjectName("comSkill1")
        # self.comSpin1 = QtWidgets.QSpinBox(self)
        # self.comSpin1.setGeometry(QtCore.QRect(245, 152, 31, 22))
        # self.comSpin1.setMaximum(30)
        # self.comSpin1.setProperty("value", 0)
        # self.comSpin1.setObjectName("comSpin1")
        # self.comBox1 = QtWidgets.QCheckBox(self)
        # self.comBox1.setGeometry(QtCore.QRect(218, 186, 16, 17))
        # self.comBox1.setObjectName("comBox1")

    def loadJobSkills(self, jobJson):
        jobSkills = jobJson.get("skills")
        # commonVSkills = 
        # commonFile = json.get("common")
        # branchFile = json.get("branch")
        commonFile = open(os.path.join("jobs", jobJson.get("common")))
        branchFile = open(os.path.join("jobs", jobJson.get("branch")))
        commonSkills = json.load(commonFile)
        branchSkills = json.load(branchFile)
        allSkills = jobSkills + commonSkills + branchSkills
        for skill in allSkills:
            if(skill.get("passive") == False and skill.get("fifth")):
                fifth = skillIcon(self)
                fifth.setSkill(skill)
                x = 210 + (70 * len(self.activeFifth))
                fifth.setGeometry(QtCore.QRect(x, 152, 32, 32))
                self.activeFifth.append(fifth)
                box = QtWidgets.QCheckBox(self)
                x += 8
                box.setGeometry(QtCore.QRect(x, 186, 16, 17))
                box.stateChanged.connect(self.updateTotal)
                self.activeFifthBoxes.append(box)
                spin = QtWidgets.QSpinBox(self)
                x += 27
                spin.setGeometry(QtCore.QRect(x, 152, 31, 22))
                spin.setMaximum(30)
                spin.setProperty("value", 0)
                spin.valueChanged.connect(self.updateFifthActives)
                self.activeFifthSpins.append(spin)
            elif(skill.get("fifth")): #is fifth, is passive
                fifth = skillIcon(self)
                fifth.setSkill(skill)
                x = 20 + (40 * len(self.passiveFifth))
                fifth.setGeometry(QtCore.QRect(x, 230, 32, 32))
                self.passiveFifth.append(fifth)
                spin = QtWidgets.QSpinBox(self)
                x += 35
                spin.setGeometry(QtCore.QRect(x, 230, 31, 22))
                spin.setMaximum(30)
                spin.setProperty("value", 0)
                spin.valueChanged.connect(self.updateFifthPassives)
                self.passiveFifthSpins.append(spin)
            else:
                if(skill.get("passive") is True):
                    passive = skillIcon(self)
                    passive.setSkill(skill)
                    x = 20 + (40 * len(self.passiveSkills))
                    passive.setGeometry(QtCore.QRect(x, 20, 32, 32))
                    self.passiveSkills.append(passive)
                else:
                    active = skillIcon(self)
                    active.setSkill(skill)
                    x = 20 + (40 * len(self.activeSkills))
                    active.setGeometry(QtCore.QRect(x, 80, 32, 32))
                    self.activeSkills.append(active)
                    box = QtWidgets.QCheckBox(self)
                    x += 8
                    box.setGeometry(QtCore.QRect(x, 114, 16, 17))
                    if(skill.get("stats")[0].get("ALLSKILLS") is not None):
                        box.stateChanged.connect(self.realCombatOrders)
                    box.stateChanged.connect(self.updateTotal)
                    self.activeBoxes.append(box)

        self.updateTotal()


    #This is awful and I hate everything about it.. thank you combat orders
    def decentCombatOrders(self):
        self.dco = not self.dco
        self.applyCombatOrders()

    def realCombatOrders(self):
        self.co = not self.co
        self.applyCombatOrders()

    #Again, I really hate combat orders
    def applyCombatOrders(self):
        val = self.allSkill
        if(self.co):
            val += 2
        elif(self.dco):
            val += 1
        if(val > 2):
            val = 2
        for skill in self.passiveSkills:
            skill.updateLevel(val)
        for skill in self.activeSkills:
            skill.updateLevel(val)
        self.updateTotal()

    def updateTotal(self):
        self.total.clear()
        for skill in self.passiveSkills:
            self.total = addDicts(self.total, skill.getStats())
        for i in range(0, len(self.activeBoxes)):
            if(self.activeBoxes[i].isChecked()):
                self.total = addDicts(self.total, self.activeSkills[i].getStats())
        for i in range(0, len(self.passiveFifth)):
            if(self.passiveFifthSpins[i].value() > 0):
                self.total = addDicts(self.total, self.passiveFifth[i].getStats())
        for i in range(0, len(self.activeFifth)):
            if(self.activeFifthBoxes[i].isChecked() and self.activeFifthSpins[i].value() > 0):
                self.total = addDicts(self.total, self.activeFifth[i].getStats())
        if(self.decSeBox.isChecked()):
            self.total = addDicts(self.total, self.decSeLabel.getStats())
        if(self.decAbBox.isChecked()):
            self.total = addDicts(self.total, self.decAbLabel.getStats())
        if(self.decHbBox.isChecked()):
            self.total = addDicts(self.total, self.decHbLabel.getStats())
        # if(self.decCoBox.isChecked()):
        #     self.total = addDicts(self.total, self.decCoLabel.getStats())
        if(self.fifthSeSpin.value() > 0):
            self.total = addDicts(self.total, self.fifthSeLabel.getStats())
        if(self.fifthHbSpin.value() > 0):
            self.total = addDicts(self.total, self.fifthHbLabel.getStats())
        if(self.fifthDoorSpin.value() > 0):
            self.total = addDicts(self.total, self.fifthDoorLabel.getStats())
        if(self.fifthBlinkSpin.value() > 0):
            self.total = addDicts(self.total, self.fifthBlinkLabel.getStats())
        if(self.fifthRopeSpin.value() > 0):
            self.total = addDicts(self.total, self.fifthRopeLabel.getStats())
        if(self.fifthSiSpin.value() > 0):
            self.total = addDicts(self.total, self.fifthSiLabel.getStats())
        self.notifyParent()

    def toggleActives(self):
        for box in self.activeBoxes:
            box.setChecked(self.allActivesBox.isChecked())

    def updateFifthActives(self):
        for i in range(0, len(self.activeFifthSpins)):
            skill = self.activeFifth[i]
            spin = self.activeFifthSpins[i]
            skill.updateLevel(spin.value())
            linked = skill.json.get("link_id")
            #Linked means it's one skill that has both a passive and active. 
            #Leveling up one should level up the other for the user.
            if(linked is not None):
                for j in range(0, len(self.passiveFifth)):
                    passive = self.passiveFifth[j]
                    passiveSpin = self.passiveFifthSpins[j]
                    if(linked == passive.json.get("link_id")):
                        passiveSpin.setProperty("value", spin.value())
                        passive.updateLevel(spin.value())
        self.updateTotal()
        

    def updateFifthPassives(self):
        for i in range(0, len(self.passiveFifthSpins)):
            skill = self.passiveFifth[i]
            spin = self.passiveFifthSpins[i]
            skill.updateLevel(spin.value())
            linked = skill.json.get("link_id")
            if(linked is not None):
                for j in range(0, len(self.activeFifth)):
                    active = self.activeFifth[j]
                    activeSpin = self.activeFifthSpins[j]
                    if(linked == active.json.get("link_id")):
                        activeSpin.setProperty("value", spin.value())
                        active.updateLevel(spin.value())
        self.updateTotal()

    def updateSkillToolTips(self):
        self.fifthSeLabel.updateDecentLevel(self.fifthSeSpin.value())
        self.fifthHbLabel.updateDecentLevel(self.fifthHbSpin.value())
        self.fifthDoorLabel.updateDecentLevel(self.fifthDoorSpin.value())
        self.fifthBlinkLabel.updateDecentLevel(self.fifthBlinkSpin.value())
        self.fifthRopeLabel.updateDecentLevel(self.fifthRopeSpin.value())
        self.fifthSiLabel.updateDecentLevel(self.fifthSiSpin.value())
        self.updateTotal()