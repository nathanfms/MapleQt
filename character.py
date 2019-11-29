#Character base stats = class skills and level AP
#Item stats = stats of that item

import json

tyrantStr = """{
	"name": "Tyrant Hyades Belt",
	"type": "BELT",
    "isWep": false,
    "base": {
        "STR": 50,
        "DEX": 50,
        "INT": 50,
        "LUK": 50,
        "ATK": 25,
        "MATK": 25,
        "DEF": 105
    },
	"star": {
		"amount": 2,
		"STR": 39,
		"DEX": 39,
		"INT": 39,
		"LUK": 39,
		"DEF": 12
	},
	"flame": {
		"STR": 888,
		"DEX": 12,
		"ALL": 0.06,
        "BOSS": 0.14
	},
	"mpot": {
		"STR": [
			0.12,
			0.12
		],
        "DEX": 0.09
	},
	"bpot": {
		"STR": 0.03,
		"LUK": 24,
        "ATK": 27
	},
    "soul": {
        "ATK": [
            0.03,
            20
        ]
    }
}"""
tyrant = json.loads(tyrantStr)

"""todo: Make stats() accept a json?"""
class stats():
    def __init__(self):
        self.setup()

    def setup(self):
        self._atk = 0
        self._matk = 0
        self._stre = 0
        self._dex = 0
        self._inte = 0
        self._luk = 0
        self._hp = 0
        self._defe = 0
        self._mp = 0
        self._speed = 0
        self._jump = 0
        self._critRate = 0.0
        self._critDmg = 0.0
        self._finalDmg = 0.0
        self._bossDmg = 0.0
        self._dmg = 0.0
        self._ignore = []
        # p = percentage
        self._all = 0.0
        self._atkp = 0.0
        self._matkp = 0.0
        self._strep = 0.0
        self._dexp = 0.0
        self._intep = 0.0
        self._lukp = 0.0
        self._hpp = 0.0
        self._mpp = 0.0
        self._defep = 0.0

    #Add one stats object to another, returning a new stats object
    def add(self, theOther):
        if(type(theOther) is not stats):
            raise Exception("stats", "stats.add(o) called on unknown object")
        total = stats()
        total.atk = self.atk + theOther.atk
        total.matk = self.matk + theOther.matk
        total.stre = self.stre + theOther.stre
        # print("Total.stre = ", total.stre, " self.stre = ", self.stre, " theOther.stre = ", theOther.stre)
        total.dex = self.dex + theOther.dex
        total.inte = self.inte + theOther.inte
        total.luk = self.luk + theOther.luk
        total.hp = self.hp + theOther.hp
        total.defe = self.defe + theOther.defe
        total.mp = self.mp + theOther.mp
        total.speed = self.speed + theOther.speed
        total.jump = self.jump + theOther.jump
        total.critRate = self.critRate + theOther.critRate
        total.critDmg = self.critDmg + theOther.critDmg
        total.finalDmg = self.finalDmg + theOther.finalDmg
        total.bossDmg = self.bossDmg + theOther.bossDmg
        total.dmg = self.dmg + theOther.dmg
        total.ignore = self.ignore + theOther.ignore
        total.all = self.all + theOther.all
        total.atkp = self.atkp + theOther.atkp
        total.matkp = self.matkp + theOther.matkp
        total.strep = self.strep + theOther.strep
        total.dexp = self.dexp + theOther.dexp
        total.intep = self.intep + theOther.intep
        total.lukp = self.lukp + theOther.lukp
        total.hpp = self.hpp + theOther.hpp
        total.mpp = self.mpp + theOther.mpp
        total.defep = self.defep + theOther.defep
        # print(total.stre)
        return total


    @property
    def atk(self):
        return self._atk

    @atk.setter
    def atk(self, value):
        self._atk += value

    @property
    def matk(self):
        return self._matk

    @matk.setter
    def matk(self, value):
        self._matk += value

    @property
    def stre(self):
        return self._stre

    @stre.setter
    def stre(self, value):
        self._stre += value

    @property
    def dex(self):
        return self._dex

    @dex.setter
    def dex(self, value):
        self._dex += value

    @property
    def inte(self):
        return self._inte

    @inte.setter
    def inte(self, value):
        self._inte += value

    @property
    def luk(self):
        return self._luk

    @luk.setter
    def luk(self, value):
        self._luk += value

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp += value

    @property
    def defe(self):
        return self._defe

    @defe.setter
    def defe(self, value):
        self._defe += value

    @property
    def mp(self):
        return self._mp

    @mp.setter
    def mp(self, value):
        self._mp += value

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed += value

    @property
    def jump(self):
        return self._jump

    @jump.setter
    def jump(self, value):
        self._jump += value

    @property
    def critRate(self):
        return self._critRate

    @critRate.setter
    def critRate(self, value):
        self._critRate += value

    @property
    def critDmg(self):
        return self._critDmg

    @critDmg.setter
    def critDmg(self, value):
        self._critDmg += value

    @property
    def finalDmg(self):
        return self._finalDmg

    @finalDmg.setter
    def finalDmg(self, value):
        self._finalDmg += value

    @property
    def bossDmg(self):
        return self._bossDmg

    @bossDmg.setter
    def bossDmg(self, value):
        self._bossDmg += value

    @property
    def dmg(self):
        return self._dmg

    @dmg.setter
    def dmg(self, value):
        self._dmg += value

    @property
    def ignore(self):
        return self._ignore

    @ignore.setter
    def ignore(self, value):
        self._ignore.append(value)

    @property
    def all(self):
        return round(self._all, 2)

    @all.setter
    def all(self, value):
        self._all += value

    @property
    def atkp(self):
        return round(self._atkp, 2)

    @atkp.setter
    def atkp(self, value):
        self._atkp += value

    @property
    def matkp(self):
        return round(self._matkp, 2)

    @matkp.setter
    def matkp(self, value):
        self._matkp += value

    @property
    def strep(self):
        return round(self._strep, 2)

    @strep.setter
    def strep(self, value):
        self._strep += value

    @property
    def dexp(self):
        return round(self._dexp, 2)

    @dexp.setter
    def dexp(self, value):
        self._dexp += value

    @property
    def intep(self):
        return round(self._inte, 2)

    @inte.setter
    def intep(self, value):
        self._inte += value

    @property
    def lukp(self):
        return round(self._lukp, 2)

    @lukp.setter
    def lukp(self, value):
        self._lukp += value

    @property
    def hpp(self):
        return round(self._hpp, 2)

    @hpp.setter
    def hpp(self, value):
        self._hpp += value

    @property
    def mpp(self):
        return round(self._mpp, 2)

    @mpp.setter
    def mpp(self, value):
        self._mpp += value

    @property
    def defep(self):
        return round(self._defep, 2)

    @defep.setter
    def defep(self, value):
        self._defep += value

