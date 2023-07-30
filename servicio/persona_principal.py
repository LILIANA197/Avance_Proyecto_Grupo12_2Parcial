from Proyecto.UI.vtn_principal import Ui_vtn_principal
from Proyecto.dominio.docente import Docente
from Proyecto.dominio.estudiante import Estudiante
from PySide6.QtWidgets import QMainWindow


class PersonaPrincipal(QMainWindow):
    def __init__(self):
        super(PersonaPrincipal, self).__init__()
        self.ui = Ui_vtn_principal()
        self.ui.setupUi(self)
        self.ui.stb_estado.showMessage('Bienvenido', 2000)
        # self.ui.lbl_nombre.setText('Primer Nombre:')
        self.ui.btn_grabar.clicked.connect(self.grabar)

    def grabar(self):
        tipo_persona = self.ui.cb_tipo_persona.currentText()
        if tipo_persona == 'Docente':
            persona = Docente()
            persona.nombre = self.ui.txt_nombre.text()
            persona.apellido = self.ui.txt_apellido.text()

        else:
            persona = Estudiante()
            persona.nombre = self.ui.txt_nombre.text()
            persona.apellido = self.ui.txt_apellido.text()
        # print(tipo_persona)
        # print(persona)

        archivo = None
        try:
            archivo = open('archivo.txt', mode='a')
            archivo.write(persona.__str__())
            archivo.write('\n')
            archivo.write('*'.center(100, '*'))
            archivo.write('\n')
        except Exception as e:
            print('No se pudo grabar')
        finally:
            if archivo:
                archivo.close()
        self.ui.txt_nombre.setText('')
        self.ui.txt_apellido.setText('')
        self.ui.stb_estado.showMessage('Grabado con exito.', 2000)
