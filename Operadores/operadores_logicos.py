# Operador AND

condicion1 = False
condicion2 = True
resultado = condicion1 and condicion2
print(f'Resultado {condicion1} and {condicion2}: {resultado}')

# Operador NOT

condicion1 = True
resultado = not condicion1
print(resultado)

# Revisar si una variable es cadena vacia
nombre = ''
es_cadena_vacia = not nombre
print(f'Es cadena vacia: {es_cadena_vacia}')

# Revisar si una variable no tiene ningun valor asignado
variable = None
es_variable_sin_valor = not variable
print(f'Es variable vacia: {es_variable_sin_valor}')