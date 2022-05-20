from curses import window
from PySide6.QtWidgets import QWidget
from PySide6 import QtWidgets
import _conexion as cn
from interfaz.controllers.main_window import MainWindowForm
from interfaz.controllers.register import Register
from views.inicio import MainInicio

class Inici(QWidget,MainInicio):
    def __init__(self,widget):
        super().__init__(widget)
        self.widget = widget
        self.setupUi(self)
        self.boton = self.ok
        self.boton.clicked.connect(self.send)
        self.botonRegistro.clicked.connect(self.open_main_register)
        
    def open_main_window(self,usuario):
        inputs = MainWindowForm(usuario,self.widget)
        self.widget.addWidget(inputs)
        
        self.widget.setCurrentIndex(2)
        self.widget.show()
        
        
        
    def open_main_register(self):
        # registro = Register(self.widget)
        # self.widget.addWidget(registro)
        self.widget.setCurrentIndex(1)
        self.widget.show()
        print(dir(self.widget))
        
    def send(self):
           response=cn.Conexion('usuario').login(self.user_input.text(),self.password_input.text())
           if response:
               self.open_main_window(self.user_input.text())
        #    else:
            #    register = Register()
