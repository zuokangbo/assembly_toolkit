# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import exportUI

class exportWin(QWidget,exportUI.Ui_Form):
    '''load show UI '''
    def __init__(self):
        super(exportWin, self).__init__()
        self.initUi()

    def initUi(self):
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = exportWin()
    win.show()
    sys.exit(app.exec_())
