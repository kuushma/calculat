from PyQt5.QtWidgets import QMainWindow
from question import Qestion
from errorr.error import Error
from area.area_trapezoid import Trapezoid
from PyQt5.QtGui import QPixmap
from Trapezoid_ui import Trapezoid_ui


class Trapezoid_Window(QMainWindow, Trapezoid_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.back.clicked.connect(self.Back)
        self.qestion.clicked.connect(self.Qestion)
        self.sides_hide_run.clicked.connect(self.sides_hide)
        self.hide_linesr_run.clicked.connect(self.hide_linesr)
        self.sides_run.clicked.connect(self.sides)
        self.ravnobedrenny_side_run.clicked.connect(self.ravnobedrenny_side)
        self.ravnobedrenny_osns_ugol_run.clicked.connect(self.ravnobedrenny_osns_ugol)

        self.trapezoid_1.setPixmap(QPixmap('Pictures/trapezoid_1.PNG'))
        self.trapezoid_2.setPixmap(QPixmap('Pictures/trapezoid_2.JPEG'))
        self.trapezoid_3.setPixmap(QPixmap('Pictures/trapezoid_3.JPEG'))
        self.trapezoid_4.setPixmap(QPixmap('Pictures/trapezoid_4.PNG'))
        self.trapezoid_5.setPixmap(QPixmap('Pictures/trapezoid_5.PNG'))

    def sides_hide(self):
        a = self.sides_hide_a.text()
        a = float(a.replace(',', '.'))
        b = self.sides_hide_b.text()
        b = float(b.replace(',', '.'))
        h = self.sides_hide_h.text()
        h = float(h.replace(',', '.'))
        if Trapezoid().examination(a, b, h) == 'Ошибка':
            self.Error()
        else:
            self.sides_hide_ans.display(Trapezoid().sides_hide(a, b, h))

    def hide_linesr(self):
        m = self.hide_linesr_m.text()
        m = float(m.replace(',', '.'))
        h = self.hide_linesr_h.text()
        h = float(h.replace(',', '.'))
        if Trapezoid().examination(m, h) == 'Ошибка':
            self.Error()
        else:
            self.hide_linesr_ans.display(Trapezoid().hide_linesr(h, m))

    def sides(self):
        a = self.sides_a.text()
        a = float(a.replace(',', '.'))
        b = self.sides_b.text()
        b = float(b.replace(',', '.'))
        c = self.sides_c.text()
        c = float(c.replace(',', '.'))
        d = self.sides_d.text()
        d = float(d.replace(',', '.'))
        if Trapezoid().examination(a, b, c, d) == 'Ошибка':
            self.Error()
        else:
            self.sides_ans.display(Trapezoid().sides(a, b, c, d))

    def ravnobedrenny_side(self):
        a = self.ravnobedrenny_side_a.text()
        a = float(a.replace(',', '.'))
        b = self.ravnobedrenny_side_b.text()
        b = float(b.replace(',', '.'))
        c = self.ravnobedrenny_side_c.text()
        c = float(c.replace(',', '.'))
        if Trapezoid().examination(a, b, c) == 'Ошибка':
            self.Error()
        else:
            self.ravnobedrenny_side_ans.display(Trapezoid().ravnobedrenny_side(a, b, c))

    def ravnobedrenny_osns_ugol(self):
        a = self.ravnobedrenny_osns_ugol_a.text()
        a = float(a.replace(',', '.'))
        b = self.ravnobedrenny_osns_ugol_b.text()
        b = float(b.replace(',', '.'))
        aa = self.ravnobedrenny_osns_ugol_aa.text()
        aa = float(aa.replace(',', '.'))
        if Trapezoid().examination(a, b, aa) == 'Ошибка':
            self.Error()
        else:
            self.ravnobedrenny_osns_ugol_ans.display(Trapezoid().ravnobedrenny_osns_ugol(a, b, aa))

    def Qestion(self):
        self.fourth = Qestion()
        self.fourth.show()

    def Back(self):
        self.hide()

    def Error(self):
        self.fourth = Error()
        self.fourth.show()