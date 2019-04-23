import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

class Example(QWidget):
        def __init__(self):
                super().__init__()
                self.setGeometry(0,0,600,600)
                self.setWindowTitle("Testing 123")
                self.show()

app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
