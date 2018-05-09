import sys
from Ewidget import ESearchButton
from PyQt5.QtWidgets import (QLabel,QVBoxLayout,QApplication,QPushButton,QLineEdit)
from PyQt5.QtGui import(QCursor,QIcon)
from functools import partial
from PyQt5.QtCore import Qt
from functools import partial

class headbar(QLabel):
    def __init__(self,id,parent=None):
        super().__init__(parent)

        self.resize(950,60)
        qss = "QLabel{background-color:rgb(52, 164, 232);color:rgb(255, 255, 255);font-size:30px;font-weight:bold;font-family:'Microsoft YaHei',}"
        self.setStyleSheet(qss)
        self.setAlignment(Qt.AlignCenter)
        self.setText("书店管理系统")

        self.SearchEdit = QLineEdit(self)
        self.SearchEdit.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.SearchEdit.setGeometry(700,15,170,30)

        self.SearchButton = ESearchButton.ESearchButton(self)

        self.SearchButton.clicked.connect(partial(parent.searchBook,"开发"))
        self.SearchButton.setGeometry(880,15,30,30)   

        self.show()
