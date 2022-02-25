from PyQt5.QtWidgets import QMainWindow
from question import Qestion
from error.error import Error
from area.area_rhombus import Rhombus
from PyQt5.QtGui import QPixmap
from Rhombus_ui import Rhombus_ui



class Rhombus_Window(QMainWindow, Rhombus_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.back.clicked.connect(self.Back)
        self.qestion.clicked.connect(self.Qestion)
        self.side_hide_run.clicked.connect(self.side_hide)
        self.side_ugol_run.clicked.connect(self.side_ugol)
        self.diagonal_run.clicked.connect(self.diagonal)
        self.diagonal_ugol_run.clicked.connect(self.diagonal_ugol)
        self.diagonal_ugol_ne_run.clicked.connect(self.diagonal_ugol_ne)
        self.ugol_radius_run.clicked.connect(self.ugol_radius)
        self.side_radius_run.clicked.connect(self.side_radius)

        self.rhombus_1.setPixmap(QPixmap('Pictures/rhombus_1.PNG'))
        self.rhombus_2.setPixmap(QPixmap('Pictures/rhombus_2.PNG'))
        self.rhombus_3.setPixmap(QPixmap('Pictures/rhombus_3.JPEG'))
        self.rhombus_4.setPixmap(QPixmap('Pictures/rhombus_4.JPEG'))
        self.rhombus_5.setPixmap(QPixmap('Pictures/rhombus_5.JPEG'))


    def side_hide(self):
        a = self.side_hide_a.text()
        a = float(a.replace(',', '.'))
        h = self.side_hide_h.text()
        h = float(h.replace(',', '.'))
        if Rhombus().examination(a, h) == 'Ошибка':
            self.Error()
        else:
            self.side_hide_ans.display(Rhombus().side_hide(a, h))

    def side_ugol(self):
        a = self.side_ugol_a.text()
        a = float(a.replace(',', '.'))
        aa = self.side_ugol_aa.text()
        aa = float(aa.replace(',', '.'))
        if Rhombus().examination(a, aa) == 'Ошибка':
            self.Error()
        else:
            self.side_ugol_ans.display(Rhombus().side_ugol(a, aa))

    def diagonal(self):
        d1 = self.diagonal_d1.text()
        d1 = float(d1.replace(',', '.'))
        d2 = self.diagonal_d2.text()
        d2 = float(d2.replace(',', '.'))
        if Rhombus().examination(d1, d2) == 'Ошибка':
            self.Error()
        else:
            self.diagonal_ans.display(Rhombus().diagonal(d1, d2))

    def diagonal_ugol(self):
        d = self.diagonal_ugol_d.text()
        d = float(d.replace(',', '.'))
        aa = self.diagonal_ugol_aa.text()
        aa = float(aa.replace(',', '.'))
        if Rhombus().examination(d, aa) == 'Ошибка':
            self.Error()
        else:
            self.diagonal_ugol_ans.display(Rhombus().diagonal_ugol(d, aa))

    def diagonal_ugol_ne(self):
        d = self.diagonal_ugol_ne_d.text()
        d = float(d.replace(',', '.'))
        aa = self.diagonal_ugol_ne_aa.text()
        aa = float(aa.replace(',', '.'))
        if Rhombus().examination(d, aa) == 'Ошибка':
            self.Error()
        else:
            self.diagonal_ugol_ne_ans.display(Rhombus().diagonal_ugol_ne(d, aa))

    def ugol_radius(self):
        aa = self.ugol_radius_aa.text()
        aa = float(aa.replace(',', '.'))
        r = self.ugol_radius_r.text()
        r = float(r.replace(',', '.'))
        if Rhombus().examination(aa, r) == 'Ошибка':
            self.Error()
        else:
            self.ugol_radius_ans.display(Rhombus().ugol_radius(aa, r))

    def side_radius(self):
        a = self.side_radius_a.text()
        a = float(a.replace(',', '.'))
        r = self.side_radius_r.text()
        r = float(r.replace(',', '.'))
        if Rhombus().examination(a, r) == 'Ошибка':
            self.Error()
        else:
            self.side_radius_ans.display(Rhombus().side_radius(a, r))

    def Qestion(self):
        self.fourth = Qestion()
        self.fourth.show()

    def Back(self):
        self.hide()

    def Error(self):
        self.fourth = Error()
        self.fourth.show()