class equip():
    def __init__(self, json=None):
        self._json = json
        self._total = stats()
        self._eqpType = None
        self._name = None
        self.setup()

    def setup(self):
        if(self._json is not None):
            self.parseJson()

    def addStat(self, statName, value):
        switcher = {
            "STR": "stre",
            "DEX": "dex",
            "INT": "inte",
            "LUK": "luk",
            "ATK": "atk",
            "MATK": "matk",
            "DEF": "defe",
            "HP": "hp",
            "MP": "mp",
            "SPEED": "speed",
            "JUMP": "jump",
        }
        if(value > 0 and value < 1): #percentage
            switcher = {
                "STR": "strep",
                "DEX": "dexp",
                "INT": "intep",
                "LUK": "lukp",
                "ALL": "all",
                "ATK": "atkp",
                "MATK": "matkp",
                "DEF": "defep",
                "HP": "hpp",
                "MP": "mpp",
                "CRITRATE": "critRate",
                "CRITDMG": "critDmg",
                "FINALDMG": "finalDmg",
                "DMG": "dmg",
                "BOSS": "bossDmg",
                "IGNORE": "ignore",
            }
        if(statName not in switcher.keys()):
            raise Exception("addStat", "No such stat exists")

        #setattr = bad practice??? i am not sure. seems like the most efficient way
        setattr(self.total, switcher[statName], value)

    def isNone(self):
        return self.json is None
    
    def parseJson(self, json=None):
        if(json is not None):
            self.json = json
        if(self.json is None):
            raise Exception('Error', 'equip.json is empty')
        self.eqpType = self.json.get("type")
        self.name = self.json.get("name")
        if(self.json.get("base") is not None):
            for key in self.json.get("base"):
                self.addStat(key, self.json.get("base").get(key))
        if(self.json.get("star") is not None):
            for key in self.json.get("star"):
                if(key != "amount"):
                    self.addStat(key, self.json.get("star").get(key))
        if(self.json.get("flame") is not None):
            for key in self.json.get("flame"):
                self.addStat(key, self.json.get("flame").get(key))
        if(self.json.get("mpot") is not None):
            for key in self.json.get("mpot"):
                if(type(self.json.get("mpot").get(key)) is list):
                    for val in self.json.get("mpot").get(key):
                        self.addStat(key, val)
                else:
                    self.addStat(key, self.json.get("mpot").get(key))
        if(self.json.get("bpot") is not None):
            for key in self.json.get("bpot"):
                if(type(self.json.get("bpot").get(key)) is list):
                    for val in self.json.get("bpot").get(key):
                        self.addStat(key, val)
                else:
                    self.addStat(key, self.json.get("bpot").get(key))
        #Soul in weapon class only

    @property
    def json(self):
        return self._json

    @json.setter
    def json(self, json):
        self._json = json

    @property
    def eqpType(self):
        return self._eqpType

    @eqpType.setter
    def eqpType(self, value):
        self._eqpType = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def total(self):
        return self._total


