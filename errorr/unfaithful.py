from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic


class Unfaithful(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('designerr/unfaithful.ui', self)