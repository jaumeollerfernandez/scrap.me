from curses import window
from PySide6.QtWidgets import QWidget
from PySide6 import QtWidgets
import _conexion as cn
from views.main_register import RegisterForm



class Register(QWidget,RegisterForm):
    def __init__(self,widget):
        super().__init__()
        self.widget = widget
        self.setupUi(self)
        self.botonInicio.clicked.connect(self.open_main_inicio)
        self.registro_boton.clicked.connect(self.send_register_data)
        
        
    def open_main_inicio(self):
        self.widget.setCurrentIndex(0)
        self.widget.show()

       
        
    def send_register_data(self):
           
           response = cn.Conexion('usuario').lectura(self.nick_input.text())
           if not response:
                cn.Conexion('usuario').register(self.nick_input.text(),self.contrasea_input.text(),self.nombre_input.text(),self.apellidos_input.text())
           else:
               print('el usuario ya existe')
