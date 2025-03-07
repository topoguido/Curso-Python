from DispositivoEntrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    _contador_teclados = 0
    _id_teclado = 0

    def __init__(self, marca, tipo_entrada):
        Teclado._contador_teclados += 1
        self._id_teclado = Teclado._contador_teclados
        super().__init__(marca, tipo_entrada)

    @property
    def contador_teclados(self):
        return self._contador_teclados

    @contador_teclados.setter
    def contador_teclados(self, contador):
        self._contador_teclados = contador

    @property
    def id_teclado(self):
        return self._id_teclado

    @id_teclado.setter
    def id_teclado(self, id):
        self._id_teclado = id

    def __str__(self):
        return f'''
        Id teclado: {self._id_teclado}
        Tipo Entrada: {self._tipo_entrada}'''

if __name__ == '__main__':
    teclado1 = Teclado('Logitech', 'USB')
    print(teclado1)
    teclado2 = Teclado('Noga', 'USB')
    print(teclado2)