#encoding=utf-8
import os,time
import sys,leftbar,booktable,headbar,footbar,avater
from Ewidget import addBookDialog,payDialog
from PyQt5.QtWidgets import (QMessageBox,QMainWindow,QPushButton,QApplication,QTableWidget,QDesktopWidget)
from PyQt5.QtCore import Qt
from decimal import Decimal

class mainWindow(QMainWindow):

    def __init__(self,logininfo,connect):
        super().__init__()
        self.logininfo = logininfo
        self.curUser = self.logininfo[0]
        self.setWindowTitle(self.logininfo[3])
        self.connect = connect
        self.cursor = connect.cursor()
        self.setGeometry(300, 150, 1200, 550)
        self.setFixedSize(1200,550)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet("")
##左上头像
        self.AvaterButton = avater.avater(self.logininfo[2],self)
        self.AvaterButton.move(0,0)
##左边栏
        self.lfb = leftbar.leftbar(self.logininfo[6],self)            
##右上头
        self.headBar("store")
##右中表
        self.rightTable("store")
##右下选项
        self.footBar("store")
        self.center()
        self.show()

    def headBar(self,id):
        self.hb = headbar.headbar(id,self)
        self.hb.move(250,0)       

    def footBar(self,id):
        self.fb = footbar.footbar(id,self)
        self.fb.move(250,480)

    def rightTable(self,id):
        self.bktb = booktable.Etable(20,6,self.cursor,id,self)
        self.bktb.move(250,60)

    def searchBook(self,keyword):
        print(keyword)
        self.keyword = keyword
        self.rightTable("search")
        print("搜索书籍")

    def addToCart(self,info):  
        sql = "select BookID from books where BName = '"+info+"' "
        self.cursor.execute(sql)
        sql = "call addToCart('"+self.cursor.fetchone()[0]+"','"+self.logininfo[0]+"');"
        print(sql)
        self.cursor.execute(sql)
        self.connect.commit()

    def deleteCart(self,info):
        sql = "select BookID from books where BName = '"+info+"' "
        self.cursor.execute(sql)
        print(sql)
        sql = "DELETE FROM carts where BookID = '"+self.cursor.fetchone()[0]+"' AND CusID = '"+self.logininfo[0]+"'"
        self.cursor.execute(sql)
        self.connect.commit()
        self.rightTable("cart")

    def payAll(self):
        #获取购买的书籍信息
        sql = "call searchCart('"+self.logininfo[0]+"');"
        self.cursor.execute(sql)

        payBookID = []
        payPrice = []
        payNum = []
        totalPrices = Decimal.from_float(0.00)

        while True:
            CartInfo=self.cursor.fetchone()
            if CartInfo == None:
                break
            payBookID.append(CartInfo[0])
            payNum.append(CartInfo[5])
            payPrice.append(CartInfo[4]*CartInfo[5])
            totalPrices += CartInfo[4]*CartInfo[5]
        #检查余量合法
        for i in range(len(payBookID)):
            sql = "select BName,BStock from books where BookID = '"+ payBookID[i] +"'"
            self.cursor.execute(sql)
            message = self.cursor.fetchone()
            if(message[1] < payNum[i]):
                QMessageBox.critical(self,"Critical",self.tr("库存不足(《"+message[0]+"》仅剩 "+str(message[1])+" 本)!"))
                return
        print("库存检查通过")
        #减少相应库存
        for i in range(len(payBookID)):
            sql = "update books set BStock = BStock - "+str(payNum[i])+" where BookID = '"+ payBookID[i] + "'"
            self.cursor.execute(sql)
        #付款信息输入
        self.payDialog = payDialog.payDialog(totalPrices,self)
        self.payDialog.exec_()

        payTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        payType = self.payDialog.payInfo[0]
        deliverType = self.payDialog.payInfo[1]

        #插入消费记录
        for i in range(len(payBookID)):
            sql = "insert into records values(null,'"+payBookID[i]+"','"+self.curUser+"','"+payTime+"',"+str(payNum[i])+","+str(payPrice[i])+",'"+payType+"','"+deliverType+"')"
            self.cursor.execute(sql)
        #清空购物车
        sql = "delete from carts where CusID = '"+ self.curUser +"'"
        self.cursor.execute(sql)
        
        #提交
        self.connect.commit()
        self.rightTable("cart")

    def addBook(self):
        addBookD = addBookDialog.addBookDialog(self)     
        addBookD.exec_()
        BookInfo = addBookD.BookInfo
        sql = "insert into books values('"+BookInfo[0]+"','"+BookInfo[1]+"','"+BookInfo[2]+"','"+BookInfo[3]+"','"+BookInfo[4]+"',"+BookInfo[5]+","+BookInfo[6]+",'空','"+BookInfo[7]+"')"
        print(sql)
        self.cursor.execute(sql)
        self.connect.commit()
        self.rightTable("manage")

    def deleteBook(self,info):
        sql = "select BookID from books where BName = '"+info+"'"
        self.cursor.execute(sql)
        print(sql)
        sql = "DELETE FROM books where BookID = '"+self.cursor.fetchone()[0]+"'"
        self.cursor.execute(sql)
        self.connect.commit()
        self.rightTable("manage")

    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_drag=True
            self.m_DragPosition=event.globalPos()-self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() and Qt.LeftButton:
            self.move(QMouseEvent.globalPos()-self.m_DragPosition)
            QMouseEvent.accept()
 
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag=False

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mainWindow("0","0")
    sys.exit(app.exec_())