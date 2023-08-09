from Proyecto.UI.vtn_principal import Ui_vtn_principal
from Proyecto.datos.estudiante_dao import EstudianteDao
from Proyecto.dominio.docente import Docente
from Proyecto.dominio.estudiante import Estudiante
from PySide6 import QtGui
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QMainWindow, QMessageBox


class PersonaPrincipal(QMainWindow):
    def __init__(self):
        super(PersonaPrincipal, self).__init__()
        self.ui = Ui_vtn_principal()
        self.ui.setupUi(self)
        self.ui.stb_estado.showMessage('Bienvenido', 2000)
        # self.ui.lbl_nombre.setText('Primer Nombre:')
        self.ui.btn_grabar.clicked.connect(self.grabar)
        self.ui.btn_buscar_cedula.clicked.connect(self.busca_x_cedula)
        self.ui.txt_cedula.setValidator(QtGui.QIntValidator())

        correo_exp = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        validator = QRegularExpressionValidator(correo_exp, self)
        self.ui.txt_email.setValidator(validator)

    def grabar(self):
        tipo_persona = self.ui.cb_tipo_persona.currentText()
        if (self.ui.txt_nombre.text() == '' or self.ui.txt_apellido.text() == '' or len(self.ui.txt_cedula.text()) < 10
                or self.ui.txt_email.text() == ''):
            print('Completar datos')
            QMessageBox.warning(self, 'Advertencia', 'Falta de llenar los datos obligatorios.')
        else:
            persona = None
            if tipo_persona == 'Docente':
                persona = Docente()
                persona.nombre = self.ui.txt_nombre.text()
                persona.apellido = self.ui.txt_apellido.text()
                persona.cedula = self.ui.txt_cedula.text()
                persona.email = self.ui.txt_email.text()
            else:
                persona = Estudiante()
                persona.nombre = self.ui.txt_nombre.text()
                persona.apellido = self.ui.txt_apellido.text()
                persona.cedula = self.ui.txt_cedula.text()
                persona.email = self.ui.txt_email.text()
                #Insertar en la base de datos al estudiante
                respuesta = None
                respuesta = EstudianteDao.insertar_estudiante(persona)
                # try:
                #     respuesta = EstudianteDao.insertar_estudiante(persona)
                # except Exception as e:
                #     print(e)
            # print(tipo_persona)
            # print(persona)
            # archivo = None
            # try:
            #     archivo = open('archivo.txt', mode='a')
            #     archivo.write(persona.__str__())
            #     archivo.write('\n')
            #     archivo.write('*'.center(100, '*'))
            #     archivo.write('\n')
            # except Exception as e:
            #     print('No se pudo grabar')
            # finally:
            #     if archivo:
            #         archivo.close()
            if respuesta['exito']:
                self.ui.txt_nombre.setText('')
                self.ui.txt_apellido.setText('')
                self.ui.txt_cedula.setText('')
                self.ui.txt_email.setText('')
                self.ui.stb_estado.showMessage('Grabado con exito.', 2000)
            else:
                QMessageBox.critical(self, 'Error', respuesta['mensaje'])

    def busca_x_cedula(self):
        cedula = self.ui.txt_cedula.text()
        e = Estudiante(cedula=cedula)
        e = EstudianteDao.seleccionar_por_cedula(e)
        print(e)
        self.ui.txt_nombre.setText(e.nombre)
        self.ui.txt_apellido.setText(e.apellido)
        self.ui.txt_email.setText(e.email)
        self.ui.cb_tipo_persona.setCurrentText('Estudiante')

