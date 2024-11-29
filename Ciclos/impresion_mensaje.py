print('*** Repeticion de un mensaje ***')

mensaje = input('Proporcione un mensaje a repetir: ')
nro_repeticiones = int(input('Cantidad de repeticiones: '))

for _ in range(nro_repeticiones): #el guion bajo indica que no necesitamos usar una variable en el indice de for
    print(mensaje)

