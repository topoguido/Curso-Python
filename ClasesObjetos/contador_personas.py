class Persona:
    #Atributo de clase
    contador_personas = 0

    def __init__(self, nombre, apellido):
        # incrementa el valor del atributo de clase
        Persona.contador_personas += 1
        self.id = Persona.contador_personas
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'Persona: {self.id}, {self.nombre}, {self.apellido}')

    @staticmethod
    def get_contador_personas_estatico():
        return Persona.contador_personas

    @classmethod
    def get_contador_personas_clase(cls):
        return cls.contador_personas


if __name__ == '__main__':
    persona1 = Persona('Arnaldo', 'Gomez')
    persona1.mostrar_persona()

    # segundo objeto
    persona2 = Persona('Daniel', 'Sanchez')
    persona2.mostrar_persona()

    # Imprimir valor de contador de objetos
    print(f'Contador objetos Persona: {Persona.contador_personas}')
    print(f'Contador objetos Persona1 (static): {Persona.get_contador_personas_estatico()}')
    print(f'Contador objetos Persona (clase): {Persona.contador_personas}')