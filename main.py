import math
import random
import sys

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5 import uic
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.flag = False
        self.run()
        self.btn1.clicked.connect(self.hello1)
        self.btn2.clicked.connect(self.hello2)

    def run(self):
        pass

    def hello1(self):
        if 1 <= self.box1.value() and not self.flag:
            self.number.display(self.box1.value())
            self.flag = True
            self.label.setText('')
            self.list.clear()

    def hello2(self):
        if 1 <= self.box2.value() <= 3 and self.number.value() >= self.box2.value():
            self.number.display(int(self.number.value() - self.box2.value()))
            n = QListWidget()
            self.list.addItem(f'Игрок взял - {self.box2.value()}')
            if self.number.value() == 0:
                self.label.setText("Победа игрока!!!")
                self.flag = False
                return
            if self.number.value() % 4 == 0:
                n = random.choice([1, 2, 3])
                self.list.addItem(f'Компьютер взял - {int(n)}')
                self.number.display(int(self.number.value() - n))
            else:
                n = self.number.value() % 4
                self.list.addItem(f'Компьютер взял - {int(n)}')
                self.number.display(int(self.number.value() - n))
            if self.number.value() == 0:
                self.label.setText("Победа компьютера!!!")
                self.flag = False
                return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
