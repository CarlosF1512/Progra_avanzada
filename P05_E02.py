# Dada una lista de diccionarios que representan productos con nombre (llave en el diccionario)
# y precio (valor de la llave en el diccionario), filtre los productos que cuestan más de $200.00
# y aplique un descuento del 10%. Finalmente calcule el total de los productos que tienen descuento

# Importamos librerias necesarias
from functools import reduce
import random

# Generamos una lista de productos con nombre y precio
productos = {'audífonos': 327, 'mochila': 189, 'teclado':452, 'lámpara':134, 'cafetera':298, 
             'power bank':259, 'mouse': 215, 'reloj': 399, 'herramientas':175, 'parlante': 487} 
# Imprimimos la lista de productos generados
print("Lista de productos:", productos)

# Usamos filter para filtrar los productos que cuestan más de $200.00
productos_filtrados = list(filter(lambda x: x[1] > 200, productos.items()))
# Usamos map para aplicar un descuento del 10% a los productos filtrados
productos_descuento = list(map(lambda x: (x[0], round(x[1]* 0.9, 2)), productos_filtrados))

# Usamos reduce para calcular el total de los productos con descuento
total_descuento = reduce(lambda total, x: total + x[1], productos_descuento, 0)

# Imprimimos el resultado
print("Productos filtrados (precio > $200):", productos_filtrados)  
print("Productos con descuento del 10%:", productos_descuento)
print("Total de productos con descuento:", total_descuento)