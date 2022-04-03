from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic


class No_variable(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('designerr/no_variable.ui', self)