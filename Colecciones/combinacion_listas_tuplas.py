print('*** Combinacion de listas y tuplas ***')


#definir una lista que almacen tuplas de productos

productos = [
    ('P001','Camiseta', 20.0),
    ('P002', 'Jeans', 30.0),
    ('P003', 'Sudadera', 40.0),
]

# Imprimir la informacion de cada producto
# y ademas calculo el precio total
precio_total = 0

print('Informacion de los productos: ')
for producto in productos:
    id, descripcion, precio = producto  # unpacking
    print(f'Id: {id}, Descripcion: {descripcion}, Precio: {precio}')
    precio_total += precio
print(f'Precio total de los productos: ${precio_total}')
