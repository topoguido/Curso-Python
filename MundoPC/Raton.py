from DispositivoEntrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    _contador_raton = 0
    _id_raton = 0

    def __init__(self, marca, tipo_entrada):
        Raton._contador_raton += 1
        self._id_raton = Raton._contador_raton
        self._marca = marca
        self._tipo_entrada = tipo_entrada

    @property
    def contador_raton(self):
        return self._contador_ratones

    @contador_raton.setter
    def contador_raton(self, contador):
        self._contador_ratones = contador

    @property
    def id_raton(self):
        return self._id_raton

    @id_raton.setter
    def id_raton(self, id):
        self._id_raton = id

    def __str__(self):
        return (f'''
        Id ratón: {self._id_raton},
        Marca: {self._marca}
        Tipo entrada: {self._tipo_entrada}''')

if __name__ == '__main__':
    raton1 = Raton('Logitech', 'USB')
    print(raton1)
    raton2 = Raton('Noga', 'USB')
    print(raton2)