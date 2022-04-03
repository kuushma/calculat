from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic


class None_formula_error(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('designerr/none_formula_error.ui', self)