from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic


class Error_min_max(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('designerr/error_min_max.ui', self)