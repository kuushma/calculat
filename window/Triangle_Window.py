from PyQt5.QtWidgets import QMainWindow
from question import Qestion
from area.area_triangle import Triangle
from error.error import Error
from PyQt5.QtGui import QPixmap
from Triangle_ui import Triangle_ui


class Triangle_Window(QMainWindow, Triangle_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.back.clicked.connect(self.Back)
        self.question.clicked.connect(self.Qestion)
        self.Geron_run.clicked.connect(self.Geron)
        self.Hight_a_run.clicked.connect(self.Hight_a)
        self.angle_between_them_run.clicked.connect(self.angle_between_them)
        self.isosceles_triangle_run.clicked.connect(self.isosceles_triangle)
        self.equilateral_triangle_run.clicked.connect(self.equilateral_triangle)
        self.right_triangle_run.clicked.connect(self.right_triangle)

        self.triangle_regular.setPixmap(QPixmap('Pictures/triangle_regular'))
        self.triangle_isosceles.setPixmap(QPixmap('Pictures/triangle_isosceles'))
        self.triangle_equilateral.setPixmap(QPixmap('Pictures/triangle_equilateral'))
        self.triangle_rectangula.setPixmap(QPixmap('Pictures/triangle_rectangula'))

    def Geron(self):
        a = self.Geron_a.text()
        a = float(a.replace(',', '.'))
        b = self.Geron_b.text()
        b = float(b.replace(',', '.'))
        c = self.Geron_c.text()
        c = float(c.replace(',', '.'))
        if Triangle().examination(a, b, c) == 'Ошибка' or Triangle().Geron(a, b, c) == 'Ошибка':
            self.Error()
        else:
            self.Geron_ans.display(float(Triangle().Geron(a, b, c)))

    def Hight_a(self):
        a = self.Hight_a_a.text()
        a = float(a.replace(',', '.'))
        h = self.Hight_a_h.text()
        h = float(h.replace(',', '.'))
        if Triangle().examination(a, h) == 'Ошибка' or Triangle().Hight_a(a, h) == 'Ошибка':
            self.Error()
        else:
            self.Hight_a_ans.display(float(Triangle().Hight_a(a, h)))

    def angle_between_them(self):
        a = self.angle_between_them_a.text()
        a = float(a.replace(',', '.'))
        b = self.angle_between_them_b.text()
        b = float(b.replace(',', '.'))
        angle = self.angle_between_them_aa.text()
        angle = float(angle.replace(',', '.'))
        if Triangle().examination(a, b, angle) == 'Ошибка' or Triangle().angle_between_them(a, b, angle) == 'Ошибка':
            self.Error()
        else:
            self.angle_between_them_ans.display(float(Triangle().angle_between_them(a, b, angle)))

    def isosceles_triangle(self):
        a = self.isosceles_triangle_a.text()
        a = float(a.replace(',', '.'))
        b = self.isosceles_triangle_b.text()
        b = float(b.replace(',', '.'))
        if Triangle().examination(a, b) == 'Ошибка' or Triangle().isosceles_triangle(a, b) == 'Ошибка':
            self.Error()
        else:
            self.isosceles_triangle_ans.display(float(Triangle().isosceles_triangle(a, b)))

    def equilateral_triangle(self):
        a = self.equilateral_triangle_a.text()
        a = float(a.replace(',', '.'))
        if Triangle().examination(a) == 'Ошибка' or Triangle().equilateral_triangle(a) == 'Ошибка':
            self.Error()
        else:
            self.equilateral_triangle_ans.display(float(Triangle().equilateral_triangle(a)))

    def right_triangle(self):
        a = self.right_triangle_a.text()
        a = float(a.replace(',', '.'))
        b = self.right_triangle_b.text()
        b = float(b.replace(',', '.'))
        if Triangle().examination(a, b) == 'Ошибка' or Triangle().right_triangle(a, b):
            self.Error()
        else:
            self.right_triangle_ans.display(float(Triangle().right_triangle(a, b)))

    def Error(self):
        self.fourth = Error()
        self.fourth.show()

    def Qestion(self):
        self.fourth = Qestion()
        self.fourth.show()

    def Back(self):
        self.hide()