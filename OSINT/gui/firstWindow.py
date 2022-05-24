from PyQt5.Qt import QUrl, QDesktopServices
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QFrame, QStackedWidget, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
import json
import pandas as pd
import random
import sys
import os

from pathlib import Path

sys.path.append(
   os.path.abspath(
      Path(__file__).resolve().parent.parent.parent
   )
)

class firstWindow(QMainWindow):
    def __init__(self):
        super(firstWindow, self).__init__()
        uic.loadUi("./uiFiles/firstWindow.ui", self)

        self.button1 = self.findChild(QPushButton, "pushButton")
        #self.button1.clicked.connect(self.nextWindow)

    #def nextWindow(self):
    #    screen2 = Main_Window()
    #    widget.addWidget(screen2)
    #    widget.setCurrentIndex(widget.currentIndex()+1)

app = QApplication(sys.argv)
widget = QStackedWidget()
mainwindow = firstWindow()
widget.addWidget(mainwindow)

widget.setFixedHeight(1000)
widget.setFixedWidth(1900)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting...")
