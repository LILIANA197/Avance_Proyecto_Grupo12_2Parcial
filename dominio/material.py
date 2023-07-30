from abc import ABC


# Arriaga Sanchez Genesis, Bajaña Tarira Jenniffer, Landazuri Barcia Liliana, Mieles Piloso Andrews, Vera Saltos Jimmy


class Material(ABC):
    def __init__(self, codigo: str = None, autor: str = None, titulo: str = None, anio: int = None,
                 editorial: str = None, disponible: bool = None, cantidad_disponible: int = None):
        self._codigo = codigo
        self._autor = autor
        self._titulo = titulo
        self._anio = anio
        self._editorial = editorial
        self._disponible = disponible
        self._cantidad_disponible = cantidad_disponible

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, autor):
        self._autor = autor

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    @property
    def anio(self):
        return self.anio

    @anio.setter
    def anio(self, anio):
        self._anio = anio

    @property
    def editorial(self):
        return self._editorial

    @editorial.setter
    def editorial(self, editorial):
        self._editorial = editorial

    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, disponible):
        self._disponible = disponible

    @property
    def cantidad_disponible(self):
        return self._cantidad_disponible

    @cantidad_disponible.setter
    def cantidad_disponible(self, cantidad_disponible):
        self._cantidad_disponible = cantidad_disponible

    # @abstractmethod
    def actualizar_disponibilidad(self, disponible):
        self._disponible = disponible
        pass

    def _str_(self):
        return f"Codigo: {self._codigo}\nAutor: {self._autor}\nTitulo: {self._titulo}\nAño: {self._anio}\n" \
               f"Editorial: {self._editorial}\nDisponible: {self._disponible}\n" \
               f"Cantidad disponible: {self._cantidad_disponible}"


if __name__ == '__main__':
    pass


