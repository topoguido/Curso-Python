from empleado import Empleado
from empresa import Empresa

empresa = Empresa()

empresa.nombre = str(input('Nombre de la empresa: '))
cant_empleados = int(input('Cantidad empleados: '))

for i in range(cant_empleados):
    nuevo_empleado = Empleado()
    nuevo_empleado.nombre = str(input('Nombre del empleado: '))
    nuevo_empleado.departamento = str(input('Departamento: '))
    empresa.contratar_empleado(nuevo_empleado)

print(f'La empresa {empresa.nombre} tiene {empresa.obtener_nro_empleados_depto('A')} empleados en el depto A')
print(f'La empresa {empresa.nombre} tiene {empresa.obtener_nro_empleados_depto('B')} empleados en el depto B')
print(f'La empresa {empresa.nombre} tiene {empresa.obtener_nro_empleados_depto('C')} empleados en el depto C')
print(empresa)

