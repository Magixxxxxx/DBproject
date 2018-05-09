import sys
from PyQt5.QtWidgets import (QApplication,QPushButton)
from PyQt5.QtGui import(QCursor,QIcon)
from PyQt5.QtCore import Qt

class ESearchButton(QPushButton):
    def __init__(self,parent=None):
        super().__init__(parent)

        self.setStyleSheet("border-image:url(icon/search)")
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setFlat(True)
        self.show()

    def enterEvent(self,event):
        self.setStyleSheet("border-image:url(icon/searchPressed)")

    def leaveEvent(self,event):
        self.setStyleSheet("border-image:url(icon/search)")