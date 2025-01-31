

persona = {
    'nombre': '',
    'apellido': '',
    'edad': 0
}

lista_personas = []

cant_input = int(input('Ingresa la cantidad de datos a cargar: '))

for i in range(cant_input):
    keys_persona = persona.keys()
    dict_temp = {}
    for nombres in keys_persona:
        ingreso = input(f'Ingrese {nombres}: ')
        dict_temp[nombres] = ingreso
    lista_personas.append(dict_temp)

print(lista_personas)