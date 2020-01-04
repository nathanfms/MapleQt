import json

class Equip():
    def __init__(self, json=None):
        self._json = json
        self._id = None
        self.setup()

    def setup(self):
        if(self.json is not None):
            self.parseJson()
        else:
            self._base = {}
            self._star = {}
            self._flame = {}
            self._mpot = {}
            self._bpot = {}
            self._soul = {}
            self._total = {}
        
    def parseJson(self):
        self._name = self.json.get("name")
        self._eqpType = self.json.get("type")
        self._base = self.json.get("base")
        self._star = self.json.get("star")
        self._flame = self.json.get("flame")
        self._mpot = self.json.get("mpot")
        self._bpot = self.json.get("bpot")
        self._soul = self.json.get("soul")
        self._total = {}
        #     "STR": 0,
        #     "DEX": 0,
        #     "INT": 0,
        #     "LUK": 0,
        #     "ATK": 0,
        #     "MATK": 0,
        #     "HP": 0,
        #     "DEF": 0,
        #     "MP": 0,
        #     "SPEED": 0,
        #     "JUMP": 0,
        #     #p = percentage value
        #     "CRITRATEp": 0,
        #     "CRITDMGp": 0,
        #     "FINALDMGp": 0,
        #     "BOSSDMGp": 0,
        #     "DMGp": 0,
        #     #Ignore must be calculated differently; 
        #     #100 - (100 * ((1 - i)/100) *((1 - i+1)/100) * ... ((1 - n)/100))
        #     "IGNORE": [],
        #     "ALLp": 0,
        #     "ATKp": 0,
        #     "MATKp": 0,
        #     "STRp": 0,
        #     "DEXp": 0,
        #     "INTp": 0,
        #     "LUKp": 0,
        #     "HPp": 0,
        #     "MPp": 0,
        #     "DEFp": 0

    def recalcTotal(self):
        self.total.clear()
        self.addToTotal(self.base)
        self.addToTotal(self.star)
        self.total.pop("amount", None)
        self.addToTotal(self.flame)
        self.addToTotal(self.mpot)
        self.addToTotal(self.bpot)
        self.addToTotal(self.soul)


    #addingFrom = One of [base, star, flame, mpot, bpot, soul]
    def addToTotal(self, addingFrom):
        if(addingFrom is None):
            return
        for key in addingFrom:
            val = addingFrom.get(key)
            if(type(val) is list):
                val = sum(val)
            # if(key == "IGNORE"):
            #     if(self.total.get("IGNORE") is None):
            #         self.total.update( {"IGNORE" : []} )
            #     self.total.get("IGNORE").append(val)
            elif(val > 0 and val < 1): #percentage
                curr = self.total.get(key + 'p')
                keyp = key + 'p'
                if(curr is None):
                    curr = 0
                self.total.update( {keyp : curr + val} )
            else:
                curr = self.total.get(key)
                if(curr is None):
                    curr = 0
                self.total.update( {key : curr + val} )
                
    @property
    def json(self):
        return self._json

    @json.setter
    def json(self, value):
        self._json = value
        self.parseJson()

    @property
    def total(self):
        return self._total

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = str(value)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def eqpType(self):
        return self._eqpType

    @eqpType.setter
    def eqpType(self, value):
        self._eqpType = value

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, value):
        self._base = value

    @property
    def star(self):
        return self._star

    @star.setter
    def star(self, value):
        self._star = value

    @property
    def flame(self):
        return self._flame

    @flame.setter
    def flame(self, value):
        self._flame = value

    @property
    def mpot(self):
        return self._mpot

    @mpot.setter
    def mpot(self, value):
        self._mpot = value

    @property
    def bpot(self):
        return self._bpot

    @bpot.setter
    def bpot(self, value):
        self._bpot = value

    @property
    def soul(self):
        return self._soul

    @soul.setter
    def soul(self, value):
        self._soul = value
    
#Weapons are the exact same as Equips, except for having a damage multiplier.
class Weapon(Equip):
    def __init__(self, json=None):
        super().__init__(json)

    def parseJson(self):
        super().parseJson(self)
        self._mult = 0

    @property
    def mult(self):
        return self._mult

    @mult.setter
    def mult(self, value):
        self._mult = value

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
        "ATK": 0.069
    }
}"""
tyrant = json.loads(tyrantStr)

# e = Equip(tyrant)
# e.recalcTotal()
# print(e.total)