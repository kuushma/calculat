from PyQt5.QtWidgets import QMainWindow
from window_ui.question import Qestion
from errorr.error import Error
from area.area_square import Square
from PyQt5.QtGui import QPixmap
from window_ui.Square_ui import  Square_ui
from PyQt5 import uic


class Square_Window(QMainWindow,  Square_ui):
    def __init__(self):
        super().__init__()
        uic.loadUi('designerr/square.ui', self)

        self.back.clicked.connect(self.Back)
        self.question.clicked.connect(self.Qestion)
        self.side_run.clicked.connect(self.side)
        self.diagonal_run.clicked.connect(self.diagonal)

        self.square.setPixmap(QPixmap('Pictures/square.JPEG'))

    def side(self):
        a = self.side_a.text()
        a = float(a.replace(',', '.'))
        if Square().examination(a) == 'Ошибка':
            self.Error()
        else:
            self.side_ans.display(Square().side(a))

    def diagonal(self):
        a = self.diagonal_d.text()
        a = float(a.replace(',', '.'))
        if Square().examination(a) == 'Ошибка':
            self.Error()
        else:
            self.diagonal_ans.display(Square().diagonal(a))

    def Qestion(self):
        self.fourth = Qestion()
        self.fourth.show()

    def Back(self):
        self.hide()

    def Error(self):
        self.fourth = Error()
        self.fourth.show()