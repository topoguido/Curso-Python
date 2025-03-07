class Animal:
    def comer(self):
        print('Come muchas veces al dia')

    def dormir(self):
        print('Duerme muchas horas')

class Perro(Animal):
    def hacer_sonido(self):
        print('Puede ladrar')

    #sobreescritura del metodo dormir
    def dormir(self):
        print('Duerme 8 horas')

print('*** ejemplo de herencia ***')

print('Clase padre, animal')
animal1 = Animal()
animal1.comer()
animal1.dormir()

print('\nClase hija, es perro')
perro1 = Perro()
perro1.comer()
perro1.dormir()

perro1.hacer_sonido()
