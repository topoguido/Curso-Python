from empleado import Empleado

class Empresa:

    def __init__(self):
        self.__nombre = ''
        self.__empleados = [Empleado]

    def contratar_empleado(self, empleado):
        self.__empleados.append(empleado)

    def obtener_nro_empleados_depto(self, depto)-> int:
        contador = 0
        for empleado in self.__empleados:
            if empleado.departamento == depto:
                contador +=1
        return contador