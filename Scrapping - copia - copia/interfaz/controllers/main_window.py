from PySide6.QtWidgets import QWidget, QPushButton, QApplication, QMainWindow
from views.main_window import Mainwindow
import _Captador as cp
import _captadorDatosWeb as cpw
import _conexion as cn
import _comparador as cm
import interfaz.controllers.main_interface as ci
import os

class MainWindowForm(QWidget,Mainwindow):
    def __init__(self,user,widget):
        super().__init__()
        self.setupUi(self)
        
        self.widget = widget
        self.user=user
        self.lista=[]
        buttonInsert= self.insert_btn
        buttonDelete = self.delete_btn
        # buttonDelete.setDisabled(True)
        self.buttonStart = self.start_btn
        self.buttonStart.setDisabled(True)
        buttonInsert.clicked.connect(self.set_url)
        buttonDelete.clicked.connect(self.deleteItem)
        self.getProductos()
        
        
        
    
    def set_url(self):
        # if os.path.exists('BD/db.txt'):
        #     os.remove('BD/db.txt')
        id=self.url_list.count()+1
        self.lista.append(id)
        self.lista.append(self.user)
        url = self.input_url.text()
        self.lista.append(url)
        cn.Conexion('productos').escrituraProductos(self.lista)
        cp.Captador(self.user).setTags(url)
        self.lista=[]
        self.url_list.clear()
        self.getProductos()
        self.input_url.clear()
        
        
    def iniciar(self):
        
        interface = ci.MainInterface(self.user,self.widget)
        self.widget.addWidget(interface)
        
        self.widget.setCurrentIndex(3)
        self.widget.show()
        
    def activate(self,condition=bool):
        
            self.buttonStart.setDisabled(condition)
            self.buttonStart.clicked.connect(self.iniciar)
            
    
    def getProductos(self):
        
        productos = cn.Conexion('productos').lectura(self.user)
        if len(productos)>0:
            self.activate(False)
            i=0
            while i < len(productos):
                self.url_list.addItem(productos[i][2])
                i+=1
        else:
            self.activate(True)
    
    def deleteItem(self):
        
        clicked = self.url_list.currentItem()
        url = clicked.text()
        cn.Conexion('productos').delete(url,self.user)
        # cn.Conexion('url_tags').delete()
        self.url_list.clear()
        self.getProductos()