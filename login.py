#encoding=utf-8
import os,sys
import pymysql
from PyQt5.QtWidgets import (QDesktopWidget,QDialog,QApplication,QGroupBox,QLabel,QLineEdit,QPushButton,QGridLayout)
from PyQt5.QtGui import QFont
from mainWindow import mainWindow
from PyQt5.QtCore import Qt

class loginDialog(QDialog):
    
    def __init__(self):
        super().__init__()  
        self.DBconnect()  
        self.initUI()

    def init_regist(self):
        super().__init__()
        self.DBconnect()
        self.initUI_regist()

    def initUI_regist(self):
        print("注册UI")
        self.setStyleSheet("background-color:rgb(65, 170, 234);")
        self.qgb_regist = QGroupBox('书店销售管理系统',self)
        self.qgb_regist.setFont(QFont("Timers", 8, QFont.Bold))
        self.qgb_regist.setGeometry(25,25,460,310)
        self.qgb_regist.setStyleSheet(
          "QGroupBox"
          "{"
          "border: 1px solid white;"
          "border-radius:8px;"
          "margin-top:6px;"
          "}"
          "QGroupBox:title"
          "{"
          "color:white;"
          "subcontrol-origin: margin;"
          "left: 10px;"
          "}"
          )

        self.UIDLabel = QLabel('输入注册账号')
        self.UPwdLabel = QLabel('请设置密码')
        self.UNameLabel = QLabel('用户名')
        self.USexLabel = QLabel('性别')
        self.UAgeLabel = QLabel('年龄')
        self.UNumberLabel = QLabel('电话号码')

        self.uidEdit = QLineEdit("test123")
        self.pswEdit = QLineEdit("test123")
        self.UNameEdit = QLineEdit("测试用户123")
        self.USexEdit = QLineEdit("男")
        self.UAgeEdit = QLineEdit("50")
        self.UNumberEdit = QLineEdit("18373159713")

        self.uidEdit.setPlaceholderText("不可重复")

        self.registButton = QPushButton("注册")

        self.okButton = QPushButton("登录")
        self.okButton.clicked.connect(self.__init__)
        self.okButton.clicked.connect(self.close)
        self.registerButton = QPushButton("注册")
        self.registerButton.clicked.connect(self.regist)
        self.registerButton.clicked.connect(self.login)

        layout=QGridLayout()
        layout.addWidget(self.UIDLabel,0,0)
        layout.addWidget(self.UPwdLabel,1,0)
        layout.addWidget(self.UNameLabel,2,0)
        layout.addWidget(self.USexLabel,3,0)
        layout.addWidget(self.UAgeLabel,4,0)
        layout.addWidget(self.UNumberLabel,5,0)

        layout.addWidget(self.uidEdit,0,1)
        layout.addWidget(self.pswEdit,1,1)
        layout.addWidget(self.UNameEdit,2,1)
        layout.addWidget(self.USexEdit,3,1)
        layout.addWidget(self.UAgeEdit,4,1)
        layout.addWidget(self.UNumberEdit,5,1)

        layout.addWidget(self.okButton,6,0)
        layout.addWidget(self.registerButton,6,1)

        self.qgb_regist.setLayout(layout)
        self.center()
        self.show()
        
    def initUI(self):
        print("initialing the UI...")
        self.setWindowTitle("login")
        self.setGeometry(300, 300, 510, 360)
        self.setStyleSheet("background-color:rgb(65, 170, 234);")

        self.qgb = QGroupBox('书店销售管理系统',self)
        self.qgb.setFont(QFont("Timers", 8, QFont.Bold))
        self.qgb.setGeometry(25,25,460,310)
        self.qgb.setStyleSheet(
          "QGroupBox"
          "{"
          "border: 1px solid white;"
          "border-radius:8px;"
          "margin-top:6px;"
          "}"
          "QGroupBox:title"
          "{"
          "color:white;"
          "subcontrol-origin: margin;"
          "left: 10px;"
          "}"
          )

        self.lbuid = QLabel('账号')
        self.lbPsw = QLabel('密码')
        self.lbuid.setAlignment(Qt.AlignCenter)
        self.lbPsw.setAlignment(Qt.AlignCenter)

        self.uidEdit = QLineEdit(self.qgb)
        self.uidEdit.setMaximumWidth(200)
        self.uidEdit.setStyleSheet("background-color:rgb(255,255,255)")
        self.uidEdit.setText("admin")
        self.uidEdit.setAlignment(Qt.AlignCenter)

        self.pswEdit = QLineEdit(self.qgb)
        self.pswEdit.setMaximumWidth(200)
        self.pswEdit.setStyleSheet("background-color:rgb(255,255,255)")
        self.pswEdit.setText("admin")
        self.pswEdit.setAlignment(Qt.AlignCenter)

        self.okButton = QPushButton("登录")
        self.okButton.clicked.connect(self.login)
        self.registerButton = QPushButton("注册")
        self.registerButton.clicked.connect(self.close)
        self.registerButton.clicked.connect(self.init_regist)

        self.layout=QGridLayout()
        self.layout.addWidget(self.lbuid,0,0)
        self.layout.addWidget(self.uidEdit,0,1)
        self.layout.addWidget(self.lbPsw,1,0)
        self.layout.addWidget(self.pswEdit,1,1)
        self.layout.addWidget(self.okButton,2,0)
        self.layout.addWidget(self.registerButton,2,1)

        self.qgb.setLayout(self.layout)
        self.center()
        self.show()

    def DBconnect(self):
        self.username = "root"
        self.userpwd = "zjw970815"
        self.dbname = "DBprj" 
        self.db = pymysql.connect("localhost",self.username,self.userpwd,self.dbname,charset="utf8")
        self.cursor = self.db.cursor()
        print("数据库已连接");

    def login(self):
        self.uid = self.uidEdit.text() 
        self.psw = self.pswEdit.text()
        self.sql = 'call login ("'+self.uid+'","'+self.psw+'");'
        self.cursor.execute(self.sql)
        logininfo = self.cursor.fetchone()   
        if logininfo != None:
          self.mw = mainWindow(logininfo,self.db)
          print("验证成功")
          self.close()
        else:
          print("账号密码错误")

    def regist(self):

        UID = self.uidEdit.text()
        UPwd = self.pswEdit.text()
        UName = self.UNameEdit.text()
        USex = self.USexEdit.text()
        UAge = self.UAgeEdit.text()
        UNumber = self.UNumberEdit.text()

        sql = "insert into users values('"+UID+"','"+UPwd+"','"+UName+"','"+USex+"',"+UAge+",'"+UNumber+"',1)"
        print(sql)
        self.cursor.execute(sql)
        self.db.commit()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = loginDialog()
    sys.exit(app.exec_())
