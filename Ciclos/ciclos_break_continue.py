# print('*** break y continue ***')
#
# #Ejemplo con break
#
# for numero in range(1, 9):
#     if numero % 2 == 0: #numero par
#         print(numero)
#         break # termina el ciclo
#
#
# # Ejemplo con continue
# print('\nPalabra continue: ')
# for numero in range(1, 10):
#     if numero % 2 == 1: #numero impar
#         continue
#     print(numero)
#     str('Hola').lower()
#
# # Declarar la variable
cadena = 'Hola Mundo'
cantidad = 0
# # Agregar el ciclo for

for i in cadena.lower():
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        cantidad += 1

print(cantidad)