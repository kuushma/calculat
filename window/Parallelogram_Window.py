from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from question import Qestion
from error.error import Error
from area.area_parallelogram import Parallelogram
from PyQt5.QtGui import QPixmap
from Parallelogram_ui import Parallelogram_ui


class Parallelogram_Window(QMainWindow, Parallelogram_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.back.clicked.connect(self.Back)
        self.question.clicked.connect(self.Qestion)
        self.side_hide_run.clicked.connect(self.side_hide)
        self.side_injection_run.clicked.connect(self.side_injection)
        self.diagonal_ugol_run.clicked.connect(self.diagonal_ugol)

        self.parallelogram_1.setPixmap(QPixmap('Pictures/parallelogram_1.JPEG'))
        self.parallelogram_2.setPixmap(QPixmap('Pictures/parallelogram_2.JPEG'))

    def side_hide(self):
        a = self.side_hide_a.text()
        a = float(a.replace(',', '.'))
        h = self.side_hide_h.text()
        h = float(h.replace(',', '.'))
        if Parallelogram().examination(a, h) == 'Ошибка' or Parallelogram().side_hide(a, h) == 'Ошибка':
            self.Error()
        else:
            self.side_hide_ans.display(Parallelogram().side_hide(a, h))

    def side_injection(self):
        a = self.side_injection_a.text()
        a = float(a.replace(',', '.'))
        b = self.side_injection_b.text()
        b = float(b.replace(',', '.'))
        aa = float(self.side_injection_aa.text())
        if Parallelogram().examination(a, b, aa) == 'Ошибка' or Parallelogram().side_injection(a, b, aa) == 'Ошибка':
            self.Error()
        else:
            self.side_injection_ans.display(Parallelogram().side_injection(a, b, aa))

    def diagonal_ugol(self):
        d1 = self.diagonal_ugol_d1.text()
        d1 = float(d1.replace(',', '.'))
        d2 = self.diagonal_ugol_d2.text()
        d2 = float(d2.replace(',', '.'))
        aa = float(self.diagonal_ugol_aa.text())
        if Parallelogram().examination(d1, d2, aa) == 'Ошибка' or Parallelogram().diagonal_ugol(d1, d2, aa) == 'Ошибка':
            self.Error()
        else:
            self.diagonal_ugol_ans.display(Parallelogram().diagonal_ugol(d1, d2, aa))

    def Qestion(self):
        self.fourth = Qestion()
        self.fourth.show()

    def Back(self):
        self.hide()

    def Error(self):
        self.fourth = Error()
        self.fourth.show()