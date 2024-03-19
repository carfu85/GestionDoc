from PyQt6.uic.load_ui import loadUi
from PyQt6.QtWidgets import QMessageBox
from Datos.pmDatos import PmDatos
from PyQt6.QtGui import QCloseEvent

class registrarPm():
    def __init__(self, tipo):
        self.rPM=loadUi('/Volumes/Choco/Python/GestionDoc/GUI/RegistrarPM.ui')
        self.rPM.lineNombre.setText('')
        self.rPM.lineApellido.setText('')
        self.rPM.lineCorreo.setText('')
        self.rPM.show()
        self.rPM.Registrar.clicked.connect(lambda:self.registrar(tipo))

        
    def registrar(self,tipo):
        from Main import mainWindow
        nombre=self.rPM.lineNombre.text()
        apellido=self.rPM.lineApellido.text()
        correo=self.rPM.lineCorreo.text()
        if tipo=='PM':
            if self.rPM.Cposicion.currentText()== 'Project Manager':
                posicion=self.rPM.Cposicion.currentText()
            else:
                self.qm = QMessageBox()
                self.qm.setWindowTitle('Posicion Incorrecta')
                self.qm.setIcon(QMessageBox.Icon.Warning)
                self.qm.setText('Como elegiste Agregar PM, se registrará como Project Manager')
                self.qm.exec()
                print('Tienes que elegir Project Manager')
                self.rPM.Cposicion.setCurrentText('Project Manager')
                posicion=self.rPM.Cposicion.currentText()
        elif tipo=='CPM':
            if self.rPM.Cposicion.currentText()== 'Comercial Project Manager':
                posicion=self.rPM.Cposicion.currentText()
            else:
                self.qm=QMessageBox()
                self.qm.setWindowTitle('Posicion Incorrecta')
                self.qm.setIcon(QMessageBox.Icon.Warning)
                self.qm.setText('Como elegiste Agregar CPM, se registrara como Comercial Project Manager')
                self.qm.exec()
                self.rPM.Cposicion.setCurrentText('Comercial Project Manager')
                posicion=self.rPM.Cposicion.currentText()
        else:
            print('Esa posicion no existe')
        self.datos=PmDatos(nombre, apellido, correo, posicion, 'Guardar')
        self.rPM.close()
        self.mostrar=mainWindow()
        self.mostrar.main.show()    
    
    def closeEvent(self, event: QCloseEvent):
        from Main import mainWindow
        self.Buscar.hide()
        self.main = mainWindow()
        self.main.show()