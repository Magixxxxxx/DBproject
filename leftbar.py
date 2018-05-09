#encoding=utf-8
import sys
from PyQt5.QtWidgets import (QVBoxLayout,QLabel,QApplication,QPushButton)
from PyQt5.QtGui import(QIcon)
from functools import partial
class leftbar(QLabel):
    def __init__(self,identity,parent=None):
 
        super().__init__(parent)
        self.setStyleSheet("background-color:rgb(65, 170, 234);")    
        self.setGeometry(0,70,250,480)   
        ##菜单
        MenuStyle = "QPushButton{background-color:rgb(65, 170, 234);color:#ffffff;font-size:15px;}QPushButton:h0over{background-color:#333333;}"

        height = 0
        if(identity == 0):
            height = 50;
            icon_bookmanage = QIcon("icon/manage")
            self.qpb_bookmanage = QPushButton(icon_bookmanage,u"仓库管理(管理员)",self)
            self.qpb_bookmanage.setGeometry(0,0,250,50)
            self.qpb_bookmanage.setStyleSheet(MenuStyle)
            self.qpb_bookmanage.clicked.connect(partial(parent.rightTable,"manage"))
            self.qpb_bookmanage.clicked.connect(partial(parent.headBar,"manage"))
            self.qpb_bookmanage.clicked.connect(partial(parent.footBar,"manage"))
            self.qpb_bookmanage.setCheckable(True)
            self.qpb_bookmanage.setAutoExclusive(True)

        icon_market = QIcon("icon/store")
        self.qpb_market = QPushButton(icon_market,u"书籍购买",self)
        self.qpb_market.setGeometry(0,height,250,50)
        self.qpb_market.setStyleSheet(MenuStyle)
        self.qpb_market.clicked.connect(partial(parent.rightTable,"store"))
        self.qpb_market.clicked.connect(partial(parent.headBar,"store"))
        self.qpb_market.clicked.connect(partial(parent.footBar,"store"))
        self.qpb_market.setCheckable(True)
        self.qpb_market.setAutoExclusive(True)

        icon_cart = QIcon("icon/cart")
        self.qpb_cart = QPushButton(icon_cart,u"购物车",self)
        self.qpb_cart.setGeometry(0,height+50,250,50)
        self.qpb_cart.setStyleSheet(MenuStyle)
        self.qpb_cart.clicked.connect(partial(parent.rightTable,"cart"))
        self.qpb_cart.clicked.connect(partial(parent.headBar,"cart"))
        self.qpb_cart.clicked.connect(partial(parent.footBar,"cart"))
        self.qpb_cart.setCheckable(True)
        self.qpb_cart.setAutoExclusive(True)

        icon_record = QIcon("icon/record")
        self.qpb_record = QPushButton(icon_record,u"消费记录",self)
        self.qpb_record.setGeometry(0,height+50*2,250,50)
        self.qpb_record.setStyleSheet(MenuStyle)
        self.qpb_record.clicked.connect(partial(parent.rightTable,"record"))
        self.qpb_record.clicked.connect(partial(parent.headBar,"record"))
        self.qpb_record.clicked.connect(partial(parent.footBar,"record"))
        self.qpb_record.setCheckable(True)
        self.qpb_record.setAutoExclusive(True)

        icon_quit = QIcon("icon/exit")
        self.qpb_quit = QPushButton(icon_quit,u"退出系统",self)
        self.qpb_quit.setGeometry(0,height+50*3,250,50)
        self.qpb_quit.setStyleSheet(MenuStyle)
        self.qpb_quit.clicked.connect(parent.close)       
        self.qpb_quit.setCheckable(True)
        self.qpb_quit.setAutoExclusive(True)

        self.show()