# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import exportUI
import utils

class exportWin(QWidget,exportUI.Ui_Form):
    '''load show UI '''
    def __init__(self):
        super(exportWin, self).__init__()
        self.prepList = utils.getPreparation()
        self.ActionList = utils.getActionList()
        self.initUi()

    def initUi(self):
        self.setupUi(self)
        self.readPrepList()
        self.readActionList()
        self.qssColor()

    def readPrepList(self):
        self.gpuComboPr.addItems(self.prepList)
        self.heiGeoComboPr.addItems(self.prepList)
        self.geoLoaComboPr.addItems(self.prepList)
        self.lowGeoComboPr.addItems(self.prepList)
        self.abcComboPr.addItems(self.prepList)
        self.bBoxComboPr.addItems(self.prepList)
        self.layoutComboPr.addItems(self.prepList)
        self.comboBox.addItems(self.prepList)
        self.comboBox_2.addItems(self.prepList)
        self.comboBox_3.addItems(self.prepList)

    def readActionList(self):
        self.gpuComboAc.addItems(self.ActionList)
        self.heiGeoComboAc.addItems(self.ActionList)
        self.geoLodComboAc.addItems(self.ActionList)
        self.lowGeoComboAc.addItems(self.ActionList)
        self.abcComboAc.addItems(self.ActionList)
        self.bBoxComboAc.addItems(self.ActionList)
        self.layoutComboAc.addItems(self.ActionList)
        self.comboBox_4.addItems(self.ActionList)
        self.comboBox_5.addItems(self.ActionList)
        self.comboBox_6.addItems(self.ActionList)

    def qssColor(self):
        self.setStyleSheet('QComboBox#gpuComboPr{background-color:rgb(0,200,0)}'
                           'QComboBox#geoLoaComboPr{background-color:rgb(0,200,0)}'
                           'QComboBox#abcComboPr{background-color:rgb(0,200,0)}'
                           'QComboBox#layoutComboPr{background-color:rgb(0,200,0)}'
                           'QComboBox#comboBox_2{background-color:rgb(0,200,0)}'
                           
                           'QComboBox#gpuComboAc{background-color:rgb(0,200,0)}'
                           'QComboBox#geoLodComboAc{background-color:rgb(0,200,0)}'
                           'QComboBox#abcComboAc{background-color:rgb(0,200,0)}'
                           'QComboBox#layoutComboAc{background-color:rgb(0,200,0)}'
                           'QComboBox#comboBox_5{background-color:rgb(0,200,0)}'

                           'QCheckBox#gpuBox{color:rgb(0,150,0)}'
                           'QCheckBox#geoLodBox{color:rgb(0,150,0)}'
                           'QCheckBox#abcBox{color:rgb(0,150,0)}'
                           'QCheckBox#layoutBox{color:rgb(0,150,0)}'
                           'QCheckBox#checkBox_2{color:rgb(0,150,0)}'
                           )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = exportWin()
    win.show()
    sys.exit(app.exec_())
