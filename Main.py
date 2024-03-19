from PyQt6.uic.load_ui import loadUi
from PyQt6.QtWidgets import QMessageBox
from RegistrarPM import registrarPm
from UsuariosBD import BusquedaDB
from Datos.pmDatos import buscar_CPMDatos, buscar_PMDatos


try:   
    class mainWindow():
        def __init__(self):
            self.main=loadUi('/Volumes/Choco/Python/GestionDoc/GUI/Gestion_Documental.ui')
            self.main.show()
            self.main.btnAgregarPM.clicked.connect(lambda:self.abrirRegistrarPM('PM'))
            self.main.btnAgregarCPM.clicked.connect(lambda:self.abrirRegistrarPM('CPM'))
            self.main.btnEliminarPM.clicked.connect(lambda:self.abrirEliminarUsuario('PM'))
            self.main.btnEliminarCPM.clicked.connect(lambda:self.abrirEliminarUsuario('CPM'))
            
            self.Buscar_PMDatos=self.BuscarPM()
            self.Lista_PM=self.Buscar_PMDatos
            if self.Lista_PM != None:
                self.main.Lista_PM.addItems(self.Lista_PM)
            else:
                QMessageBox.warning(self,'Error','No hay PM registrados')
                
            self.Buscar_CPMDatos=self.BuscarCPM()
            self.Lista_CPM=self.Buscar_CPMDatos
            if self.Lista_CPM != None:
                self.main.Lista_CPM.addItems(self.Lista_CPM)
            else:
                QMessageBox.warning(self,'Error','No hay CPM registrados')
            
            self.main.NPEP.textChanged.connect(self.nombreCarpeta)              
        
        def nombreCarpeta(self):
            PEP=self.main.NPEP.text()
            Nombre = self.main.Lista_PM.currentText()
            NombreSeparado=Nombre.split(' ')
            Nombre=NombreSeparado[0]
            Apellido=NombreSeparado[1]
            INombre=Nombre[0]
            IApe=Apellido[0]
            NombreCarpeta=PEP + '-' + INombre + IApe +'- Nombre del Proyecto'
            self.main.labelNombreCarpeta.setText(NombreCarpeta)
        
        def abrirRegistrarPM(self,tipo):
            tipo=tipo
            self.registrarPM=registrarPm(tipo)
            self.main.hide()
            
        def abrirEliminarUsuario(self,tipo):
            tipo=tipo
            self.eliminarUsuario=BusquedaDB(tipo)
            self.main.hide()
            
        def BuscarPM(self):
            self.lista=buscar_PMDatos()
            self.resultado=self.lista.Lista_PM
            return self.resultado
        
        def BuscarCPM(self):
            self.lista=buscar_CPMDatos()
            self.resultado=self.lista.Lista_CPM
            return self.resultado      
except Exception as e:
    print(e)
    print('Error en Main.py')