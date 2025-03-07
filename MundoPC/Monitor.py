class Monitor:
    _contador_monitor = 0
    _id_monitor = 0
    _marca = ''
    _tamanio = 0

    def __init__(self, marca, tamanio):
        Monitor._contador_monitor += 1
        self._id_monitor = Monitor._contador_monitor
        self._marca = marca
        self._tamanio = tamanio

    def __str__(self):
        return f'''
        Id: {self._id_monitor}
        Marca: {self._marca}
        Tamaño: {self._tamanio}'''

    @property
    def id_monitor(self):
        return self._id_monitor

    @id_monitor.setter
    def id_monitor(self, id):
        self._id_monitor= id

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def tamanio(self):
        return self._tamanio

    @tamanio.setter
    def tamanio(self, tamanio):
        self._tamanio = tamanio


if __name__ == '__main__':
    monitor1 = Monitor('HP', 17)
    print(monitor1)
    monitor2 = Monitor('Samsung', 22)
    print(monitor2)