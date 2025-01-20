print('*** Diccionarios con Python ***')

# Crear un diccionario de persona con clave y valor
persona = {
    'nombre': 'Juan',
    'edad': 30,
    'ciudad': 'Capital'
}

print(f'Diccionario de persona: {persona}')

# Accede a los elementos del diccionario
print(f'Nombre: {persona['nombre']}')

# Modifica un valor del diccionario
persona['edad'] = 34
print(persona.get('edad'))

# Agrega un elemento
persona['profesion'] = 'Ingeniero'
print(persona)

# Elimina un elemento
del persona['ciudad']
print(persona)

persona.pop('profesion')  # otro metodo para eliminar
print(persona)

# itera los elementos de un diccionario
for llave, valor in persona.items():
    print(f'Llave: {llave}, Valor: {valor}')

# Obtiene solo los valores
print(f'\nValores del diccionario: ')
for valor in persona.values():
   print(f'- Valor: {valor} ')

# Obtiene solo las llaves
print(f'\nLlaves del diccionario: ')
for llave in persona.keys():
    print(f'Llave: {llave}')