import sys
from PyQt5.QtWidgets import QApplication
from random import randint
import ui as f
from PyQt5.QtGui import QPainter, QColor


class MyWidget(f.Window):
    def __init__(self):
        super().__init__()
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
        qp.setBrush(QColor(randint(0, 256), randint(0, 256), randint(0, 256)))
        r1 = randint(1, 100)
        r2 = randint(1, 150)
        r3 = randint(20, 80)
        qp.drawEllipse(randint(0, 600), randint(0, 400), r1, r1)
        qp.setBrush(QColor(randint(0, 256), randint(0, 256), randint(0, 256)))
        qp.drawEllipse(randint(0, 600), randint(0, 400), r1, r1)
        qp.setBrush(QColor(randint(0, 256), randint(0, 256), randint(0, 256)))
        qp.drawEllipse(randint(0, 600), randint(0, 400), r2, r2)
        qp.setBrush(QColor(randint(0, 256), randint(0, 256), randint(0, 256)))
        qp.drawEllipse(randint(0, 600), randint(0, 400), r2, r2)
        qp.setBrush(QColor(randint(0, 256), randint(0, 256), randint(0, 256)))
        qp.drawEllipse(randint(0, 600), randint(0, 400), r3, r3)
        qp.setBrush(QColor(randint(0, 256), randint(0, 256), randint(0, 256)))
        qp.drawEllipse(randint(0, 600), randint(0, 400), r3, r3)
        qp.end()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())