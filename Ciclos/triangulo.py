
print('*** Dibujar triangulo simetrico ***')

nro_filas = int(input('Proporcione el numero de filas: '))

for fila in range(1, nro_filas + 1):
    espacios_blanco = ' ' * (nro_filas - fila)
    asteriscos = '*' * (2 * fila - 1)
    print(espacios_blanco + asteriscos)
