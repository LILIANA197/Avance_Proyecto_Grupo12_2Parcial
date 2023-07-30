from Proyecto.dominio.material import Material
# Arriaga Sanchez Genesis, Bajaña Tarira Jenniffer, Landazuri Barcia Liliana, Mieles Piloso Andrews, Vera Saltos Jimmy


class Revista(Material):
    contador_revista = 0

    def __init__(self, codigo: str = None, autor: str = None, titulo: str = None, anio: int = None,
                 editorial: str = None, disponible: bool = None, cantidad_disponible: int = None,
                 tipo: str = None):
        super().__init__(codigo=codigo, autor=autor, titulo=titulo, anio=anio, editorial=editorial,
                         disponible=disponible, cantidad_disponible=cantidad_disponible)
        Revista.contador_revista += 1
        self._id = Revista.contador_revista
        self._tipo = tipo

    @property
    def id(self):
        return self._id

    # @id.setter
    # def id(self, email_cambiado):
    #     self._id = id

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    def actualizar_disponibilidad(self, disponible):
        self._disponible = disponible

    def __str__(self):
        return f"Codigo: {self._codigo}\nAutor: {self._autor}\nTitulo: {self._titulo}\nAño: {self._anio}\n" \
               f"Editorial: {self._editorial}\nDisponible: {self._disponible}\n" \
               f"Cantidad disponible: {self._cantidad_disponible}\nId:{self._id}\nTipo: {self._titulo}"


if __name__ == '__main__':
    revista1 = Revista(codigo=" 10.7560/IC47402", autor="Pierre Mounier Kuhn", titulo="Information & culture",
                       anio=2012, editorial="volume47_number4_2012", disponible=False, cantidad_disponible=0,
                       tipo="online")
    revista2 = Revista(codigo=" 10.7660/IC47702", autor="Smith J.M.& Davis H.",
                       titulo="Language acquisition among autistic children", anio=2019,
                       editorial="volume5_Issue2_2011", disponible=True, cantidad_disponible=104, tipo="online")

    print('*'.center(100, '*'))
    print(revista1)
    print('*'.center(100, '*'))
    print(revista2)