class weapon(equip):
    def __init__(self, json=None):
        super().__init__(json)
        self.setup()

    def setup(self):
        self._mult = 0

    def parseJson(self, json=None):
        super().parseJson(json)
        if(self.json.get("soul") is not None):
            for key in self.json.get("soul"):
                if(type(self.json.get("soul").get(key)) is list):
                    for val in self.json.get("soul").get(key):
                        self.addStat(key, val)
                else:
                    self.addStat(key, self.json.get("soul").get(key))

    @property
    def mult(self):
        return self._mult

    @mult.setter
    def mult(self, value):
        self._mult = value

class equipList():
    def __init__(self, json=None): #Json will be all equips in the future
        self._json = json
        self._currentlyEquipped = []
        self.setup()

    def setup(self):
        self._ring1 = equip()
        self._ring2 = equip()
        self._ring3 = equip()
        self._ring4 = equip()
        self._pocket = equip()
        self._book = equip()
        self._pend1 = equip()
        self._pend2 = equip()
        self._wep = weapon()
        self._belt = equip()
        self._hat = equip()
        self._face = equip()
        self._eye = equip()
        self._top = equip()
        self._bot = equip()
        self._shoe = equip()
        self._ear = equip()
        self._shoulder = equip()
        self._glove = equip()
        self._droid = equip()
        self._emblem = equip()
        self._badge = equip()
        self._medal = equip()
        self._second = equip()
        self._cape = equip()
        self._heart = equip()
        self._totem1 = equip()
        self._totem2 = equip()
        self._totem3 = equip()
        self._pet1 = equip()
        self._pet2 = equip()
        self._pet3 = equip()

    def parseJson(self, json=None):
        if(json is not None):
            self.json = json
        if(self.json is None):
            raise Exception('Error', 'equip.json is empty')

    #eqp = equip() of equip
    def setEquip(self, eqp):
        #First handle types that you can equip multiple of
        if(eqp.eqpType == "RING"):
            if(self.ring1.isNone()):
                self.ring1 = eqp
                self._currentlyEquipped.append(eqp)
            elif(self.ring2.isNone()):
                self.ring2 = eqp
                self._currentlyEquipped.append(eqp)
            elif(self.ring3.isNone()):
                self.ring3 = eqp
                self._currentlyEquipped.append(eqp)
            elif(self.ring4.isNone()):
                self.ring4 = eqp
                self._currentlyEquipped.append(eqp)
        elif(eqp.eqpType == "PENDANT"):
            if(self.pend1.isNone()):
                self.pend1 = eqp
                self._currentlyEquipped.append(eqp)
            elif(self.pend2.isNone()):
                self.pend2 = eqp
                self._currentlyEquipped.append(eqp)
        elif(eqp.eqpType == "TOTEM"):
            if(self.totem1.isNone()):
                self.totem1 = eqp
                self._currentlyEquipped.append(eqp)
            elif(self.totem2.isNone()):
                self.totem2 = eqp
                self._currentlyEquipped.append(eqp)
            elif(self.totem3.isNone()):
                self.totem3 = eqp
                self._currentlyEquipped.append(eqp)
        elif(eqp.eqpType == "PET"):
            if(self.pet1.isNone()):
                self.pet1 = eqp
                self._currentlyEquipped.append(eqp)
            elif(self.pet2.isNone()):
                self.pet2 = eqp
                self._currentlyEquipped.append(eqp)
            elif(self.pet3.isNone()):
                self.pet3 = eqp
                self._currentlyEquipped.append(eqp)
        elif(type(eqp) is weapon):
            #weapon will have unique type, setattr won't work
            if(self.wep.isNone()):
                self.wep = eqp
                self._currentlyEquipped.append(eqp)
        else:
            #will overwrite equips and mess up currentlyEquipped array
            setattr(self, eqp.eqpType.lower(), eqp)
            self._currentlyEquipped.append(eqp)

    def getTotal(self):
        #disgusting chain adding... i dont know if im okay with this
        total = stats()
        for eqp in self._currentlyEquipped:
            print(eqp.name)
            print(eqp.total.stre)
            total.add(eqp.total)
        print("getTotal(): ", total.stre)
        return total


    @property
    def json(self):
        return self._json

    @json.setter
    def json(self, json):
        self._json = json

    @property
    def ring1(self):
        return self._ring1
    
    @ring1.setter
    def ring1(self, value):
        self._ring1 = value

    @property
    def ring2(self):
        return self._ring2
    
    @ring2.setter
    def ring2(self, value):
        self._ring2 = value

    @property
    def ring3(self):
        return self._ring3
    
    @ring3.setter
    def ring3(self, value):
        self._ring3 = value

    @property
    def ring4(self):
        return self._ring4
    
    @ring4.setter
    def ring4(self, value):
        self._ring4 = value

    @property
    def pocket(self):
        return self._pocket
    
    @pocket.setter
    def pocket(self, value):
        self._pocket = value

    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, value):
        self._book = value

    @property
    def pend1(self):
        return self._pend1
    
    @pend1.setter
    def pend1(self, value):
        self._pend1 = value

    @property
    def pend2(self):
        return self._pend2
    
    @pend2.setter
    def pend2(self, value):
        self._pend2 = value

    @property
    def wep(self):
        return self._wep
    
    @wep.setter
    def wep(self, value):
        self._wep = value

    @property
    def belt(self):
        return self._belt
    
    @belt.setter
    def belt(self, value):
        self._belt = value

    @property
    def hat(self):
        return self._hat
    
    @hat.setter
    def hat(self, value):
        self._hat = value

    @property
    def face(self):
        return self._
    
    @face.setter
    def face(self, value):
        self._face = value

    @property
    def eye(self):
        return self._eye
    
    @eye.setter
    def eye(self, value):
        self._eye = value

    @property
    def top(self):
        return self._top
    
    @top.setter
    def top(self, value):
        self._top = value

    @property
    def bot(self):
        return self._bot
    
    @bot.setter
    def bot(self, value):
        self._bot = value

    @property
    def shoe(self):
        return self._shoe
    
    @shoe.setter
    def shoe(self, value):
        self._shoe = value

    @property
    def ear(self):
        return self._ear
    
    @ear.setter
    def ear(self, value):
        self._ear = value

    @property
    def shoulder(self):
        return self._shoulder
    
    @shoulder.setter
    def shoulder(self, value):
        self._shoulder = value

    @property
    def glove(self):
        return self._glove
    
    @glove.setter
    def glove(self, value):
        self._glove = value

    @property
    def droid(self):
        return self._droid
    
    @droid.setter
    def droid(self, value):
        self._droid = value

    @property
    def emblem(self):
        return self._emblem
    
    @emblem.setter
    def emblem(self, value):
        self._emblem = value

    @property
    def emblem(self):
        return self._emblem
    
    @emblem.setter
    def emblem(self, value):
        self._emblem = value

    @property
    def badge(self):
        return self._badge
    
    @badge.setter
    def badge(self, value):
        self._badge = value

    @property
    def medal(self):
        return self._medal
    
    @medal.setter
    def medal(self, value):
        self._medal = value

    @property
    def second(self):
        return self._second
    
    @second.setter
    def second(self, value):
        self._second = value

    @property
    def cape(self):
        return self._cape
    
    @cape.setter
    def cape(self, value):
        self._cape = value

    @property
    def heart(self):
        return self._heart
    
    @heart.setter
    def heart(self, value):
        self._heart = value

    @property
    def totem1(self):
        return self._totem1
    
    @totem1.setter
    def totem1(self, value):
        self._totem1 = value

    @property
    def totem2(self):
        return self._totem2
    
    @totem2.setter
    def totem2(self, value):
        self._totem2 = value

    @property
    def totem3(self):
        return self._totem3
    
    @totem3.setter
    def totem3(self, value):
        self._totem3 = value

    @property
    def pet1(self):
        return self._pet1
    
    @pet1.setter
    def pet1(self, value):
        self._pet1 = value

    @property
    def pet2(self):
        return self._pet2
    
    @pet2.setter
    def pet2(self, value):
        self._pet2 = value

    @property
    def pet3(self):
        return self._pet3
    
    @pet3.setter
    def pet3(self, value):
        self._pet3 = value

class mapler():
    def __init__(self, name=None, level=0, job=None):
        self._name = name
        self._level = level
        self._job = job
        self.setup()

    def setup(self):
        self.skillStats = stats()
        self.baseAp = stats()
        #Set base AP here according to job. Special Cases = Xenon, Demon Avenger
        self.hypers = stats()
        self.link = stats()
        self.legionBoard = stats()
        self.legionChars = stats()
        self.equips = equipList()
        self.symbols = stats()

    def getStats(self):
        #just chain adding everything. Looks pretty nasty fam
        equipTotal = self.equips.getTotal()
        subtotal = self.symbols.add(self.legionChars.add(self.legionBoard.add(self.link.add(self.hypers.add(self.skillStats.add(self.baseAp))))))
        return equipTotal.add(subtotal)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        self._job = value
        


m = mapler(name="Rooshy", level=240, job="Paladin")
e = equip(tyrant)
m.equips.setEquip(e)
print(m.getStats().stre)

# e = weapon()
# e.parseJson(json=tyrant)
# # e.addStat("STR", 20)
# # e.addStat("STR", 0.12)
# print(e.total.atk)
# print(e.total.atkp)