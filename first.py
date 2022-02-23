import sys

from PyQt5 import uic
from second import Second_Window
from PyQt5.QtWidgets import QApplication, QMainWindow
from task_generator import task_generator


class First_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('first.ui', self)

        self.Start.clicked.connect(self.change_first)
        self.TaSkS.clicked.connect(self.taSkS)

    def change_first(self):
        self.second_window = Second_Window()
        self.second_window.show()

    def taSkS(self):
        self.second_window = task_generator()
        self.second_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = First_Window()
    ex.show()
    sys.exit(app.exec_())