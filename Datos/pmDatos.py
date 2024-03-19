import sqlite3
from Datos.Model.dbPmCpm import conectar, crearDB

class PmDatos():
    def __init__(self,nombre, apellido, correo, posicion,accion,usuarios=[]):
        self._nombre = nombre
        self._apellido = apellido
        self._posicion = posicion
        self._accion = accion
        self._correo = correo
        self.crear=crearDB()
        if self._accion == 'Guardar':
            self.guardarDatos()
            print('Datos Guardados')
        elif self._accion == 'Eliminar':
            self.eliminarDatos()
            print('Datos Eliminados')
            
    def guardarDatos(self):
        try:
            if self._posicion == 'Project Manager':
                self.conexion = conectar()
                c = self.conexion.conn.cursor()
                c.execute("INSERT INTO PM (nombre, apellido, correo, posicion) VALUES (?, ?, ?, ?)",
                        (self._nombre, self._apellido, self._correo, self._posicion))
                self.conexion.conn.commit()
                self.conexion.conn.close()
            elif self._posicion == 'Comercial Project Manager':
                self.conexion = conectar()
                c = self.conexion.conn.cursor()
                c.execute("INSERT INTO CPM (nombre, apellido, correo, posicion) VALUES (?, ?, ?, ?)",
                        (self._nombre, self._apellido, self._correo, self._posicion))
                self.conexion.conn.commit()
                self.conexion.conn.close()
            else:
                print('Elija una posicion Valida')
                self.conexion.conn.close()
                
        except Exception as e:
            print(e)
            print('Error en pmDatos.py')
            self.conexion.conn.close()
            
    def eliminarDatos(self):
        try:
            if self._posicion == 'Project Manager':
                print(self._correo)
                self.conexion = conectar()
                c = self.conexion.conn.cursor()
                c.execute("DELETE FROM PM WHERE nombre = ? AND apellido = ? AND correo = ? AND posicion = ?",
                          (self._nombre, self._apellido, self._correo, self._posicion))
                self.conexion.conn.commit()
                self.conexion.conn.close()
                
            elif self._posicion == 'Comercial Project Manager':
                self.conexion = conectar()
                c = self.conexion.conn.cursor()
                c.execute("DELETE FROM CPM WHERE nombre = ? AND apellido = ? AND correo = ? AND posicion = ?",
                          (self._nombre, self._apellido, self._correo, self._posicion))
                self.conexion.conn.commit()
                self.conexion.conn.close()
            else:
                print('Elija una posicion Valida')
        except Exception as e:
            print(e)
            print('Error en la eliminación de usuarios')
        
class buscar_PMDatos():
    def __init__(self):
        try:
            self.conexion = conectar()
            c = self.conexion.conn.cursor()
            c.execute("SELECT nombre, apellido, correo, posicion FROM PM")
            usuarios = c.fetchall()
            self.Lista_PM=[]
            for usuario in usuarios:
                self.Lista_PM.append(usuario[0]+' '+usuario[1])
            self.conexion.conn.close()
        except Exception as e:
            print(e)
            print('Error en la busqueda de datos')
            self.conexion.conn.close()
            
class buscar_CPMDatos():
    def __init__(self):
        try:
            self.conexion = conectar()
            c = self.conexion.conn.cursor()
            c.execute("SELECT nombre, apellido, correo, posicion FROM CPM")
            usuarios = c.fetchall()
            self.Lista_CPM=[]
            for usuario in usuarios:
                self.Lista_CPM.append(usuario[0]+' '+usuario[1])
            self.conexion.conn.close()
        except Exception as e:
            print(e)
            print('Error en la busqueda de datos')
            self.conexion.conn.close()