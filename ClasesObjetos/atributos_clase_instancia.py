class Persona:
    atributo_clase = 0

    def __init__(self, atributo_instancia):
        self.atributo_instancia = atributo_instancia

# Programa
if __name__ == '__main__':
    print('*** Atributo de clase ***')
    print(f'Atributo de clase: {Persona.atributo_clase}')

    # Modifica atributo de clase
    Persona.atributo_clase = 10
    print(f'Atributo de clase: {Persona.atributo_clase}')

    # Crea objeto de persona1
    persona1 = Persona(15)
    print(f'Atributo de clase de persona1 {persona1.atributo_clase}')
    print(f'Atributo de instancia desde persona1 {persona1.atributo_instancia}')

    # Crea objeto persona2
    persona2 = Persona(30)
    print(f'Atributo de clase de persona2 {persona2.atributo_clase}')
    print(f'Atributo de instancia desde persona2 {persona2.atributo_instancia}')
