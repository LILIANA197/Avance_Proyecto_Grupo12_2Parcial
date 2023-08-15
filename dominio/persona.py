from abc import ABC, abstractmethod
# Arriaga Sanchez Genesis, Bajaña Tarira Jenniffer, Landazuri Barcia Liliana,
# Mieles Piloso Andrews, Vera Saltos Jimmy

class Persona1(ABC):

    def __init__(self, cedula: str, nombre: str, apellido: str, email: str,
                 telefono: str, direccion: str, carrera: str, numero_libros: int,
                 activo: bool, fecha_nacimiento: int, edad: int, estatura: int, peso:int):
        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._fecha_nacimiento = fecha_nacimiento
        self._edad = edad
        self._estatura = estatura
        self._peso = peso
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
    def fecha_nacimento(self):
        return self._fecha_nacimiento

    @fecha_nacimento.setter
    def fecha_nacimiento(self, fecha_nacimiento):
        self._fecha_nacimiento = fecha_nacimiento

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @property
    def estatura(self):
        return self._estatura

    @estatura.setter
    def estatura(self, estatura):
        self._estatura = estatura

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, peso):
        self._peso = peso

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
        return (f"Cédula: {self._cedula}\nNombre: {self._nombre}\nApellido: {self._apellido}\n"
                f"Estatura: {self._estatura}\nEmail: {self._email}\nTeléfono: {self._telefono}\n"
                f"Dirección: {self._direccion}\nNúmero de libros: {self._numero_libros}\nActivo: {self._activo}"
                f"\nCarrera: {self._carrera}")


if __name__ == '__main__':
    pass
