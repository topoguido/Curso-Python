from traceback import print_tb

from Computadora import Computadora
from Monitor import Monitor
from Orden import Orden
from Raton import Raton
from Teclado import Teclado

print('*** Mundo PC ***')

# Computadora 1
teclado1 = Teclado('Logitech', 'USB')
raton1 = Raton('Logitech', 'Wireless')
monitor1 = Monitor('Samsung', 22)
computadora1 = Computadora('DELL', monitor1, teclado1, raton1)

teclado2 = Teclado('Logitech', 'USB')
raton2 = Raton('Logitech', 'Wireless')
monitor2 = Monitor('Samsung', 22)
computadora2 = Computadora('HP', monitor2, teclado2, raton2)

# Crea la lista de computadoras

computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)
print(orden1)