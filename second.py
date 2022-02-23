from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

from window.Triangle_Window import Triangle_Window
from window.Square_Window import Square_Window
from window.Rectangle_Window import Rectangle_Window
from window.Parallelogram_Window import Parallelogram_Window
from window.Trapezoid_Window import Trapezoid_Window
from window.Rhombus_Window import Rhombus_Window
from window.Circle_Window import Circle_Window
from question import Qestion


class Second_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('second.ui', self)

        self.triangle.clicked.connect(self.change_triangle)
        self.square.clicked.connect(self.change_square)
        self.rectangle.clicked.connect(self.change_rectangle)
        self.parallelogram.clicked.connect(self.change_parallelogram)
        self.trapezoid.clicked.connect(self.change_trapezoid)
        self.rhombus.clicked.connect(self.change_rhombus)
        self.circle.clicked.connect(self.change_circle)

        self.qestion.clicked.connect(self.Qestion)
        self.back.clicked.connect(self.Back)

    def change_triangle(self):
        self.third = Triangle_Window()
        self.third.show()

    def change_square(self):
        self.third = Square_Window()
        self.third.show()

    def change_rectangle(self):
        self.third = Rectangle_Window()
        self.third.show()

    def change_parallelogram(self):
        self.third = Parallelogram_Window()
        self.third.show()

    def change_trapezoid(self):
        self.third = Trapezoid_Window()
        self.third.show()

    def change_rhombus(self):
        self.third = Rhombus_Window()
        self.third.show()

    def change_circle(self):
        self.third = Circle_Window()
        self.third.show()

    def Qestion(self):
        self.fourth = Qestion()
        self.fourth.show()

    def Back(self):
        self.hide()