print('*** Suma con argumentos varibles ***')

# Funcion sumar que acepta args variables

def sumar(*args):
    total = 0
    for numero in args:
        total += numero
    return total

# Llamado a la funcion symar
resultado = sumar(1,2,3,4,5)
print(f'Resultado: {resultado}')