from Monitor import Monitor
from Raton import Raton
from Teclado import Teclado

class Computadora():
    _contador_computadora = 0
    _id_computadora = 0
    _monitor = None
    _teclado = None
    _raton = None

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora._contador_computadora += 1
        self._id_computadora = Computadora._contador_computadora
        self._nombre = nombre
        self._monitor  = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f'''
        Nombre: {self._nombre}
        Id: {self._id_computadora}
        Monitor: {self.monitor}
        Teclado: {self.teclado}
        Raton: {self.raton}'''

    @property
    def contador_computadora(self):
        return self._contador_computadoras

    @contador_computadora.setter
    def contador_computadora(self, contador):
        self._contador_computadoras = contador

    @property
    def id_computadora(self):
        return self._id_computadora

    @id_computadora.setter
    def id_computadora(self, id):
        self._id_computadora = id

    @property
    def monitor(self):
        return self._monitor

    @monitor.setter
    def monitor(self, monitor):
        self._monitor = monitor

    @property
    def teclado(self):
        return self._teclado

    @teclado.setter
    def teclado(self, teclado):
        self._teclado = teclado

    @property
    def raton(self):
        return self._raton

    @raton.setter
    def raton(self, raton):
        self._raton = raton

if __name__ == '__main__':
    teclado1 = Teclado('Logitech', 'USB')
    raton1 = Raton('Logitech', 'Wireless')
    monitor1 = Monitor('Samsung', 22)
    computadora1 = Computadora('Propia', monitor1, teclado1, raton1)
    print(computadora1)