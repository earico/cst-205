import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDial, QHBoxLayout, QSpinBox, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon, QPixmap

class pictureDisplay(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Picture")
		#self.setGeometry(0,100,1500,900)

		image = QLabel(self)
		pixmap = QPixmap('MFDOOM.jpg')
		image.setPixmap(pixmap)

		self.resize(pixmap.width(),pixmap.height())
		self.show()

app = QApplication(sys.argv)
ex = pictureDisplay()
sys.exit(app.exec_())
