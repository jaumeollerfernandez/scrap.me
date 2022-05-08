from argparse import Action
from interface.comparador_interface import Ui_MainWindow
from PySide6.QtWidgets import QWidget, QPushButton, QApplication, QMainWindow

class main_window(QWidget,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        ActionSalir = self.actionSalir


        

