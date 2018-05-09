import sys
from PyQt5.QtWidgets import (QLabel,QVBoxLayout,QApplication,QPushButton,QTextEdit)
from PyQt5.QtGui import(QIcon)
from functools import partial
class footbar(QLabel):
    def __init__(self,id,parent=None):
        super().__init__(parent)
        self.resize(950,70)
        self.setStyleSheet("background-color:rgb(220, 220, 220)")

        if id == "store":
            self.EIcon = QIcon("icon/search")
            self.EButton = QPushButton(self.EIcon,"购物车",self)
            self.EButton.setGeometry(850,0,100,70)
            self.EButton.setStyleSheet("background-color:rgb(52, 164, 232)")
            self.EButton.clicked.connect(partial(parent.rightTable,"cart"))
            self.EButton.clicked.connect(partial(parent.footBar,"cart"))
        elif id == "cart":
            self.EIcon = QIcon("icon/search")
            self.EButton = QPushButton(self.EIcon,"结算",self)
            self.EButton.setGeometry(850,0,100,70)
            self.EButton.setStyleSheet("background-color:rgb(52, 164, 232)")
            self.EButton.clicked.connect(parent.payAll)

        elif id == "manage":
            self.EIcon = QIcon("icon/search")
            self.EButton = QPushButton(self.EIcon,"添加",self)
            self.EButton.setGeometry(850,0,100,70)
            self.EButton.setStyleSheet("background-color:rgb(52, 164, 232)") 
            self.EButton.clicked.connect(parent.addBook)
            
        elif id == "record":
            pass

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = footbar()
    sys.exit(app.exec_())