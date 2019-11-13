import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Circles')
        self.btn.clicked.connect(self.d)

    def d(self):
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawFlag(qp)
        qp.end()

    def drawFlag(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        r1 = randint(1, 100)
        r2 = randint(1, 150)
        r3 = randint(20, 80)
        qp.drawEllipse(randint(0, 600), randint(0, 400), r1, r1)
        qp.drawEllipse(randint(0, 600), randint(0, 400), r1, r1)
        qp.drawEllipse(randint(0, 600), randint(0, 400), r2, r2)
        qp.drawEllipse(randint(0, 600), randint(0, 400), r2, r2)
        qp.drawEllipse(randint(0, 600), randint(0, 400), r3, r3)
        qp.drawEllipse(randint(0, 600), randint(0, 400), r3, r3)
        qp.end()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
