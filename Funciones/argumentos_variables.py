print ('*** Argumentos Variables ***')

def superheroe_superpoderes(superheroe, nombre, *args):
    print(f'Superheroe: {superheroe} - {nombre} - {args}')
    # Itera los superpoderes
    for superpoder in args:
        print(f'\tSuperpoder: {superpoder}')


#llamar la funcion
superheroe_superpoderes('Spiderman', 'Peter Parker', 'Instinto aracnido', 'Telaraña')

# Es opcional enviar los *args
superheroe_superpoderes('Mi vecino','Juan Perez')

