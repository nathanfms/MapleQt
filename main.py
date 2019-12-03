import sys
import json
from os import path
from DatabaseController import Database
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from mainWindow import mainWindow
from createMapler import createMaplerWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # self.ui = itemInfo(tyrant, parent=self)
        # self.setCentralWidget(self.ui)
        self.setup()

    def setup(self):
        #character.py: parseJson
        self._currentChar = None
        self.setWindowTitle("MapleQt")
        self.center = mainWindow(parent=self)
        self.setCentralWidget(self.center)
        self._db = Database()
        self.createMapler = None
        self.getCharacter()
        self.show()

    def getCharacter(self):
        if(path.exists('maplerId.json')):
            maplerId = json.load(open('maplerid.json')).get('id')
            self._currentChar = self._db.getMapler(maplerId)
            self.center.setupMapler(self._currentChar)
        else:
            self.createMapler = createMaplerWindow(onClick=self.createMaplerDone)
            self.createMapler.show()

    def createMaplerDone(self):
        mapler = {
            'name': self.createMapler.nameEdit.text(),
            'level': int(self.createMapler.levelBox.text()),
            'job': self.createMapler.jobBox.currentText(),
            'equips': [], 
            'symbols': [0, 0, 0, 0, 0, 0], 
            'links': [],
            'legion': [], 
            'hypers': {
                'STR': 0,
                'DEX': 0,
                'INT': 0,
                'LUK': 0,
                'HP': 0,
                'MP': 0,
                'DF': 0,
                'CRITRATE': 0,
                'CRITDMG': 0,
                'IGNORE': 0,
                'DMG': 0,
                'BOSS': 0,
                'ATK': 0,
                'AF': 0
            }
        }
        result = self._db.addMapler(mapler)
        self._currentChar = mapler
        idDict = {'id': str(result), 'warn': 'please do not delete or edit this file'}
        f = open('maplerId.json', 'w')
        f.write(json.dumps(idDict))
        # print("Info: ", mapler.get('name'), mapler.get('level'), mapler.get('job'))
        self.createMapler.close()
        self.center.setupMapler(self._currentChar)

#Maybe make a widget that has them both, then add that widget to the window? this shit crazy
#zetcode.com seems to be your saving grace

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # ex = itemInfo(tyrant)
    window = MainWindow()
    # window.show()

    sys.exit(app.exec_())

