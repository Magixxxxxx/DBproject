import sys
from PyQt5.QtWidgets import (QApplication,QPushButton)
from PyQt5.QtGui import(QCursor,QIcon)
from PyQt5.QtCore import Qt
from functools import partial

class TButton(QPushButton):
    def __init__(self,string,Bid,parent=None):
        super().__init__(string,parent)
        self.Bid = Bid    
        self.show()
        