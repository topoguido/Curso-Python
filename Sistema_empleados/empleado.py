class Empleado:
    contador_empleados = 0

    def __init__(self):

        self.__nombre = ''
        self.__departamento = ''

    @property
    def nombre(self):
        return self.__nombre

    @property
    def departamento(self):
        return self.__departamento

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @departamento.setter
    def departamento(self, depto):
        self.__departamento = depto


    @classmethod
    def get_total_empleados(cls):
        return cls.contador_empleados