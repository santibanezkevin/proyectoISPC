import mysql.connector,producto;
from mysql.connector import Error
from producto import Producto

class ConexionBD:

    ### constructor de la clase ConexionBD ****
    def __init__(self) -> None:
                        
            try:
                self.connection=mysql.connector.connect(host='localhost',
                                                        database='carta_digital',
                                                        user='root',
                                                        password='root')
                if self.connection.is_connected():
                        db_Info=self.connection.get_server_info()
                        print("Conectada a MySQL Server version", db_Info)
                        
                        self.cursor=self.connection.cursor()
                        self.cursor.execute("select database();")
                        
                        record=self.cursor.fetchone()
                        print("Estas conectado a la base de datos: ", record)
                        self.cursor.close()
            except Error as e:
                print ("Error while connecting to MySQL", e)
    
    # metodo que cierra la conexion a la bd       
    def cerrarConexion(self):
            try:
                if self.connection.is_connected():
                    
                    self.connection.close()
                    print("Conexion MySQL cerrada.")
            except Error as e:
                print ("Error al cerrar la conexion",e)
    
   
 
    #insertar producto con un objeto como parametro
    def insertarProducto(self,prod):
            try:
                if self.connection.is_connected():
                    mySql_insert_query = """INSERT INTO `carta_digital`.`producto` (`nombre`, `descripcion`, `precio`, `stock`, `categoria_cod`) VALUES (%s,%s,%s,%s,%s) """
                    data=(prod.nombre,prod.descripcion,prod.precio,prod.stock,prod.categoria)
                    self.cursor=self.connection.cursor()
                    self.cursor.execute(mySql_insert_query,data)
                    self.connection.commit()
                    record=self.cursor.fetchone()
                    print(self.cursor.rowcount, "Producto agregado exitosamente ")
                    self.cursor.close()
            except Error as e:
                print("Error al insertar producto {}".format(e))


    #Eliminar producto con un objeto como parametro
    def borrarProducto(self, codigo):
            try:
                if self.connection.is_connected():
                    mySql_delete_query = "DELETE FROM `carta_digital`.`producto` WHERE `codigo` = %s"
                    self.cursor=self.connection.cursor()
                    data=(codigo, )
                    self.cursor.execute(mySql_delete_query, data)
                    self.connection.commit()
                    record=self.cursor.fetchone()
                    print(self.cursor.rowcount, "Producto eliminado exitosamente ")
                    self.cursor.close()
            except Error as e:
                print("Error al borrar un producto {}".format(e))


                