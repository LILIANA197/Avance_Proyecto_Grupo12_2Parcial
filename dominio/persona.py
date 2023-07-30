from abc import ABC, abstractmethod
# Arriaga Sanchez Genesis, Bajaña Tarira Jenniffer, Landazuri Barcia Liliana, Mieles Piloso Andrews, Vera Saltos Jimmy


class Persona1(ABC):

    def __init__(self, cedula: str = None, nombre: str = None, apellido: str = None, email: str = None,
                 telefono: str = None, direccion: str = None, carrera: str = None,  numero_libros: int = 0,
                 activo: bool = True):
        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._telefono = telefono
        self._direccion = direccion
        self._carrera = carrera
        self._numero_libros = numero_libros
        self._activo = activo


    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, telefono):
        self._telefono = telefono

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, direccion):
        self._direccion = direccion

    @property
    def carrera(self):
        return self._carrera

    @carrera.setter
    def carrera(self, carrera):
        self._carrera = carrera

    @property
    def numero_libros(self):
        return self._numero_libros

    @numero_libros.setter
    def numero_libros(self, numero_libros):
        self._numero_libros = numero_libros

    @property
    def activo(self):
        return self._activo

    @activo.setter
    def activo(self, activo):
        self._activo = activo

    # @abstractmethod
    def pedir_libro(self):
        pass

    # @abstractmethod
    def devolver_libro(self):
        pass

    def __str__(self):
        return f"Cédula: {self._cedula}\nNombre: {self._nombre}\nApellido: {self._apellido}\nEmail: {self._email}\n" \
               f"Teléfono: {self._telefono}\nDirección: {self._direccion}\nNúmero de libros: {self._numero_libros}" \
               f"\nActivo: {self._activo}\nCarrera: {self._carrera}"


if __name__ == '__main__':
    pass
