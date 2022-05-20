from PySide6.QtWidgets import QWidget, QPushButton, QApplication, QMainWindow
from views.main_window import Mainwindow
from _Captador import Captador
import _captadorDatosWeb as cp
from _comparador import ComparadorFinal

class MainWindowForm(QWidget,Mainwindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lista=[]
        buttonInsert= self.insert_btn
        self.buttonStart = self.start_btn
        self.buttonStart.setDisabled(True)
        buttonInsert.clicked.connect(self.set_url)
        
        
    
    def set_url(self):
        
        url = self.input_url.text()
        print(url)
        self.url_list.addItem(url)
        self.lista.append(url)
        self.activate()
        self.input_url.clear()
        
        
    def a(self):
        
        Captador(True).introducirURL(self.lista)
        m = cp.CaptadorPrecios('alter_main_program/BD/url_tag.txt').getData()
        ComparadorFinal(m).comparacion("alter_main_program/BD/db.txt")
        
    def activate(self):
        
        if len(self.lista) > 0:
            self.buttonStart.setDisabled(False)
            self.buttonStart.clicked.connect(self.a)