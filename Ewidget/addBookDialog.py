import sys
from PyQt5.QtWidgets import (QTextEdit,QGridLayout,QDialog,QApplication,QLabel,QLineEdit,QComboBox,QPushButton,QDesktopWidget)
from PyQt5.QtGui import (QFont)

class addBookDialog(QDialog):
    
    def __init__(self,parent = None):
        super().__init__(parent)
        #输入付款方式，运送方式
        self.BookInfo = []
        self.resize(300,300)
        self.center()
        self.setWindowTitle("输入书籍信息")

        self.BookIDLabel = QLabel("书号",self)
        self.BNameLabel = QLabel("书名",self)
        self.BTypeLabel = QLabel("种类",self)
        self.BAuthorLabel = QLabel("作者",self)
        self.BPubLabel = QLabel("出版社",self)
        self.BPriceLabel = QLabel("定价",self)
        self.BNumLabel = QLabel("数量",self)
        self.BInfoLabel = QLabel("简介",self)

        self.BookIDEdit = QLineEdit("12345678",self)
        self.BNameEdit = QLineEdit("论自由",self)
        self.BTypeEdit = QLineEdit("HS102",self)
        self.BAuthorEdit = QLineEdit("密尔",self)
        self.BPubEdit = QLineEdit("三联出版社",self)
        self.BPriceEdit = QLineEdit("18.88",self)
        self.BNumEdit = QLineEdit("20",self)
        self.BInfoEdit = QTextEdit("空",self)

        self.okButton = QPushButton("ok",self)
        self.cancleButton = QPushButton("cancle",self)
        self.okButton.clicked.connect(self.setBookInfo)
        self.cancleButton.clicked.connect(self.cancle)

        layout=QGridLayout()
        layout.addWidget(self.BookIDLabel,0,0)
        layout.addWidget(self.BTypeLabel,1,0)
        layout.addWidget(self.BNameLabel,2,0)
        layout.addWidget(self.BAuthorLabel,3,0)    
        layout.addWidget(self.BPubLabel,4,0)    
        layout.addWidget(self.BPriceLabel,5,0)    
        layout.addWidget(self.BNumLabel,6,0)
        layout.addWidget(self.BInfoLabel,7,0)

        layout.addWidget(self.BookIDEdit,0,1)
        layout.addWidget(self.BTypeEdit,1,1)
        layout.addWidget(self.BNameEdit,2,1)
        layout.addWidget(self.BAuthorEdit,3,1)    
        layout.addWidget(self.BPubEdit,4,1)    
        layout.addWidget(self.BPriceEdit,5,1)
        layout.addWidget(self.BNumEdit,6,1)
        layout.addWidget(self.BInfoEdit,7,1)

        layout.addWidget(self.okButton,8,0)    
        layout.addWidget(self.cancleButton,8,1)    

        self.setLayout(layout)
        self.show()

    def setBookInfo(self):      
        self.BookInfo.append(self.BookIDEdit.text())#0
        self.BookInfo.append(self.BTypeEdit.text())#1
        self.BookInfo.append(self.BNameEdit.text())#2
        self.BookInfo.append(self.BAuthorEdit.text())#3
        self.BookInfo.append(self.BPubEdit.text())#4
        self.BookInfo.append(self.BPriceEdit.text())#5
        self.BookInfo.append(self.BNumEdit.text())#6
        self.BookInfo.append(self.BInfoEdit.toPlainText())#7
        self.close()

    def cancle(self):
        self.close()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        


