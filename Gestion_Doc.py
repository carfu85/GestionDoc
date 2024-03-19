import sys
from PyQt6.QtWidgets import QApplication
from Main import mainWindow

class GestionDoc():
    def __init__(self):
        self.app = QApplication([])
        self.mainwindow= mainWindow()
        self.app.exec()