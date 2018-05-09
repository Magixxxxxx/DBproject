import sys
from PyQt5.QtWidgets import (QGridLayout,QDialog,QApplication,QLabel,QLineEdit,QComboBox,QPushButton,QDesktopWidget)
from PyQt5.QtGui import (QFont)

class payDialog(QDialog):
    
    def __init__(self,totalPrices,parent = None):
        super().__init__(parent)
        #输入付款方式，运送方式
        self.payInfo = []
        self.resize(200,200)
        self.center()
        self.setWindowTitle("请选择付款信息")

        self.aLabel = QLabel("应付款项",self)
        self.priceLabel = QLabel(str(totalPrices),self)

        self.payLabel = QLabel("付款方式",self)
        self.deliverLabel = QLabel("运送方式",self)

        self.payBox = QComboBox(self)
        self.payBox.addItem("微信")
        self.payBox.addItem("支付宝")
        self.payBox.addItem("银行卡")
        self.deliverBox = QComboBox(self)
        self.deliverBox.addItem("顺丰")
        self.deliverBox.addItem("圆通")
        self.deliverBox.addItem("邮政")
        self.okButton = QPushButton("确认付款",self)
        self.cancleButton = QPushButton("取消",self)

        self.okButton.clicked.connect(self.setPayInfo)
        self.cancleButton.clicked.connect(self.cancle)

        layout=QGridLayout()
        layout.addWidget(self.aLabel,0,0)
        layout.addWidget(self.priceLabel,0,1)
        layout.addWidget(self.payLabel,1,0)    
        layout.addWidget(self.payBox,1,1)    
        layout.addWidget(self.deliverLabel,2,0)    
        layout.addWidget(self.deliverBox,2,1)      
        layout.addWidget(self.okButton,3,0)    
        layout.addWidget(self.cancleButton,3,1)    

        self.setLayout(layout)
        self.show()

    def setPayInfo(self):      
        self.payInfo.append(self.payBox.currentText())
        self.payInfo.append(self.deliverBox.currentText())
        self.close()

    def cancle(self):
        pass
        self.close()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = payDialog()
    sys.exit(app.exec_())
