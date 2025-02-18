print('*** Imprimir detalles de una persona con kwargs')

# Funcion que acepta args variables en forma de llave-valor

def imprimir_detalle_persona(**kwargs):
    print('\nValores recibidos: ')
    for llave, valor in kwargs.items():
        print(f'{llave}:{valor}')

# Llamado a la funcion

imprimir_detalle_persona(nombre='Karla', edad=30, ciudad='Mexico')
imprimir_detalle_persona(nombre='Carlos', edad=28, ciudad='Guada', puesto='Gerente')