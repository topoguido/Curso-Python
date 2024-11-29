print('*** Lista de suscriptores ***')

#Define el set inicial
# suscriptores = {} # aqui se define un diccionario vacio

suscriptores = set() # Define un set vacio
numero_suscriptores = int(input('Numero de suscriptores iniciales: '))
for _ in range(numero_suscriptores-1):
    suscriptores.add(input('Nuevo suscriptor (email): '))

print(f'Lista de suscriptores inicial: {suscriptores}')

# Verificar si un nuevo suscriptor ya está en la lista

nuevo_suscriptor = input('Proporciona el nuevo suscriptor: ')
if nuevo_suscriptor in suscriptores:
    print(f'El nuevo suscriptor ya está en la lista {nuevo_suscriptor}')
else:
    suscriptores.add(nuevo_suscriptor)
    print(f'El nuevo suscriptor se ha agregado a la lista {nuevo_suscriptor}')

print(f'Lista de suscriptores actualizada: {suscriptores}')

# Eliminar un suscriptor
suscriptores_eliminar = input('Proporciona suscriptor a eliminar: ')
suscriptores.remove(suscriptores_eliminar)
print(f'El suscritor {suscriptores_eliminar} se ha eliminado')
print(f'Lista de suscriptores final: {suscriptores}')

# Verifica cantidad total de suscriptores
print(f'Cantidad total de suscriptores : {len(suscriptores)}')

# Muestra todos los suscriptores iterando
print(f'--- Lista de suscriptores ---')
for suscriptor in suscriptores:
    print(f'- {suscriptor}')