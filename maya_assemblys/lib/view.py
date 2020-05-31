# _*_ coding: utf-8 _*_
# @Time      : 5/31/2020 11:27 PM
# @author    : zuokangbo
# @eamil     : 1156298563@qq.com
# @File      : view.py
# @software  : PyCharm
import sys

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import lib

class LibUi(QDialog, lib.Ui_Dialog):
    def __init__(self):
        super(LibUi, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Assembly AssetsLib')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    UI = LibUi()
    UI.show()
    exit(app.exec_())