print('*** manejo de listas ***')

mi_lista = [1, 2, 3, 4, 5]
print(f'{mi_lista}')

# largo de una listas
print(f'Largo de la lista: {len(mi_lista)}')

# Acceder a los elementos de la lista por indice
print(f'Accedemos al valor del indice 4: {mi_lista[4]}')
print(f'Accedemos al valor del ultimo indice: {mi_lista[-1]}')

# Modificar los elementos de una lista
mi_lista[1] = 10
print(f'Modifica el valor del indice 1: {mi_lista}')

#Agregar un nuevo elemento al final
mi_lista.append(6)
print(f'{mi_lista}')

# Añadir un nuevo elemento en un indice especifico
mi_lista.insert(2,15)
print(f'{mi_lista} -> se añadió el valor de 15 en el indice 2')

##  Eliminar elementos de una lista
# usando el metodo remove
mi_lista.remove(5)
print(f'{mi_lista} -> se eliminó el valor 5')

# Removemos por indice con el metodo pop
mi_lista.pop(1)
print(f'{mi_lista} -> se eliminó el valor del indice 1')

# Elimina usando la palabra del
del mi_lista[2]
print(f'{mi_lista} -> se eliminó el elmento del indice 2')

# Obtener sublista de una lista
subLista = mi_lista[1:3] #genera una sublista del indice 1 al 2 (3 no se incluye)
print(f'{subLista} <- sublista[1:3]')
