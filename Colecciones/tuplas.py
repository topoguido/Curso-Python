print('*** Manejo de tuplas ***')

mi_tupla = (1,2,3,4,5)
print(mi_tupla)
# No podemos modificar una tupla
# mi_tupla[0] = 10

# Podemos iterar los elementos de una tupla

for elemento in mi_tupla:
    print(elemento, end=' ')

# Crear una tupla para una coordenada x, y

coordenadas = (3,5)
print(f'\nCoordenada en el eje x: {coordenadas[0]}')
print(f'Coordenada en el eje y: {coordenadas[1]}')

# crear una tupla unitaria
tupla_un_elemento = 10,
print(f'Tupla de un element: {tupla_un_elemento}')

# Tupla anidada
tupla_anidada = (1, (2,3), (4,5))
print(tupla_anidada)
print(f'Segundo elemento de la tupla anidada: {tupla_anidada[1]}')