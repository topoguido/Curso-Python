from random import randint
from collections.abc import Sequence

print('*** Sistema Generador de ID Unico ***')

nombre = input('Cual es tu nombre?: ').strip().upper()
apellido = input('Cual es tu apellido?: ').strip().upper()
anio = str(input('Cual es tu año de nacimiento?: ')).strip()
print('--------------------------------------')
print('\n')
num_rand = randint(1000,9999)
print(f'Hola {nombre},\n' + f'Tu ID es: {nombre[0:2] + apellido[0:2] + str(num_rand) + anio[2:4]}')

