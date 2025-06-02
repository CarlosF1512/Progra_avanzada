# Dada una lista de diccionatios que representan productos con nombre (llave en el ciccionario)
# y precio (valor de la llave en el diccionario), filtre los productos que cuestan más de $200.00
# y aplique un descuento del 10%. Finalmente calcule el total de los productos que tienen descuento

# Importamos librerias necesarias
from functools import reduce
import random

# Generamos una lista de productos con nombre y precio
productos = [
    {'nombre': f'Producto {i}', 'precio': random.randint(100, 500)}
    for i in range(1, 21)
]
# Imprimimos la lista de productos generados
print("Lista de productos:", productos)

# Usamos filter para filtrar los productos que cuestan más de $200.00
productos_filtrados = list(filter(lambda x: x['precio'] > 200, productos))
# Usamos map para aplicar un descuento del 10% a los productos filtrados
productos_descuento = list(map(lambda x: {'nombre': x['nombre'], 'precio': x['precio'] * 0.9}, productos_filtrados))

# Usamos reduce para calcular el total de los productos con descuento
total_descuento = reduce(lambda total, x: total + x['precio'], productos_descuento, 0)

# Imprimimos el resultado
print("Productos filtrados (precio > $200):", productos_filtrados)  