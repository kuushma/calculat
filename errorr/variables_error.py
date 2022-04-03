from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic


class Variables_error(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('designerr/variables_error.ui', self)