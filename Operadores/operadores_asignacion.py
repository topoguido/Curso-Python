print('*** Operadores de asignación ***')
numero = 5
print(f'Valor de numero: {numero}')
cadena = 'Saludos desde Python'
print(f'Valor de la cadena: {cadena}')

# Asignacion multiple
x, y, z = 5, 'Hola', -9.15
print(f'Valor de x = {x}, y = {y}, z = {z}')

# Asignacion encadenada

a = b = c = 9
print(f'a = {a}, b = {b}, c = {c}')

# Intercambio de valores de una variable, sin utilizar variables temporales
x, y = 5, 10
print(f'x = {x}, y = {y}')
# Aplicando el concepto de asignacion multiple, intercambiamos valores
x, y = y, x
print(f'x = {x}, y = {y}')

# Recibir multiples valores de la entrada del usuario
nombre, apellido = input('Ingresa tu nombre y apellidos separados por coma: ').split(',')
print(f'Nombre: {nombre}, apellido: {apellido.strip()}')