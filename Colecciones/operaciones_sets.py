print('*** Operaciones con Set ***')
a = {1,2,3,4}
b = {3,4,5,6}

union = a | b
print(f'Union de a | b: {union}')

interseccion = a & b
print(f'Interseccion a & b: {interseccion}')

diferencia = a - b
print(f'Diferencia de a - b: {diferencia}')