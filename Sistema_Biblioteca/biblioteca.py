import json

from libro import Libro

class Biblioteca:
    def __init__(self):
        self._id = 0
        self._libros = []

    @property
    def id(self):
         return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def libros(self) -> [Libro]:
        return self._libros

    @libros.setter
    def libros(self, libros: list[Libro]):
        self._libros = libros

    @property
    def libro(self, libro: Libro) -> Libro:
        for _libro in self.libros:
            if _libro == libro:
                return _libro

    def buscar_libros_por_autor(self, autor) -> [Libro]:
        libro_return = []
        for libro in self._libros:
            if libro.autor == autor:
                libro_return.append(libro)
        return libro_return

    def buscar_libros_por_genero(self, genero) -> [Libro]:
        libro_return = []
        for libro in self._libros:
            if libro.genero == genero:
                libro_return.append(libro)
        return libro_return

    def agregar_libro(self, libro):
        self._libros.append(libro)




