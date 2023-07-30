from Proyecto.dominio.material import Material
# Arriaga Sanchez Genesis, Bajaña Tarira Jenniffer, Landazuri Barcia Liliana, Mieles Piloso Andrews, Vera Saltos Jimmy


class Libro(Material):
    contador_libro = 0

    def __init__(self, codigo: str = None, autor: str = None, titulo: str = None, anio: int = None,
                 editorial: str = None, disponible: bool = None, cantidad_disponible: int = None,
                 tipo_pasta: str = None):
        super().__init__(codigo=codigo, autor=autor, titulo=titulo, anio=anio, editorial=editorial,
                         disponible=disponible, cantidad_disponible=cantidad_disponible)
        Libro.contador_libro += 1
        self._id = Libro.contador_libro
        self._tipo_pasta = tipo_pasta

    @property
    def id(self):
        return self._id

    # @id.setter
    # def id(self, email_cambiado):
    #     self._id = id

    @property
    def tipo_pasta(self):
        return self._tipo_pasta

    @tipo_pasta.setter
    def tipo_pasta(self, tipo_pasta):
        self._tipo_pasta = tipo_pasta

    def actualizar_disponibilidad(self, disponible):
        self._disponible = disponible

    def __str__(self):
        return f"Codigo: {self._codigo}\nAutor: {self._autor}\nTitulo: {self._titulo}\nAño: {self._anio}\n" \
               f"Editorial: {self._editorial}\nDisponible: {self._disponible}\n" \
               f"Cantidad disponible: {self._cantidad_disponible}\nId:{self._id}\nTipo de pasta: {self._tipo_pasta}"


if __name__ == '__main__':
    libro1 = Libro(codigo="620.1/C87", autor="Craig Jr Roy", titulo="Mecanica de materiales", anio=2002,
                   editorial="continental", disponible=True, cantidad_disponible=30, tipo_pasta="cubierta carton")
    libro2 = Libro(codigo="doi12.123", autor="McGoldrick J.Giordano",
                   titulo="Back to the future:An examination of the native american holocaust experience",
                   anio=2002, editorial="tercera edicion", disponible=False, cantidad_disponible=0,
                   tipo_pasta="Electronico")
    print('*'.center(100, '*'))
    print(libro1)
    print('*'.center(100, '*'))
    print(libro2)


