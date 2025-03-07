from Computadora import Computadora
class Orden(Computadora):
    _contador_orden = 0
    _id_orden = 0
    _computadoras = {Computadora}

    def __init__(self, computadoras):
        Orden._contador_orden += 1
        self.id_orden = Orden._contador_orden
        self._computadoras = computadoras

    def __str__(self):
        return f'''
           '''

    @property
    def id_orden(self):
        return self._id_orden

    @id_orden.setter
    def id_orden(self, id):
        self._id_orden = id

    @property
    def computadoras(self):
        return self._computadoras

    @computadoras.setter
    def computadoras(self, computadoras):
        self._computadoras = computadoras

    def agregar_computadora(self, computadora):
        self._computadoras.append(computadora)

    def __str__(self):
        computadoras_str = ''
        for computadora in self._computadoras:
            computadoras_str += '\n' + computadora.__str__()

        return f'''Orden: {self._id_orden}
        Computadoras: {computadoras_str}'''