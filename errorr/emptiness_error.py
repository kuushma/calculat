from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

class Emptiness_error(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('designerr/emptiness_error.ui', self)