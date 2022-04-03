from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic


class Non_existent(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('designerr/non-existent.ui', self)