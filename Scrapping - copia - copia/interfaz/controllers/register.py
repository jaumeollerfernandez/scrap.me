from curses import window
from PySide6.QtWidgets import QWidget, QMessageBox
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
                self.nick_input.setText("")
                self.contrasea_input.setText("")
                self.nombre_input.setText("")
                self.apellidos_input.setText("")
                QMessageBox.information(self,"Register Ouput","Usuario registrado correctamente!!")
                print(f'ERROR #0: El Usuario {self.nick_input.text()} registrado correctamente')
                self.widget.setCurrentIndex(0)
           else:
                self.nick_input.setText("")
                self.contrasea_input.setText("")
                self.nombre_input.setText("")
                self.apellidos_input.setText("")
                QMessageBox.information(self,"Register Ouput","El Usuario ya esta registrado")
                print(f'ERROR #103: El Usuario {self.nick_input.text()} ya existe')
