# Definicion de una clase

class Persona:

    def __init__(self,nombre, apellido):
        # Creamos los atributos de la case
        self.__nombre = nombre
        self.__apellido = apellido

    @property
    def nombre(self):
        return self.__nombre

    @property
    def apellido(self):
        return self.__apellido

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido


# Creacion de objetos
if __name__ == '__main__':
    #Creacion del primer objeto
    persona1 = Persona('fulano', 'mengano')
    print(f'Nombre: {persona1.nombre} - Apellido: {persona1.apellido}')

    persona1.nombre = 'Antonio'
    persona1.apellido = 'Perez'
    print(f'Nombre: {persona1.nombre} - Apellido: {persona1.apellido}')

    # se agrega un atributo de manera dinamica, pero solo para este objeto
    setattr(persona1, 'edad',20)
    print(f'nuevo atributo Edad: {persona1.edad}')
    print(persona1.__dict__)
    print(persona1.__module__)