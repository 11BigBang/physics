# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 07:01:07 2020

@author: wbmar
"""

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200,200,400,400)
        self.setWindowTitle('Fuck off')
        self.initUI()
        
    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText('My first label')
        self.label.move(50,50)
    
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText('Click me')
        self.b1.clicked.connect(self.clicked)
        
    def clicked(self):
        self.label.setText('You pressed the button')
        self.update()
        
    def update(self):
        self.label.adjustSize()
        

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    
    win.show()
    sys.exit(app.exec_())
    
window()