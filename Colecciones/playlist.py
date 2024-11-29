print('*** Playlist de caciones ***')

# Creamos la lista vacia
lista_reproduccion = []

numero_canciones = int(input('Cuantas canciones deses agregar?: '))

# Iteramos cada elemento de la lista para agregar un nuevo elemento
for indice in range(numero_canciones):
    cancion = input(f'Proporcione la cancion {indice +1}: ')
    lista_reproduccion.append(cancion)

# Ordenar la lista en orden alfabetico
#lista_reproduccion.sort(reverse=True) # Ordena a la inversa
lista_reproduccion.sort()

# Mostrar la lista iterando sus elementos
print('\nIteramos el playlist')
for cancion in lista_reproduccion:
    print(f'- {cancion}')