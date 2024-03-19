import sqlite3

class crearDB():
    def __init__(self):
        try:
            # Conectar a la base de datos (creará un archivo si no existe)
            self.conn = sqlite3.connect('/Volumes/Choco/Python/GestionDoc/GUI/Datos/Model/ProjectManagement.db')
            # Crear un cursor para ejecutar comandos SQL
            print('Conexión exitosa')
            self.crear_tabla()
            
        except sqlite3.OperationalError as error:
            print(error)
        except Exception as e:          
            print(e)
            print('Error en crearDB.py')
        
    def crear_tabla(self):
        tablaPm=('''
                CREATE TABLE IF NOT EXISTS PM (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT,
                    apellido TEXT,
                    correo TEXT UNIQUE,
                    posicion TEXT
                )
            ''')
        tablaCpm=('''
                CREATE TABLE IF NOT EXISTS CPM (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT,
                    apellido TEXT,
                    correo TEXT UNIQUE,
                    posicion TEXT
                )
            ''')

        # Crear la tabla para almacenar los datos
        cursor = self.conn.cursor()
        cursor.execute(tablaPm)
        cursor.execute(tablaCpm)
            
        # Guardar los cambios y cerrar la conexión
        self.conn.commit()   
        self.conn.close()

class conectar():
    def __init__(self):
        self.conn = sqlite3.connect('/Volumes/Choco/Python/GestionDoc/GUI/Datos/Model/ProjectManagement.db')
