import json

import biblioteca
from biblioteca import Biblioteca
from libro import Libro

def ingreso_continua():
    while(True):
        print('Desea cargar otro libro? S/N: ')
        ing = str(input()).strip().upper()
        if ing == 'S' or ing == 'N':
            return ing
        else:
            print('Ingreso erroneo...')

with open("biblioteca.json", "r", encoding="utf-8") as archivo:
    biblio_file = json.load(archivo)

print('*** Sistema de bibliotecas ***')

# menu
print('Elija opción')
print('1: Agregar libro')
print('2: Buscar libros por autor')
print('3: Buscar libros por género')
opcion = int(input())

if opcion == 1:
    continua = 'S'
    while(continua == 'S'):
        print('Elija la biblioteca: ')

        for biblioteca in biblio_file:
            print(f'ID: {biblioteca['id']} - Nombre: {biblioteca['nombre']}')

        id = int(input())
        titulo = str(input('Titulo: '))
        autor = str(input('Autor: '))
        genero = str(input('Género: '))
        nuevo_libro = Libro(titulo, autor, genero)
        biblio = Biblioteca()
        biblio.id = id
        biblio.agregar_libro(nuevo_libro)

        continua = ingreso_continua()

elif opcion == 2:
    autor = str(input('Autor: '))
    with open("biblioteca_libro.json", "r", encoding="utf-8") as archivo:
        bibliotecas_detalle = json.load(archivo)

    biblios = [Biblioteca]
    biblio = Biblioteca()
    for biblioteca in bibliotecas_detalle:
        biblio.id_libro = biblioteca['id']
        libros = [Libro(libro['titulo'], libro['autor'], libro['genero'])
                  for libro in biblioteca['libros'] if libro["autor"].lower() == autor.lower()]
        if libros:
            biblio.agregar_libro(libros)
        biblios.append(biblio)

    print('Estos son los libros del autor:')

    for biblio in biblios:
        print(f'Biblioteca: {biblio.id}')
        print('Libros:')
        libros = [biblio.libros]
        for libro in libros:
            print(f'Titulo: {libro} - Género: {libro}')


