from interface.comparador_interface import Ui_MainWindow
from PySide6.QtWidgets import QWidget, QPushButton, QApplication, QMainWindow

class main_window(QWidget,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bol = False
        self.play_button = QPushButton()
        self.play_button.setCheckable(True)
        self.stop_button = QPushButton()
        self.stop_button.setCheckable(True)
        self.play_button.clicked.connect(self.power_on())
        self.stop_button.clicked.connect(self.power_off())
    
    def power_on(self):
        if self.bol == False:
            self.play_button.setDisabled(False)
            self.stop_button.setDisabled(True)
            self.bol = True

    def power_off(self):
        if self.bol == True:
            self.play_button.setDisabled(True)
            self.stop_button.setDisabled(False)
            self.bol = False

