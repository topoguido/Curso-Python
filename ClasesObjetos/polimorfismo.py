# Polimorfismo
from herencia import animal1

class Animal:
    def hacer_sonido(self):
        print('Hace pitido')

class Perro(Animal):
     def hacer_sonido(self):
         print('Puede ladrar')

class Gato(Animal):
    def hacer_sonido(self):
        print('Puede maullar')

def hacer_sonido_animal(animal):
    animal.hacer_sonido()

print('*** Ejemplo polimorfismo ***')
print('Clase Padre Animal: ')
animal1 = Animal()
hacer_sonido_animal(animal1)

print('\nClase hija Perro: ')
animal2 = Perro()
hacer_sonido_animal(animal2)

print('\nClase hija Gato: ')
animal3 = Gato()
hacer_sonido_animal(animal3)