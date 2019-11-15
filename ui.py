from PyQt5.QtWidgets import QWidget, QPushButton


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.btn = QPushButton(self)
        self.setWindowTitle('Circles')
        self.setGeometry(50, 50, 800, 600)
        self.btn.setText('Show')
        self.btn.move(350, 470)
