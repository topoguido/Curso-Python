# *args: arguments, tupla.
# **kwargs: keyword args (key, value) como un diccionario

print('*** Argumentos variables en forma de diccionario ***')

def superheroe_superpoderes(nombre, *args, **kwargs):
    print(f'Superheroe: {nombre} - {args} - Mas info: {kwargs}')

# LLamado a funcion
superheroe_superpoderes('Spiderman', 'Instinto aracnido', edad=18, empresa='Marvel')