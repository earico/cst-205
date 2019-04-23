from PyQt5.QtWidgets import (QWidget, QLabel, QComboBox, QApplication, QPushButton)
from PyQt5.QtCore import pyqtSlot
import sys

class myPopup(QWidget):
    def __init__(self):
        QWidget.__init__(self)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl1 = QLabel("RGB: ",self) #setting label text for RGB
        self.lbl2 = QLabel("Hex: ",self) #setting label text for HEX
        self.my_btn = QPushButton("Show Color!", self) #setting button for new window
        self.my_btn.clicked.connect(self.on_click, )

        combo = QComboBox(self) #init combo box
        combo.addItem("Emerald") #adding color to box
        combo.addItem("Diamond") #^^
        combo.addItem("Copper") #^^
        combo.addItem("Platinum") #^^
        combo.addItem("Gold") #^^
        combo.move(100,50) #setting position of combo box

        self.lbl1.move(30,150) #Setting label 1 farther to the left to create room for the text
        self.lbl2.move(170, 150) #Setting label 2 farther to the right to give text more room for other text (Gold)

        combo.activated[str].connect(self.onActivated)

        self.setGeometry(300,300,300,200) #window dimensions
        self.setWindowTitle('RGB/HEX')
        self.show()

    def onActivated(self, text):
        if(text=="Emerald"): #check for color then set values accordlingly
            self.lbl1.setText("RGB: (31,78,47)")
            self.lbl1.adjustSize()
            self.lbl2.setText("HEX: #50c878")
            self.lbl2.adjustSize()

        if(text=="Diamond"): #check for color then set values accordlingly
            self.lbl1.setText("RGB: (185,242,255)")
            self.lbl1.adjustSize()
            self.lbl2.setText("HEX: #B9F2FF")
            self.lbl2.adjustSize()

        if(text=="Copper"): #check for color then set values accordlingly
            self.lbl1.setText("RGB: (72,45,20)")
            self.lbl1.adjustSize()
            self.lbl2.setText("HEX: #b87333")
            self.lbl2.adjustSize()

        if(text=="Platinum"): #check for color then set values accordlingly
            self.lbl1.setText("RGB: (90,89,89)")
            self.lbl1.adjustSize()
            self.lbl2.setText("HEX: #e5e4e2")
            self.lbl2.adjustSize()

        if(text=="Gold"): #check for color then set values accordlingly
            self.lbl1.setText("RGB: (255,215,0)")
            self.lbl1.adjustSize()
            self.lbl2.setText("HEX: #FFD700")
            self.lbl2.adjustSize()

if __name__ == '__main__': #init
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
