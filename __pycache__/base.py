from PyQt5.QtWidgets import QWidget, QFrame, QPushButton, QLabel, QSlider,\
    QScrollArea, QDialog, QLineEdit, QCheckBox, QTableWidget, QComboBox,\
    QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QObject


class EButton(QPushButton):
    def __init__(self,id):
        super().__init__()
        self.setGeometry(0,80*id,180,80)
        self.setStyleSheet("QPushButton{background-color:#16A085;color:#ffffff;font-size:20px;}"
                               "QPushButton:h0over{background-color:#333333;}")


class ECheckBox(QCheckBox):
    def __init__(self, parent=None):
        super().__init__(parent)

    def set_theme_style(self):
        pass