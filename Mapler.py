import json
from Equip import Equip
from DatabaseController import Database
#Inventory locally stored, everything else in DB?

def addDicts(dict1, dict2):
    return { key: dict1.get(key, 0) + dict2.get(key, 0)
                    for key in set(dict1) | set(dict2) }

class Mapler(Equip):
    def __init__(self, json=None):
        super().__init__(json)

    #will load everything about this mapler. From DB?
    def parseJson(self):
        self._db = Database()
        self._name = self.json.get("name")
        self._job = self.json.get("job")
        self._level = self.json.get("level")
        self._equipIds = self.json.get("equips")
        self._equips = {}
        self._skills = {}
        self._links = self.json.get("links")
        self._legion = self.json.get("legion")
        self._hypers = self.json.get("hypers")
        self._symbols = self.json.get("symbols")
        self._invIds = self.json.get("inventory")
        self._inventory = {}

        self._statInfo = self.getStatInfo()

        self.load()

    def load(self):
        #equips
        for key,val in self.equipIds.items():
            eqpJson = self.db.getEquip(val)
            e = Equip(json=eqpJson)
            e.recalcTotal()
            self.equips.update({key : e})
        #links
        #legion
        #symbols
        #hypers
        #inventory
        for item in self._invIds:
            #(row, col) = id
            eqp = Equip(self.db.getEquip(item.get('id')))
            self.inventory.update({ (item.get('row'), item.get('col')) : eqp })

    def addEquip(self, equip):
        #Returns none if nothing needs to be swapped
        itemType = equip.eqpType
        if(itemType == 'PENDANT'):
            itemType = self.getOpenPendSlot()
        alreadyInSlot = self.equips.get(itemType.lower())
        self.equips.update( {itemType.lower() : equip} )
        if(alreadyInSlot is not None):
            return itemType

    def removeEquip(self, equipType):
        self.equips.pop(equipType)

    """
    Changing 1 item should not have to recalculate EVERYTHING!
    """
    def getTotal(self):
        total = {"ALL": 4, "HP": 50, "CRITRATEp": 0.05, "SPEED": 100, "JUMP": 100} #Base stats
        if(type(self.statInfo.get('main')) is not list): #Xenon's will have to change their base AP manually
            total.update({self.statInfo.get('main') : 14 + int(self.level) * 5})
        eqpTotal = self.updateStatsByEqp()
        symTotal = self.updateStatsBySymbols()

        # total = { key: total.get(key, 0) + eqpTotal.get(key, 0)
        #             for key in set(total) | set(eqpTotal) }
        total = addDicts(total, eqpTotal)
        total = addDicts(total, symTotal)
        total = addDicts(total, self.skills)
        return total
        # self._baseStats.update(statInfo.get('main') = 14 * self.level * 5)

    #Update my total stats from equipment list
    def updateStatsByEqp(self):
        total = {}
        for key in self.equips:
            eqp = self.equips.get(key)
            # total = { key: total.get(key, 0) + eqp.total.get(key, 0)
            #         for key in set(total) | set(eqp.total) }
            total = addDicts(total, eqp.total)
        return total

    #Link Skills
    def updateStatsByLinks(self):
        pass

    #Legion Board + Legion Chars
    def updateStatsByLegion(self):
        pass

    #Hyper AP
    def updateStatsByHypers(self):
        pass

    #Base AP
    def updateStatsByBase(self):
        pass
    
    #Skills
    def updateStatsBySkills(self):
        pass

    #Symbols
    def updateStatsBySymbols(self):
        stats = {}
        total = 0
        mainStat = self.statInfo.get('main')
        for val in self.symbols:
            if(val != 0):
                if(type(mainStat) is list): #Xenon
                    for stat in mainStat:
                        stats.update({stat : 78 + (39 * val)})
                else:
                    total += 200 + (100 * val)
                    stats.update({mainStat : total})
        return stats

    #Get main / secondary stat information related to job
    def getStatInfo(self):
        info = {
            'Angelic Buster': {
                'main': 'DEX',
                'sec': 'STR'
            },
            'Aran': {
                'main': 'STR',
                'sec': 'DEX'
            },
            'Ark': {
                'main': 'STR',
                'sec': 'DEX'
            },
            'Battle Mage': {
                'main': 'INT',
                'sec': 'LUK'
            },
            'Beast Tamer': {
                'main': 'INT',
                'sec': 'LUK'
            },
            'Bishop': {
                'main': 'INT',
                'sec': 'LUK'
            },
            'Blaster': {
                'main': 'STR',
                'sec': 'DEX'
            },
            'Blaze Wizard': {
                'main': 'INT',
                'sec': 'LUK'
            },
            'Bowmaster': {
                'main': 'DEX',
                'sec': 'STR'
            },
            'Buccaneer': {
                'main': 'STR',
                'sec': 'DEX'
            },
            'Cadena': {
                'main': 'LUK',
                'sec': ['DEX', 'STR']
            },
            'Cannoneer': {
                'main': 'STR',
                'sec': 'DEX'
            },
            'Corsair': {
                'main': 'DEX',
                'sec': 'STR'
            },
            'Dark Knight': {
                'main': 'STR',
                'sec': 'DEX'
            },
            'Dawn Warrior': {
                'main': 'STR',
                'sec': 'DEX'
            },
            'Dual Blade': {
                'main': 'LUK',
                'sec': ['DEX', 'STR']
            },
            'Evan': {
                'main': 'INT',
                'sec': 'LUK'
            },
            'Fire/Poison': {
                'main': 'INT',
                'sec': 'LUK'
            },
            'Hayato': {
                'main': 'STR',
                'sec': 'DEX'
            },
            'Hero': {
                'main': 'STR',
                'sec': 'DEX'
            },
            'Ho Young': {
                'main': 'LUK',
                'sec': 'DEX'
            },
            'Ice/Lightning': {
                'main': 'INT',
                'sec': 'LUK'
            },
            'Illium': {
                'main': 'INT',
                'sec': 'LUK'
            },
            'Jett': {
                'main': 'DEX',
                'sec': 'STR'
            },
            'Kaiser': {
                'main': 'STR',
                'sec': 'DEX'
            },
            'Kanna': {
                'main': 'INT',
                'sec': 'LUK'
            },
            'Kinesis': {
                'main': 'INT',
                'sec': 'LUK'
            },
            'Luminous': {
                'main': 'INT',
                'sec': 'LUK'
            },
            'Marksman': {
                'main': 'DEX',
                'sec': 'STR'
            },
            'Mechanic': {
                'main': 'DEX',
                'sec': 'STR'
            },
            'Mercedes': {
                'main': 'DEX',
                'sec': 'STR'
            },
            'Mihile': {
                'main': 'STR',
                'sec': 'DEX'
            },
            'Night Lord': {
                'main': 'LUK',
                'sec': 'DEX'
            },
            'Night Walker': {
                'main': 'LUK',
                'sec': 'DEX'
            },
            'Paladin': {
                'main': 'STR',
                'sec': 'DEX'
            },
            'Pathfinder': {
                'main': 'DEX',
                'sec': 'STR'
            },
            'Phantom': {
                'main': 'LUK',
                'sec': 'DEX'    
            },
            'Shade': {
                'main': 'STR',
                'sec': 'DEX'
            },
            'Shadower': {
                'main': 'LUK',
                'sec': ['DEX', 'STR']
            },
            'Thunder Breaker': {
                'main': 'STR',
                'sec': 'DEX'
            },
            'Wild Hunter': {
                'main': 'DEX',
                'sec': 'STR'
            },
            'Wind Archer': {
                'main': 'DEX',
                'sec': 'STR'
            },
            'Xenon': {
                'main': ['STR', 'DEX', 'LUK'],
                'sec': None
            },
            'Zero': {
                'main': 'STR',
                'sec': 'DEX'    
            }
        }
        return info.get(self.job)

    def getOpenRingSlot(self):
        if(self.equips.get('ring4') is None):
            return 'ring4'
        if(self.equips.get('ring3') is None):
            return 'ring3'
        if(self.equips.get('ring2') is None):
            return 'ring2'
        if(self.equips.get('ring1') is None):
            return 'ring1'
        #Swap ring4 if they're all full
        return 'ring4'

    def getOpenPendSlot(self):
        if(self.equips.get('pend1') is None):
            return 'pend1'
        if(self.equips.get('pend2') is None):
            return 'pend2'
        #Swap pend1 if they're both full
        return 'pend1'

    def getOpenTotemSlot(self):
        if(self.equips.get('totem1') is None):
            return 'totem1'
        if(self.equips.get('totem2') is None):
            return 'totem2'
        if(self.equips.get('totem3') is None):
            return 'totem3'
        #Swap totem1 if they're both full
        return 'totem1'

    def getOpenPetSlot(self):
        if(self.equips.get('pet1') is None):
            return 'pet1'
        if(self.equips.get('pet2') is None):
            return 'pet2'
        if(self.equips.get('pet3') is None):
            return 'pet3'
        #Swap pet1 if they're all full
        return 'pet1'

    @property
    def db(self):
        return self._db

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        self._job = value

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value

    #Contains just the object ID of the equip. Obtained from DB
    @property
    def equipIds(self):
        return self._equipIds

    #Contains the complete equip JSONs
    @property
    def equips(self):
        return self._equips

    @property
    def symbols(self):
        return self._symbols

    @symbols.setter
    def symbols(self, value):
        self._symbols = value

    @property
    def inventory(self):
        return self._inventory

    @property
    def statInfo(self):
        return self._statInfo

    @property
    def skills(self):
        return self._skills

    @skills.setter
    def skills(self, value):
        self._skills = value

