from argparse import Action
from interface.comparador_interface import Ui_MainWindow
from PySide6.QtWidgets import QWidget, QPushButton, QApplication, QMainWindow
from interface.comparador_interface import Ui_MainWindow

class main_window(QWidget,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #Botones
        ButtonStop = self.stop_button
        ButtonPlay = self.play_button

        #Cuadros de texto
        URLtext = self.URL
        PRICEtext = self.Precio
        ALERTtext = self.Alert
        PRODUCTtext = self.NombreProducto
        self.stop_button.clicked.connect(self.say_hello())
    
    def say_hello(self):
        print("holaaaa")



        

