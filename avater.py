import sys
from PyQt5.QtWidgets import (QLabel,QVBoxLayout,QApplication,QPushButton,QTextEdit)
from PyQt5.QtGui import(QCursor,QIcon)
from functools import partial
from PyQt5.QtCore import Qt

class avater(QLabel):
    def __init__(self,id,parent=None):
        super().__init__(parent)

        self.resize(250,70)
        self.setStyleSheet("background-color:rgb(59, 112, 170);")
        self.name = QLabel(id,self)
        self.name.move(120,35)
        self.avButton = QPushButton(self)
        self.avButton.setGeometry(15,5,60,60);
        self.avButton.setStyleSheet("border-image:url(icon/avater)")
        self.avButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = avater("test")
    sys.exit(app.exec_())
