from PyQt5.QtWidgets import QMainWindow
from window_ui.question import Qestion
from area.area_circle import Circle
from errorr.error import Error
from PyQt5.QtGui import QPixmap
from window_ui.Circle_ui import Circle_ui


class Circle_Window(QMainWindow, Circle_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.back.clicked.connect(self.Back)
        self.question.clicked.connect(self.Qestion)
        self.radius_run.clicked.connect(self.radius)
        self.diametr_run.clicked.connect(self.diametr)
        self.len_run.clicked.connect(self.len)

        self.circle.setPixmap(QPixmap('Pictures/circle.JPEG'))


    def radius(self):
        r = self.radius_r.text()
        r = float(r.replace(',', '.'))
        if Circle().examination(r) == 'Ошибка':
            self.Error()
        else:
            self.radius_ans.display(Circle().radius(r))

    def diametr(self):
        d = self.diametr_d.text()
        d = float(d.replace(',', '.'))
        if Circle().examination(d) == 'Ошибка':
            self.Error()
        else:
            self.diametr_ans.display(Circle().diametr(d))

    def len(self):
        L = self.len_L.text()
        L = float(L.replace(',', '.'))
        if Circle().examination(L) == 'Ошибка':
            self.Error()
        else:
            self.len_ans.display(Circle().len(L))

    def Qestion(self):
        self.fourth = Qestion()
        self.fourth.show()

    def Back(self):
        self.hide()

    def Error(self):
        self.fourth = Error()
        self.fourth.show()