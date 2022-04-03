from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic


class Number_error(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('designerr/number_error.ui', self)