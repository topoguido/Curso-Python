print('*** Agenda de contactos ***')

agenda = {
    "Carlos": {
        'telefono': '12345',
        'correo': 'c@mail.com',
        'direccion': 'calle 13'
    },

    "Maria": {
        'telefono': '55555',
        'correo': 'm@mail.com',
        'direccion': 'avenida 33'
    },

    "Raul": {
        'telefono': '888888',
        'correo': 'ffff@mail.com',
        'direccion': 'calle sin nombre'
    }
}

print(agenda)

# Acceder a la informacion de un contacto específico
nombre_a_buscar = input('Nombre a buscar: ').capitalize()
print(f'Datos encontrados: {agenda.get(nombre_a_buscar).get('correo')}')

# Agrega contacto nuevo
agenda['Ana'] = {
    'telefono': '44444',
    'correo': 'a@mail.com',
    'direccion': 'calle'
}
print(agenda.get('Ana'))

# Eliminar un contacto existente
agenda.pop('Carlos')
print(agenda)

# Mostrar todos los contactos
print('\nContactos en la agenda')
for nombre, detalles in agenda.items():
    print(f'''Nombre: {nombre}
    Telefono: {detalles.get('telefono')}
    correo: {detalles.get('correo')}
    Direccion: {detalles.get('direccion')}''')