from Proyecto.dominio.persona import Persona1
# Arriaga Sanchez Genesis, Bajaña Tarira Jenniffer, Landazuri Barcia Liliana, Mieles Piloso Andrews, Vera Saltos Jimmy

class Docente(Persona1):
    contador_docente = 0

    def __init__(self, cedula: str = None, nombre: str = None, apellido: str = None, email: str = None,
                 telefono: str = None, direccion: str = None, carrera: str = None,  numero_libros: int = 0,
                 activo: bool = True, titulo_3er_nivel: str = None, titulo_4to_nivel: str = None):
        super().__init__(cedula=cedula, nombre=nombre, apellido=apellido, email=email, telefono=telefono,
                         direccion=direccion, carrera=carrera, numero_libros=numero_libros, activo=activo)
        Docente.contador_docente += 1
        self._id = Docente.contador_docente
        self._titulo_3er_nivel = titulo_3er_nivel
        self._titulo_4to_nivel = titulo_4to_nivel

    @property
    def id(self):
        return self._id

    # @id.setter
    # def id(self, email_cambiado):
    #     self._id = id

    @property
    def titulo_3er_nivel(self):
        return self._titulo_3er_nivel

    @titulo_3er_nivel.setter
    def titulo_3er_nivel(self, titulo_3er_nivel):
        self._titulo_3er_nivel = titulo_3er_nivel

    @property
    def titulo_4to_nivel(self):
        return self._titulo_4to_nivel

    @titulo_4to_nivel.setter
    def titulo_4to_nivel(self, titulo_4to_nivel):
        self._titulo_4to_nivel = titulo_4to_nivel

    def pedir_libro(self):
        if self.activo and self.numero_libros < 3:
            self.numero_libros += 1
            return True
        return False

    def devolver_libro(self):
        if self.activo and self.numero_libros > 0:
            self.numero_libros -= 1
            return True
        return False

    def __str__(self):
        return f"Cédula: {self._cedula}\nNombre: {self._nombre}\nApellido: {self._apellido}\nEmail: {self._email}\n" \
               f"Teléfono: {self._telefono}\nDirección: {self._direccion}\nNúmero de libros: {self._numero_libros}" \
               f"\nActivo: {self._activo}\nCarrera: {self._carrera}\nId: {self._id}\n" \
               f"Titulo 3ª nivel: {self._titulo_3er_nivel}\nTitulo 4ª nivel: {self._titulo_4to_nivel}"


if __name__ == '__main__':
    doc1= Docente(cedula="0123457759", nombre="Marcelo", apellido= "Villalba", email="Marcelo@gmail.com",
                  telefono="0944563344", direccion="Avenida El Ejercito", numero_libros=2, activo=True,
                   carrera="Finanzas", titulo_3er_nivel="Licenciatura en Contaduria ",
                   titulo_4to_nivel="Magister en Finanzas")
    doc2= Docente(cedula="0964553423", nombre="Jessica", apellido= "Moncada", email="Jessica@gmail.com",
                  telefono="0960356422", direccion="Avenida Juan TancaMarengo", numero_libros=4, activo=False,
                  carrera="Psicologia", titulo_3er_nivel="Licenciada en Psicopedagogia",
                  titulo_4to_nivel="Magister en estudios sociales")
    print('*'.center(100, '*'))
    print(doc1)
    print('*'.center(100, '-'))
    print(doc2)
