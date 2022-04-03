from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic


class Error(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('designerr/error.ui', self)