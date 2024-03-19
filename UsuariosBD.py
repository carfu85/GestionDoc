import sqlite3
from PyQt6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt6.uic.load_ui import loadUi
from PyQt6.QtWidgets import QTableView, QApplication
from Datos.pmDatos import conectar
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox
from Datos.pmDatos import PmDatos

class BusquedaDB():
    def __init__(self,tipo):
        self.Buscardb=loadUi('/Volumes/Choco/Python/GestionDoc/GUI/BusquedaBD.ui')
        self.Buscardb.btnSeleccionar.hide()
        self.Buscardb.show()
        self.Buscardb.btnBuscar.clicked.connect(lambda:self.buscarDB(tipo))
    
    def buscarDB(self,tipo):
        self.nombre=self.Buscardb.lineNombre.text()
        self.apellido=self.Buscardb.lineApellido.text()
        if self.nombre=='':
            QMessageBox.information(self.Buscardb, 'Error', 'No se puede buscar con el campo Nombre vacio')
            self.Buscardb.lineNombre.setFocus()
            self.nombre=self.Buscardb.lineNombre.text()
        elif self.apellido=='':
            QMessageBox.information(self.Buscardb, 'Error', 'No se puede buscar solo con el Nombre')
            self.Buscardb.lineApellido.setFocus()
            self.nombre=self.Buscardb.lineApellido.text()
        else:
            self.modelo=self.modeloBD(tipo)

    def modeloBD(self,tipo):
        if tipo=='PM':
            try:
                self.db=conectar()
                cursor = self.db.conn.cursor()
                cursor.execute("SELECT * FROM PM WHERE nombre = ? AND apellido = ?",
                                (self.nombre, self.apellido))
                usuarios = cursor.fetchall()
                self.Buscardb.tableResultado.setRowCount(len(usuarios))
                self.Buscardb.tableResultado.setColumnCount(len(usuarios[0]))
                for i, usuario in enumerate(usuarios):
                    for j, dato in enumerate(usuario):
                        self.Buscardb.tableResultado.setItem(i, j, QTableWidgetItem(str(dato)))
                self.Buscardb.btnSeleccionar.show()
                self.Buscardb.btnSeleccionar.clicked.connect(self.seleccionar)
                self.db.conn.close()
            except sqlite3.Error as e:
                print(e)
                QMessageBox.warning(self.Buscardb, 'Error', 'Ha ocurrido un error en la base de datos')
                self.Buscardb.show()
            except Exception as e:
                from Main import mainWindow
                print(e)
                QMessageBox.warning(self.Buscardb, 'Error', 'No Hay datos en la base de datos')
                self.Buscardb.close()
                self.mostrar=mainWindow()
                self.mostrar.main.show()
            
        elif tipo=='CPM':
            try:
                self.db=conectar()
                cursor = self.db.conn.cursor()
                cursor.execute("SELECT * FROM CPM WHERE nombre = ? AND apellido = ?",
                                (self.nombre, self.apellido))
                usuarios = cursor.fetchall()
                self.Buscardb.tableResultado.setRowCount(len(usuarios))
                self.Buscardb.tableResultado.setColumnCount(len(usuarios[0]))
                for i, usuario in enumerate(usuarios):
                    for j, dato in enumerate(usuario):
                        self.Buscardb.tableResultado.setItem(i, j, QTableWidgetItem(str(dato)))
                self.Buscardb.btnSeleccionar.show()
                self.Buscardb.btnSeleccionar.clicked.connect(self.seleccionar)
                self.db.conn.close()
            except sqlite3.Error as e:
                print(e)
                QMessageBox.warning(self.Buscardb, 'Error', 'Ha ocurrido un error en la base de datos')
                self.Buscardb.show()
            except Exception as e:
                from Main import mainWindow
                print(e)
                QMessageBox.warning(self.Buscardb, 'Error', 'No Hay datos en la base de datos')
                self.Buscardb.close()
                self.mostrar=mainWindow()
                self.mostrar.main.show()
                
    def seleccionar(self):
        from Main import mainWindow
        items=self.Buscardb.tableResultado.selectedItems()
        if items:
            Lista_Seleccionado=[]
            for item in items:
                texto = item.text()
                Lista_Seleccionado.append(texto)
            nombre=Lista_Seleccionado[1].strip()
            apellido=Lista_Seleccionado[2].strip()
            correo=Lista_Seleccionado[3].strip()
            posicion=Lista_Seleccionado[4].strip()
            self.datos=PmDatos(nombre=nombre, apellido=apellido, posicion=posicion,correo=correo, accion='Eliminar')
            self.Buscardb.close()
            self.mostrar=mainWindow()
            self.mostrar.main.show()
        else:
            QMessageBox.warning(self.Buscardb, 'Error', 'No Hay datos seleccionados')
            self.Buscardb.close()
            self.mostrar=mainWindow()
            self.mostrar.main.show()

                
            