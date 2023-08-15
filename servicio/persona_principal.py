# Arriaga Sanchez Genesis, Bajaña Tarira Jenniffer, Landazuri Barcia Liliana,
# Mieles Piloso Andrews, Vera Saltos Jimmy
import statistics

from Proyecto.UI.vtn_principal import Ui_vtn_principal
from Proyecto.datos.estudiante_dao import EstudianteDao
from Proyecto.dominio.docente import Docente
from Proyecto.dominio.estudiante import Estudiante
from PySide6 import QtGui
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import QDate


class PersonaPrincipal(QMainWindow):
    def __init__(self):
        super(PersonaPrincipal, self).__init__()
        self.ui = Ui_vtn_principal()
        self.ui.setupUi(self)
        self.ui.stb_estado.showMessage('Bienvenido', 2000)
        # self.ui.lbl_nombre.setText('Primer Nombre:')
        self.ui.btn_grabar.clicked.connect(self.grabar)
        self.ui.btn_buscar_cedula.clicked.connect(self.buscar_x_cedula)
        self.ui.dae_fecha_nacimiento.setDate(QDate.currentDate())
        self.ui.btn_cal_edad.clicked.connect(self.calcular_edad)
        self.ui.btn_estatura.clicked.connect(self.calculos_estatura)
        self.ui.btn_peso.clicked.connect(self.calculos_peso)
        self.ui.btn_edad.clicked.connect(self.calculos_edades)
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
                persona.cedula = self.ui.txt_cedula.text()
                persona.nombre = self.ui.txt_nombre.text()
                persona.apellido = self.ui.txt_apellido.text()
                persona.email = self.ui.txt_email.text()
                persona.carrera = self.ui.txt_carrera.text()
                persona.fecha_nacimiento = self.ui.dae_fecha_nacimiento.text()
                persona.edad = self.ui.sp_edad.setValue()
                persona.estatura = self.ui.sp_estatura.text()
                persona.peso = self.ui.sp_peso.text()

            else:
                persona = Estudiante()
                persona.cedula = self.ui.txt_cedula.text()
                persona.nombre = self.ui.txt_nombre.text()
                persona.apellido = self.ui.txt_apellido.text()
                persona.email = self.ui.txt_email.text()
                persona.carrera = self.ui.txt_carrera.text()
                persona.fecha_nacimiento = self.ui.dae_fecha_nacimiento.text()
                persona.edad = self.ui.sp_edad.text()
                persona.estatura = self.ui.sp_estatura.text()
                persona.peso = self.ui.sp_peso.text()
                # Insertar en la base de datos al estudiante
                respuesta = None
                respuesta = EstudianteDao.insertar_estudiante(persona)
                # try:
                #     respuesta = EstudianteDao.insertar_estudiante(persona)
                # except Exception as e:
                #     print(e)
            try:
                fecha_nacimiento_str = self.ui.dae_fecha_nacimiento.text()
                fecha_nacimiento = QDate.fromString(fecha_nacimiento_str, 'dd-MM-yyyy')
                persona.fecha_nacimiento = fecha_nacimiento
            except Exception as e: # Manejo de excepciones
                pass
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
                self.ui.txt_cedula.setText('')
                self.ui.txt_nombre.setText('')
                self.ui.txt_apellido.setText('')
                self.ui.txt_email.setText('')
                self.ui.txt_carrera.setText('')
                self.ui.dae_fecha_nacimiento.setDate(QDate())
                self.ui.sp_edad.setValue(0)
                self.ui.sp_estatura.setValue(0)
                self.ui.sp_peso.setValue(0)
                self.ui.stb_estado.showMessage('Grabado con exito.', 3000)
            else:
                QMessageBox.critical(self, 'Error', respuesta['mensaje'])

    def buscar_x_cedula(self):
        cedula = self.ui.txt_cedula.text()
        e = Estudiante(cedula=cedula)
        e = EstudianteDao.seleccionar_por_cedula(e)
        print(e)
        self.ui.txt_nombre.setText(e.nombre)
        self.ui.txt_apellido.setText(e.apellido)
        self.ui.txt_email.setText(e.email)
        self.ui.txt_carrera.setText(e.carrera)
        self.ui.dae_fecha_nacimiento.setDate(e.fecha_nacimiento)
        if isinstance(e.edad, int):
            self.ui.sp_edad.setValue(e.edad)
        else:
            self.ui.sp_edad.clear()
        if isinstance(e.estatura, int):
            self.ui.sp_estatura.setValue(e.estatura)
        else:
            self.ui.sp_estatura.clear()
        if isinstance(e.peso, int):
            self.ui.sp_peso.setValue(e.peso)
        else:
            self.ui.sp_peso.clear()
        # self.ui.sp_estatura.setValue(e.estatura)
        # self.ui.sp_peso.setValue(e.peso)
        self.ui.cb_tipo_persona.setCurrentText('Estudiante')
        self.ui.cb_tipo_habilitado.setCurrentText('Si')

    def calculos_estatura(self):
        estudiantes = EstudianteDao.seleccionar_estudiantes()
        cantidad_estudiantes = len(estudiantes)
        suma_estaturas = 0
        estaturas = [estudiante.estatura for estudiante in estudiantes]
        for estudiante in estudiantes:
            suma_estaturas += estudiante.estatura
        promedio_estatura = suma_estaturas / cantidad_estudiantes
        media_estatura = statistics.median(estaturas)
        moda_estatura = statistics.mode(estaturas)
        min_estatura = min(estaturas)
        max_estatura = max(estaturas)
        print('*'.center(100, '*'))
        print('-CALCULOS DE ESTATURA:')
        print('*'.center(100, '*'))
        print(f'El promedio de estaturas es: {promedio_estatura}')
        print(f'La moda de estatura es : {moda_estatura}')
        print(f'La media de estaturas es: {media_estatura}')
        print(f'La mínima de estatura es: {min_estatura}')
        print(f'La  máxima de estatura es: {max_estatura}')

    def calculos_peso(self):
        estudiantes = EstudianteDao.seleccionar_estudiantes()
        cantidad_estudiantes = len(estudiantes)
        suma_pesos = 0
        pesos = [estudiante.peso for estudiante in estudiantes]
        for estudiante in estudiantes:
            suma_pesos += estudiante.peso
        promedio_peso = suma_pesos / cantidad_estudiantes
        media_peso = statistics.median(pesos)
        moda_peso = statistics.mode(pesos)
        min_peso = min(pesos)
        max_peso = max(pesos)
        print('*'.center(100, '*'))
        print('-CALCULOS DE PESO:')
        print('*'.center(100, '*'))
        print(f'El promedio de peso es: {promedio_peso}')
        print(f'La media de peso es: {media_peso}')
        print(f'La moda de peso es: {moda_peso}')
        print(f'La mínima de peso es: {min_peso}')
        print(f'La  máxima de peso es: {max_peso}')

    def calcular_edad(self):
        fecha_nacimiento = self.ui.dae_fecha_nacimiento.date()
        # Obtener la fecha actual
        fecha_actual = QDate.currentDate()
        # Calcular la diferencia de años
        diferencia_anios = fecha_actual.year() - fecha_nacimiento.year()
        # Verificar si aún no ha pasado el cumpleaños de este año
        if (fecha_actual.month(), fecha_actual.day()) < (fecha_nacimiento.month(), fecha_nacimiento.day()):
            diferencia_anios -= 1
        # Establecer la edad en el QSpinBox
        self.ui.sp_edad.setValue(diferencia_anios)

    def calculos_edades(self):
        estudiantes = EstudianteDao.seleccionar_estudiantes()
        cantidad_estudiantes = len(estudiantes)
        suma_edades = 0
        for estudiante in estudiantes:
            suma_edades += estudiante.edad
        promedio_edades = suma_edades / cantidad_estudiantes
        edades = [estudiante.edad for estudiante in estudiantes]
        media_edad = statistics.median(edades)
        moda_edad = statistics.mode(edades)
        min_edad = min(edades)
        max_edad = max(edades)
        print('*'.center(100, '*'))
        print('-CALCULOS DE EDAD:')
        print('*'.center(100, '*'))
        print(f'El promedio de edad es: {promedio_edades}')
        print(f'La media de edades es: {media_edad}')
        print(f'La moda de edades es: {moda_edad}')
        print(f'La mínima de edades es: {min_edad}')
        print(f'La  máxima de edades es: {max_edad}')


