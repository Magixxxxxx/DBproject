#encoding=utf-8
import sys
from Ewidget import TButton
from PyQt5.QtWidgets import (QPushButton,QApplication,QTableWidget,QTableWidgetItem,QAbstractItemView)
from functools import partial
class Etable(QTableWidget):

    def setInfo(self,id):
        self.Info = self.item(id,0).text()  #书名信息
     #  self.Info.append(self.item(id,0).text())   #购买数量
        self.parent.addToCart(self.Info)

    def setDeleteCartInfo(self,id):
        self.Info = self.item(id,0).text()
        self.parent.deleteCart(self.Info)

    def setDeleteBookInfo(self,id):
        self.Info = self.item(id,0).text()
        self.parent.deleteBook(self.Info)

    def __init__(self,height,width,cursor,id="store",parent=None):
        super().__init__(height,width,parent)
        self.parent=parent
        self.resize(950,420)
        self.setStyleSheet("")
        self.cursor = cursor
        self.h=0
        self.Info = []
        self.setColumnWidth(0,250)
        self.setColumnWidth(1,120)
        self.setColumnWidth(2,150)
        self.setColumnWidth(3,100)
        self.setColumnWidth(4,100)
        self.setColumnWidth(5,175)
        self.setSelectionBehavior(QAbstractItemView.SelectRows);#整行选取
        self.setAlternatingRowColors(True)#间隔换色
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)#禁止编辑

        if id == "store":
            self.h=0
            self.setHorizontalHeaderLabels(['书名','作者','出版社','价格','存量','添加到购物车'])
            self.sql = 'select * from books'
            self.cursor.execute(self.sql)          
            while True:
                BookInfo=self.cursor.fetchone()
                if BookInfo == None:
                    break
                #按钮设置
                store_button = TButton.TButton("+1",self.h,self)
                store_button.clicked.connect(partial(self.setInfo,store_button.Bid))
                #表格设置
                            
                for i in range(5):
                    item = QTableWidgetItem(str(BookInfo[i+2]))
                    self.setItem(self.h,i,item)
                self.setCellWidget(self.h,5,store_button)
                self.h+=1

        elif id == "manage":
            self.h=0
            self.setHorizontalHeaderLabels(['书名','作者','出版社','价格','存量','删除条目'])
            self.sql = 'select * from books'
            self.cursor.execute(self.sql)

            while True:
                delete_button = QPushButton("X")
                BookInfo=self.cursor.fetchone()
                if BookInfo == None:
                    break       
                deleteBook_button = TButton.TButton("删除",self.h,self)
                deleteBook_button.clicked.connect(partial(self.setDeleteBookInfo,deleteBook_button.Bid))       
                for i in range(5):
                    item = QTableWidgetItem(str(BookInfo[i+2]))
                    self.setItem(self.h,i,item)
                self.setCellWidget(self.h,5,deleteBook_button)
                self.h+=1

        elif id == "cart":
            self.setHorizontalHeaderLabels(['书名','作者','出版社','价格','购买量','删除选项'])
            self.h=0
            self.sql = "call searchCart('"+parent.logininfo[0]+"');"
            self.cursor.execute(self.sql)
            while True:
                CartInfo=self.cursor.fetchone()
                if CartInfo == None:
                    break 
                deleteCart_button = TButton.TButton("删除",self.h,self)
                deleteCart_button.clicked.connect(partial(self.setDeleteCartInfo,deleteCart_button.Bid))
                for i in range(5):
                    item = QTableWidgetItem(str(CartInfo[i+1]))
                    self.setItem(self.h,i,item)
                self.setCellWidget(self.h,5,deleteCart_button)
                self.h+=1
        
        elif id == "record":
            self.setColumnWidth(0,250)
            self.setColumnWidth(1,195)
            self.setColumnWidth(2,150)
            self.setColumnWidth(3,100)
            self.setColumnWidth(4,100)
            self.setColumnWidth(5,100)
            self.h=0
            self.setHorizontalHeaderLabels(['图书名称','日期','数量','付款','付款方式','发货方式'])
            self.sql = "select BName,RDate,Num,RProfit,RType_Pay,RType_Deliver from books,records where books.BookID = records.BookID AND CusID ='"+parent.logininfo[0]+"';"
            self.cursor.execute(self.sql)
            while True:
                BookInfo=self.cursor.fetchone()
                if BookInfo == None:
                    break              
                for i in range(6):
                    item = QTableWidgetItem(str(BookInfo[i]))
                    self.setItem(self.h,i,item)
                self.h+=1

        elif id == "search":

            self.h=0
            self.setHorizontalHeaderLabels(['书名','作者','出版社','价格','存量','添加到购物车'])
            self.sql = "select * from books where BName like '%"+ self.parent.keyword +"%' ;"
            print(self.sql)
            self.cursor.execute(self.sql)          
            while True:
                BookInfo=self.cursor.fetchone()
                if BookInfo == None:
                    break
                #按钮设置
                store_button = TButton.TButton("+1",self.h,self)
                store_button.clicked.connect(partial(self.setInfo,store_button.Bid))
                #表格设置
                            
                for i in range(5):
                    item = QTableWidgetItem(str(BookInfo[i+2]))
                    self.setItem(self.h,i,item)
                self.setCellWidget(self.h,5,store_button)
                self.h+=1

        self.show()

