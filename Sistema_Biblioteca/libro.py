class Libro:
    def __init__(self, titulo, autor, genero):
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero


    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor

    @property
    def genero(self):
        return self.__genero

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @autor.setter
    def autor(self, autor):
        self.__autor = autor

    @genero.setter
    def genero(self, genero):
        self.__genero = genero
