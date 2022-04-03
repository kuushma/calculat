from PyQt5.QtWidgets import QMainWindow
from window_ui.question import Qestion
from errorr.error import Error
from area.area_rectangle import rectangle
from PyQt5.QtGui import QPixmap
from window_ui.Rectangle_ui import Rectangle_ui
from PyQt5 import uic


class Rectangle_Window(QMainWindow, Rectangle_ui):
    def __init__(self):
        super().__init__()
        uic.loadUi('designerr/rectangle.ui', self)

        self.back.clicked.connect(self.Back)
        self.question.clicked.connect(self.Qestion)
        self.side_run.clicked.connect(self.side)
        self.diagonal_run.clicked.connect(self.diagonal)
        self.radius_and_side_run.clicked.connect(self.radius_and_side)
        self.side_diagonal_run.clicked.connect(self.side_diagonal)
        self.diametr_and_side_run.clicked.connect(self.diametr_and_side)

        self.rectangle_1.setPixmap(QPixmap('Pictures/rectange_1.JPEG'))
        self.rectangle_2.setPixmap(QPixmap('Pictures/rectange_2.PNG'))

    def side(self):
        a = self.side_a.text()
        a = float(a.replace(',', '.'))
        b = self.side_b.text()
        b = float(b.replace(',', '.'))
        if rectangle().examination(a, b) == 'Ошибка':
            self.Error()
        else:
            self.side_ans.display(rectangle().side(a, b))

    def diagonal(self):
        d = self.diagonal_d.text()
        d = float(d.replace(',', '.'))
        aa = self.diagonal_aa.text()
        aa = float(aa.replace(',', '.'))
        if rectangle().examination(d, aa) == 'Ошибка':
            self.Error()
        else:
            self.diagonal_ans.display(rectangle().diagonal(d, aa))

    def side_diagonal(self):
        a = self.side_diagonal_a.text()
        a = float(a.replace(',', '.'))
        d = self.side_diagonal_d.text()
        d = float(d.replace(',', '.'))
        if rectangle().side_diagonal(a, d) == 'Ошибка' or rectangle().examination(a, d):
            self.Error()
        else:
            self.side_diagonal_ans.display(rectangle().side_diagonal(a, d))

    def radius_and_side(self):
        a = self.radius_and_side_a.text()
        a = float(a.replace(',', '.'))
        R = self.radius_and_side_R.text()
        R = float(R.replace(',', '.'))
        if rectangle().examination(a, R) == 'Ошибка':
            self.Error()
        else:
            self.radius_and_side_ans.display(rectangle().radius_and_side(a, R))

    def diametr_and_side(self):
        a = self.diametr_and_side_a.text()
        a = float(a.replace(',', '.'))
        D = self.diametr_and_side_D.text()
        D = float(D.replace(',', '.'))
        if rectangle().examination(a, D) == 'Ошибка':
            self.Error()
        elif (D ** 2 - a ** 2) < 0:
            self.Error()
        else:
            self.diametr_and_side_.display(rectangle().diametr_and_side(a, D))

    def Qestion(self):
        self.fourth = Qestion()
        self.fourth.show()

    def Back(self):
        self.hide()

    def Error(self):
        self.fourth = Error()
        self.fourth.show()