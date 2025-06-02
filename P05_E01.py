# Dada una lista de números enteros cuañquiera, utilice los métodos map, filter y reduce 
# para filtar los número s impares de la lista y calcular la suma de sus cuadrados

# Importamos librerias necesarias
from functools import reduce
import random

# Generamos una lista de números aleatorios
numeros = [random.randint(1, 100) for x in range(20)]
# Imprimimos la lista de números generados
print("Lista de números:", numeros)

# Usamos filter para filtrar los números impares
impares = list(filter(lambda x: x % 2 != 0, numeros))
# Usamos map para calcular el cuadrado de los números impares
cuadrados_impares = list(map(lambda x: x ** 2, impares))
# Usamos reduce para calcular la suma de los cuadrados de los números impares
suma_cuadrados_impares = reduce(lambda x, y: x + y, cuadrados_impares)

# Imprimimos el resultado
print("Números impares:", impares)
print("Cuadrados de los números impares:", cuadrados_impares)
print("Suma de los cuadrados de los números impares:", suma_cuadrados_impares)

