class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    #sobreescribir el metodo __Str__
    def __str__(self):
        return f'''Persona:
        nombre = {self.nombre}
        apellido = {self.apellido}
        Dir. memoria -> {super.__str__(self)}'''


# Codigo principal
persona1 = Persona('Ana', 'Martinez')
print(persona1)
