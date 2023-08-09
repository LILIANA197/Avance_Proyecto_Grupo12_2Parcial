# Arriaga Sanchez Genesis, Bajaña Tarira Jenniffer, Landazuri Barcia Liliana, Mieles Piloso Andrews, Vera Saltos Jimmy
import sys

from Proyecto.UI.vtn_principal import Ui_vtn_principal
from PySide6.QtWidgets import QApplication

from servicio.persona_principal import PersonaPrincipal

app = QApplication()
vtn_principal = PersonaPrincipal()
vtn_principal.show()
sys.exit(app.exec())


