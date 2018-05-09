#encoding=utf-8
import sys
from PyQt5.QtWidgets import (QHBoxLayout,QApplication,QTextBrowser,QMainWindow)
from PyQt5.QtCore import Qt
import time 

class DBserver(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("服务器")
        self.resize(500,200)
        self.tBrowser = QTextBrowser(self)
        self.setCentralWidget(self.tBrowser)
        self.tBrowser.append(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+": "+"message")

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DBserver()
    sys.exit(app.exec_())