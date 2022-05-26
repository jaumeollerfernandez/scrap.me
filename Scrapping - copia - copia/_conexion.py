from colorama import Cursor
import mysql.connector
from mysql.connector import errorcode
# import _comparador as compa

class Conexion:

    def __init__(self,tabla):
        self.tabla = tabla
        
        self.c = {
                'user': 'root',
                'password': '',
                'port':'33021',
                'host': '127.0.0.1',
                'database': 'scrapping'
            }
        self.cnx=self.iniciarSesion()
        self.cursor = self.Vcursor()
        

    def iniciarSesion(self):
        try: #iniciamos la conexión
            cnx = mysql.connector.connect(**self.c)
            return cnx#le pasamos el diccionario, directamente lo mismo que pasar por parametros
        except mysql.connector.Error as err: #zona de casos de error
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error de nombre usuario o clave",err)
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("error de acceso de base de datos", err)
            else:
                print(err)
                
                
    def Vcursor(self):
        cursor = self.cnx.cursor()        
        cursor.execute("USE scrapping") # BD que usaremos
        return cursor
            
    
    def login(self,user,password):
        sql = f"SELECT * FROM {self.tabla} WHERE id_usuario = '{user}' AND password = '{password}'"
        self.cursor.execute(sql)
        return self.cursor.fetchone()
    
    
    def register(self,username,password,name,surname):
        
        sql = f"INSERT INTO {self.tabla} VALUES ('{username}','{password}','{name}','{surname}')"
        try:
            self.cursor.execute(sql)
        except mysql.connector.Error as err:
            print("datos ya insertados",err)
        self.cnx.commit() #confirmar la transacción
        self.cursor.close()
        self.cnx.close()
        
    def lectura(self,user):
        sql = f"SELECT * FROM {self.tabla} where id_usuario = '{user}'"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        return res
    
    def lecturaTags(self): # lee la tabla tags
        sql = f"SELECT * FROM {self.tabla}"
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        return res

    def escritura_URL_TAGS(self, lista_url_tags,user,id): # inserta datos en la tabla url_tags 
        id=id
        id_usuario = user
        nombre_empresa = lista_url_tags
        sql = f"INSERT INTO {self.tabla} VALUES({id},'{id_usuario}','{nombre_empresa}');"
        try:
            self.cursor.execute(sql)
        except mysql.connector.Error as err:
                print(err)
        self.cnx.commit() #confirmar la transacción
        self.cursor.close()
        self.cnx.close()
        
    def update(self,precio,id,user):
        sql = f"UPDATE {self.tabla} SET precio = '{precio}' where id = '{id}' and id_usuario = '{user}'"
        try:
            self.cursor.execute(sql)
        except mysql.connector.Error as err:
                print(err)
        self.cnx.commit() #confirmar la transacción
        self.cursor.close()
        self.cnx.close() 
        
        
    def escritura(self,array):
        z=0
        while z < len(array):
            id = array[z][0]
            id_usuario = array[z][1]
            nombre = array[z][2]
            precio = array[z][3]
            url = array[z][4]
            #tabla = "comparador"
            sql = f"INSERT INTO {self.tabla} VALUES ({id},'{id_usuario}','{nombre}',{precio},'{url}')"
            try:
                self.cursor.execute(sql)
            except mysql.connector.Error as err:
                print("datos ya insertados",err)
            z+=1
                
        self.cnx.commit() #confirmar la transacción
        self.cursor.close()
        self.cnx.close()
    
    def escrituraProductos(self,array):
    
        id_usuario = array[1]
        url = array[2]
            #tabla = "comparador"
        sql = f"INSERT INTO {self.tabla}(id_usuario,url) VALUES ('{id_usuario}','{url}')"
        try:
            self.cursor.execute(sql)
        except mysql.connector.Error as err:
            print("datos ya insertados",err)
           
                
        self.cnx.commit() #confirmar la transacción
        self.cursor.close()
        self.cnx.close()

    
    def delete(self,url,user):
        sql = f"DELETE FROM {self.tabla} WHERE URL = '{url}' and ID_USUARIO = '{user}'"
        
        try:
            self.cursor.execute(sql)
        except mysql.connector.Error as err:
            print("datos no eliminados",err)
            
        self.cnx.commit() #confirmar la transacción
        self.cursor.close()
        self.cnx.close()


    def lectura_TAGS_relacion_User(self,user):
        
        
        sql= f"SELECT tabla1.id,tabla1.id_usuario,tabla2.url,tabla3.tag1,tabla3.tag2,tabla3.tag3,tabla3.tag4,tabla3.tag5,tabla3.tag6 from url_tags tabla1 join productos tabla2 on tabla1.id_usuario = tabla2.id_usuario and tabla1.id = tabla2.id join tags tabla3 on tabla1.nombre_empresa = tabla3.nombre_empresa and tabla2.id_usuario='{user}' order by id" 
        
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        return res
    # SELECT tabla1.id,tabla1.id_usuario,tabla2.url,tabla3.tag1,tabla3.tag2,tabla3.tag3,tabla3.tag4,tabla3.tag5,tabla3.tag6 from url_tags tabla1 join productos tabla2 on tabla1.id_usuario = tabla2.id_usuario join tags tabla3 on tabla1.nombre_empresa = tabla3.nombre_empresa; 