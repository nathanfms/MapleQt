# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stats.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class statsController(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        # Form.setObjectName("Form")
        labelStyle = "background-color: rgb(180, 255, 16); border-radius: 10px; border: 2px solid black; qproperty-alignment: AlignCenter;"
        modStyle = "border-radius: 10px; border: 2px solid black; qproperty-alignment: AlignCenter;background-color: rgb(79, 238, 238);"
        entryStyle = "background-color: rgb(255, 255, 255);border-radius: 10px; border: 1px solid black; qproperty-alignment: 'AlignVCenter | AlignLeft';"

        self.resize(321, 341)
        self.name_label = QtWidgets.QLabel(self)
        self.name_label.setGeometry(QtCore.QRect(0, 0, 71, 31))
        self.name_label.setStyleSheet(labelStyle)
        self.name_label.setText("Name")
        self.level_label = QtWidgets.QLabel(self)
        self.level_label.setGeometry(QtCore.QRect(210, 30, 71, 31))
        self.level_label.setStyleSheet(labelStyle)
        self.level_label.setText("Level")
        self.job_label = QtWidgets.QLabel(self)
        self.job_label.setGeometry(QtCore.QRect(180, 0, 41, 31))
        self.job_label.setStyleSheet(labelStyle)
        self.job_label.setText("Job")
        self.matk_label = QtWidgets.QLabel(self)
        self.matk_label.setGeometry(QtCore.QRect(0, 90, 71, 31))
        self.matk_label.setStyleSheet(labelStyle)
        self.matk_label.setText("M.ATK")
        self.atk_label = QtWidgets.QLabel(self)
        self.atk_label.setGeometry(QtCore.QRect(0, 60, 71, 31))
        self.atk_label.setStyleSheet(labelStyle)
        self.atk_label.setText("ATK")
        self.str_label = QtWidgets.QLabel(self)
        self.str_label.setGeometry(QtCore.QRect(0, 120, 71, 31))
        self.str_label.setStyleSheet(labelStyle)
        self.str_label.setText("STR")
        self.dex_label = QtWidgets.QLabel(self)
        self.dex_label.setGeometry(QtCore.QRect(0, 150, 71, 31))
        self.dex_label.setStyleSheet(labelStyle)
        self.dex_label.setText("DEX")
        self.int_label = QtWidgets.QLabel(self)
        self.int_label.setGeometry(QtCore.QRect(0, 180, 71, 31))
        self.int_label.setStyleSheet(labelStyle)
        
        self.int_label.setText("INT")
        self.luk_label = QtWidgets.QLabel(self)
        self.luk_label.setGeometry(QtCore.QRect(0, 210, 71, 31))
        self.luk_label.setStyleSheet(labelStyle)
        
        self.luk_label.setText("LUK")
        self.name_entry = QtWidgets.QLabel(self)
        self.name_entry.setGeometry(QtCore.QRect(70, 0, 111, 31))
        self.name_entry.setStyleSheet(entryStyle)
        
        self.hp_label = QtWidgets.QLabel(self)
        self.hp_label.setGeometry(QtCore.QRect(0, 250, 71, 31))
        self.hp_label.setStyleSheet(labelStyle)
        
        self.hp_label.setText("HP")
        self.mp_label = QtWidgets.QLabel(self)
        self.mp_label.setGeometry(QtCore.QRect(0, 310, 71, 31))
        self.mp_label.setStyleSheet(labelStyle)
        
        self.mp_label.setText("MP")
        self.def_label = QtWidgets.QLabel(self)
        self.def_label.setGeometry(QtCore.QRect(0, 280, 71, 31))
        self.def_label.setStyleSheet(labelStyle)
        
        self.def_label.setText("DEF")
        self.speed_label = QtWidgets.QLabel(self)
        self.speed_label.setGeometry(QtCore.QRect(180, 280, 71, 31))
        self.speed_label.setStyleSheet(labelStyle)
        
        self.speed_label.setText("SPEED")
        self.jump_label = QtWidgets.QLabel(self)
        self.jump_label.setGeometry(QtCore.QRect(180, 310, 71, 31))
        self.jump_label.setStyleSheet(labelStyle)
        
        self.jump_label.setText("JUMP")
        self.job_entry = QtWidgets.QLabel(self)
        self.job_entry.setGeometry(QtCore.QRect(220, 0, 101, 31))
        self.job_entry.setStyleSheet(entryStyle)
        
        self.level_entry = QtWidgets.QLabel(self)
        self.level_entry.setGeometry(QtCore.QRect(280, 30, 41, 31))
        self.level_entry.setStyleSheet(entryStyle)
        
        self.atk_entry = QtWidgets.QLabel(self)
        self.atk_entry.setGeometry(QtCore.QRect(70, 60, 111, 31))
        self.atk_entry.setStyleSheet(entryStyle)
        
        self.int_entry = QtWidgets.QLabel(self)
        self.int_entry.setGeometry(QtCore.QRect(70, 180, 111, 31))
        self.int_entry.setStyleSheet(entryStyle)
        
        self.str_entry = QtWidgets.QLabel(self)
        self.str_entry.setGeometry(QtCore.QRect(70, 120, 111, 31))
        self.str_entry.setStyleSheet(entryStyle)
        
        self.matk_entry = QtWidgets.QLabel(self)
        self.matk_entry.setGeometry(QtCore.QRect(70, 90, 111, 31))
        self.matk_entry.setStyleSheet(entryStyle)
        
        self.dex_entry = QtWidgets.QLabel(self)
        self.dex_entry.setGeometry(QtCore.QRect(70, 150, 111, 31))
        self.dex_entry.setStyleSheet(entryStyle)
        
        self.luk_entry = QtWidgets.QLabel(self)
        self.luk_entry.setGeometry(QtCore.QRect(70, 210, 111, 31))
        self.luk_entry.setStyleSheet(entryStyle)
        
        self.hp_entry = QtWidgets.QLabel(self)
        self.hp_entry.setGeometry(QtCore.QRect(70, 250, 111, 31))
        self.hp_entry.setStyleSheet(entryStyle)
        
        self.def_entry = QtWidgets.QLabel(self)
        self.def_entry.setGeometry(QtCore.QRect(70, 280, 111, 31))
        self.def_entry.setStyleSheet(entryStyle)
        
        self.mp_entry = QtWidgets.QLabel(self)
        self.mp_entry.setGeometry(QtCore.QRect(70, 310, 111, 31))
        self.mp_entry.setStyleSheet(entryStyle)
        
        self.atk_mod = QtWidgets.QLabel(self)
        self.atk_mod.setGeometry(QtCore.QRect(130, 60, 51, 31))
        self.atk_mod.setStyleSheet(modStyle)
        
        self.matk_mod = QtWidgets.QLabel(self)
        self.matk_mod.setGeometry(QtCore.QRect(130, 90, 51, 31))
        self.matk_mod.setStyleSheet(modStyle)
        
        self.str_mod = QtWidgets.QLabel(self)
        self.str_mod.setGeometry(QtCore.QRect(130, 120, 51, 31))
        self.str_mod.setStyleSheet(modStyle)
        
        self.dex_mod = QtWidgets.QLabel(self)
        self.dex_mod.setGeometry(QtCore.QRect(130, 150, 51, 31))
        self.dex_mod.setStyleSheet(modStyle)
        
        self.int_mod = QtWidgets.QLabel(self)
        self.int_mod.setGeometry(QtCore.QRect(130, 180, 51, 31))
        self.int_mod.setStyleSheet(modStyle)
        
        self.luk_mod = QtWidgets.QLabel(self)
        self.luk_mod.setGeometry(QtCore.QRect(130, 210, 51, 31))
        self.luk_mod.setStyleSheet(modStyle)
        
        self.def_mod = QtWidgets.QLabel(self)
        self.def_mod.setGeometry(QtCore.QRect(130, 280, 51, 31))
        self.def_mod.setStyleSheet(modStyle)
        
        self.hp_mod = QtWidgets.QLabel(self)
        self.hp_mod.setGeometry(QtCore.QRect(130, 250, 51, 31))
        self.hp_mod.setStyleSheet(modStyle)
        
        self.mp_mod = QtWidgets.QLabel(self)
        self.mp_mod.setGeometry(QtCore.QRect(130, 310, 51, 31))
        self.mp_mod.setStyleSheet(modStyle)
        
        self.ignore_label = QtWidgets.QLabel(self)
        self.ignore_label.setGeometry(QtCore.QRect(180, 210, 81, 31))
        self.ignore_label.setStyleSheet(labelStyle)
        
        self.ignore_label.setText("IGNORE")
        self.bossdmg_label = QtWidgets.QLabel(self)
        self.bossdmg_label.setGeometry(QtCore.QRect(180, 180, 81, 31))
        self.bossdmg_label.setStyleSheet(labelStyle)
        
        self.bossdmg_label.setText("BOSS DMG")
        self.dmg_label = QtWidgets.QLabel(self)
        self.dmg_label.setGeometry(QtCore.QRect(180, 150, 81, 31))
        self.dmg_label.setStyleSheet(labelStyle)
        
        self.dmg_label.setText("DMG")
        self.critrate_label = QtWidgets.QLabel(self)
        self.critrate_label.setGeometry(QtCore.QRect(180, 60, 81, 31))
        self.critrate_label.setStyleSheet(labelStyle)
        
        self.critrate_label.setText("CRIT RATE")
        self.finaldmg_label = QtWidgets.QLabel(self)
        self.finaldmg_label.setGeometry(QtCore.QRect(180, 120, 81, 31))
        self.finaldmg_label.setStyleSheet(labelStyle)
        
        self.finaldmg_label.setText("FINAL DMG")
        self.critdmg_label = QtWidgets.QLabel(self)
        self.critdmg_label.setGeometry(QtCore.QRect(180, 90, 81, 31))
        self.critdmg_label.setStyleSheet(labelStyle)
        
        self.critdmg_label.setText("CRIT DMG")
        self.critrate_entry = QtWidgets.QLabel(self)
        self.critrate_entry.setGeometry(QtCore.QRect(260, 60, 61, 31))
        self.critrate_entry.setStyleSheet(entryStyle)
        
        self.critdmg_entry = QtWidgets.QLabel(self)
        self.critdmg_entry.setGeometry(QtCore.QRect(260, 90, 61, 31))
        self.critdmg_entry.setStyleSheet(entryStyle)
        
        self.finaldmg_entry = QtWidgets.QLabel(self)
        self.finaldmg_entry.setGeometry(QtCore.QRect(260, 120, 61, 31))
        self.finaldmg_entry.setStyleSheet(entryStyle)
        
        self.dmg_entry = QtWidgets.QLabel(self)
        self.dmg_entry.setGeometry(QtCore.QRect(260, 150, 61, 31))
        self.dmg_entry.setStyleSheet(entryStyle)
        
        self.bossdmg_entry = QtWidgets.QLabel(self)
        self.bossdmg_entry.setGeometry(QtCore.QRect(260, 180, 61, 31))
        self.bossdmg_entry.setStyleSheet(entryStyle)
        
        self.ignore_entry = QtWidgets.QLabel(self)
        self.ignore_entry.setGeometry(QtCore.QRect(260, 210, 61, 31))
        self.ignore_entry.setStyleSheet(entryStyle)
        
        self.speed_entry = QtWidgets.QLabel(self)
        self.speed_entry.setGeometry(QtCore.QRect(250, 280, 61, 31))
        self.speed_entry.setStyleSheet(entryStyle)
        
        self.jump_entry = QtWidgets.QLabel(self)
        self.jump_entry.setGeometry(QtCore.QRect(250, 310, 61, 31))
        self.jump_entry.setStyleSheet(entryStyle)
        
        self.range = QtWidgets.QLabel(self)
        self.range.setGeometry(QtCore.QRect(0, 30, 211, 31))
        self.range.setStyleSheet("background-color: rgb(255, 255, 255);border-radius: 10px; border: 1px solid black; qproperty-alignment:AlignCenter; font-size: 11pt;")
        
        self.range.setText("999,999,999 ~ 999,999,999")

        # self.retranslateUi()
        # QtCore.QMetaObject.connectSlotsByName(Form)

    def update(self, json=None):
        if(json is None):
            return
        allStat = json.get('ALLp')
        if(allStat == None):
            allStat = 0

        self.stre = json.get('STR')
        self.strep = json.get('STRp')
        self.dex = json.get('DEX')
        self.dexp = json.get('DEXp')
        self.inte = json.get('INT')
        self.intep = json.get('INTp')
        self.luk = json.get('LUK')
        self.lukp = json.get('LUKp')
        self.atk = json.get('ATK')
        self.atkp = json.get('ATKp')
        self.matk = json.get('MATK')
        self.matkp = json.get('MATKp')
        self.hp = json.get('HP')
        self.hpp = json.get('HPp')
        self.mp = json.get('MP')
        self.mpp = json.get('MPp')
        self.defe = json.get('DEF')
        self.defep = json.get('DEFp')
        self.speed = json.get('SPEED')
        self.jump = json.get('JUMP')
        self.critRate = json.get('CRITRATE')
        self.critDmg = json.get('CRITDMG')
        self.finalDmg = json.get('FINALDMG')
        self.bossDmg = json.get('BOSSp')
        self.dmg = json.get('DMG')
        self.ignore = json.get('IGNORE')

        self.strep += allStat
        self.dexp += allStat
        self.intep += allStat
        self.lukp += allStat

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self.name_entry.setText(self.name)

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        self._job = value
        self.job_entry.setText(self.job)

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
        self.level_entry.setText(str(self.level))

    @property
    def atk(self):
        return self._atk

    @atk.setter
    def atk(self, value):
        if(value == None):
            value = 0
        self._atk = value
        self.atk_entry.setText(str(self.atk))

    @property
    def matk(self):
        return self._matk

    @matk.setter
    def matk(self, value):
        if(value == None):
            value = 0
        self._matk = value
        self.matk_entry.setText(str(self.matk))

    @property
    def stre(self):
        return self._stre

    @stre.setter
    def stre(self, value):
        if(value == None):
            value = 4
        self._stre = value
        self.str_entry.setText(str(self.stre))

    @property
    def dex(self):
        return self._dex

    @dex.setter
    def dex(self, value):
        if(value == None):
            value = 4
        self._dex = value
        self.dex_entry.setText(str(self.dex))

    @property
    def inte(self):
        return self._inte

    @inte.setter
    def inte(self, value):
        if(value == None):
            value = 4
        self._inte = value
        self.int_entry.setText(str(self.inte))

    @property
    def luk(self):
        return self._luk

    @luk.setter
    def luk(self, value):
        if(value == None):
            value = 4
        self._luk = value
        self.luk_entry.setText(str(self.luk))

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        if(value == None):
            value = 50
        self._hp = value
        self.hp_entry.setText(str(self.hp))

    @property
    def defe(self):
        return self._defe

    @defe.setter
    def defe(self, value):
        if(value == None):
            value = 0
        self._defe = value
        self.def_entry.setText(str(self.defe))

    @property
    def mp(self):
        return self._mp

    @mp.setter
    def mp(self, value):
        if(value == None):
            value = 50
        self._mp = value
        self.mp_entry.setText(str(self.mp))

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if(value == None):
            value = 100
        self._speed = value
        self.speed_entry.setText(str(self.speed))

    @property
    def jump(self):
        return self._jump

    @jump.setter
    def jump(self, value):
        if(value == None):
            value = 100
        self._jump = value
        self.jump_entry.setText(str(self.jump))

    @property
    def critRate(self):
        return self._critRate

    @critRate.setter
    def critRate(self, value):
        if(value == None):
            value = 0.05
        self._critRate = value
        self.critrate_entry.setText('{:.0%}'.format(self.critRate))

    @property
    def critDmg(self):
        return self._critDmg

    @critDmg.setter
    def critDmg(self, value):
        if(value == None):
            value = 0
        self._critDmg = value
        self.critdmg_entry.setText('{:.2%}'.format(self.critDmg))

    @property
    def finalDmg(self):
        return self._finalDmg

    @finalDmg.setter
    def finalDmg(self, value):
        if(value == None):
            value = 0
        self._finalDmg = value
        self.finaldmg_entry.setText('{:.0%}'.format(self.finalDmg))

    @property
    def bossDmg(self):
        return self._bossDmg

    @bossDmg.setter
    def bossDmg(self, value):
        if(value == None):
            value = 0
        self._bossDmg = value
        self.bossdmg_entry.setText('{:.0%}'.format(self.bossDmg))

    @property
    def dmg(self):
        return self._dmg

    @dmg.setter
    def dmg(self, value):
        if(value == None):
            value = 0
        self._dmg = value
        self.dmg_entry.setText('{:.0%}'.format(self.dmg))

    @property
    def ignore(self):
        return self._ignore

    @ignore.setter
    def ignore(self, value):
        if(value == None):
            value = 0
        self._ignore = value
        self.ignore_entry.setText('{:.0%}'.format(self.ignore))

    @property
    def atkp(self):
        return self._atkp

    @atkp.setter
    def atkp(self, value):
        if(value == None):
            value = 0
        self._atkp = value
        self.atk_mod.setText('{:.0%}'.format(self.atkp))

    @property
    def matkp(self):
        return self._matkp

    @matkp.setter
    def matkp(self, value):
        if(value == None):
            value = 0
        self._matkp = value
        self.matk_mod.setText('{:.0%}'.format(self.matkp))

    @property
    def strep(self):
        return self._strep

    @strep.setter
    def strep(self, value):
        if(value == None):
            value = 0
        self._strep = value
        self.str_mod.setText('{:.0%}'.format(self.strep))

    @property
    def dexp(self):
        return self._dexp

    @dexp.setter
    def dexp(self, value):
        if(value == None):
            value = 0
        self._dexp = value
        self.dex_mod.setText('{:.0%}'.format(self.dexp))

    @property
    def intep(self):
        return self._inte

    @inte.setter
    def intep(self, value):
        if(value == None):
            value = 0
        self._inte = value
        self.int_mod.setText('{:.0%}'.format(self.intep))

    @property
    def lukp(self):
        return self._lukp

    @lukp.setter
    def lukp(self, value):
        if(value == None):
            value = 0
        self._lukp = value
        self.luk_mod.setText('{:.0%}'.format(self.lukp))

    @property
    def hpp(self):
        return self._hpp

    @hpp.setter
    def hpp(self, value):
        if(value == None):
            value = 0
        self._hpp = value
        self.hp_mod.setText('{:.0%}'.format(self.hpp))

    @property
    def mpp(self):
        return self._mpp

    @mpp.setter
    def mpp(self, value):
        if(value == None):
            value = 0
        self._mpp = value
        self.mp_mod.setText('{:.0%}'.format(self.mpp))

    @property
    def defep(self):
        return self._defep

    @defep.setter
    def defep(self, value):
        if(value == None):
            value = 0
        self._defep = value
        self.def_mod.setText('{:.0%}'.format(self.defep))
    

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        # Form.setWindowTitle(_translate("Form", "Form"))
        self.name_label.setText(_translate("Form", "Name"))
        self.level_label.setText(_translate("Form", "Level"))
        self.job_label.setText(_translate("Form", "Job"))
        self.matk_label.setText(_translate("Form", "M.ATK"))
        self.atk_label.setText(_translate("Form", "ATK"))
        self.str_label.setText(_translate("Form", "STR"))
        self.dex_label.setText(_translate("Form", "DEX"))
        self.int_label.setText(_translate("Form", "INT"))
        self.luk_label.setText(_translate("Form", "LUK"))
        self.name_entry.setText(_translate("Form", "XXXXXXXXXXXXXXX"))
        self.hp_label.setText(_translate("Form", "HP"))
        self.mp_label.setText(_translate("Form", "MP"))
        self.def_label.setText(_translate("Form", "DEF"))
        self.speed_label.setText(_translate("Form", "SPEED"))
        self.jump_label.setText(_translate("Form", "JUMP"))
        self.job_entry.setText(_translate("Form", "Long Ass Job Name"))
        self.level_entry.setText(_translate("Form", "276"))
        self.atk_entry.setText(_translate("Form", "15613"))
        self.int_entry.setText(_translate("Form", "#val"))
        self.str_entry.setText(_translate("Form", "#val"))
        self.matk_entry.setText(_translate("Form", "#val"))
        self.dex_entry.setText(_translate("Form", "#val"))
        self.luk_entry.setText(_translate("Form", "#val"))
        self.hp_entry.setText(_translate("Form", "#val"))
        self.def_entry.setText(_translate("Form", "99,999"))
        self.mp_entry.setText(_translate("Form", "#val"))
        self.atk_mod.setText(_translate("Form", "999%"))
        self.matk_mod.setText(_translate("Form", "999%"))
        self.str_mod.setText(_translate("Form", "999%"))
        self.dex_mod.setText(_translate("Form", "999%"))
        self.int_mod.setText(_translate("Form", "999%"))
        self.luk_mod.setText(_translate("Form", "999%"))
        self.def_mod.setText(_translate("Form", "999%"))
        self.hp_mod.setText(_translate("Form", "999%"))
        self.mp_mod.setText(_translate("Form", "999%"))
        self.ignore_label.setText(_translate("Form", "IGNORE%"))
        self.bossdmg_label.setText(_translate("Form", "BOSS DMG%"))
        self.dmg_label.setText(_translate("Form", "DAMAGE%"))
        self.critrate_label.setText(_translate("Form", "CRIT. RATE%"))
        self.finaldmg_label.setText(_translate("Form", "FINAL DMG%"))
        self.critdmg_label.setText(_translate("Form", "CRIT. DMG%"))
        self.critrate_entry.setText(_translate("Form", "999%"))
        self.critdmg_entry.setText(_translate("Form", "999%"))
        self.finaldmg_entry.setText(_translate("Form", "999%"))
        self.dmg_entry.setText(_translate("Form", "999%"))
        self.bossdmg_entry.setText(_translate("Form", "999%"))
        self.ignore_entry.setText(_translate("Form", "999%"))
        self.speed_entry.setText(_translate("Form", "999%"))
        self.jump_entry.setText(_translate("Form", "999%"))
        self.range.setText(_translate("Form", "999,999,999 ~ 999,999,999"))
