# Existe un método llamado mínimo cuadrados que en su cado lineal permite obtener una línea recta
# que se aporxima a una serie de m puntos (x,y). La recta resultante del método es y = a0 + a1x, y 
# para calcular los coeficientes a0 y a1 se utiliza la siguiente fórmula:

# a1 = (Σ(xi)^2 * Σ(yi) - Σ(xiyi) * Σ(xi)) / (m * Σ(xi^2) - (Σxi)^2)
# a0 = (m*Σ(xiyi) - Σ(xi)*Σ(yi) / (m * Σ(xi^2) - (Σxi)^2)

# Desarrolle un programa en Python que realice el cácluclo de las fórmulas, utilice las funciones
# lambda, map, filter y/o reduce para el calculo de las sumatorias según sea necesario.
# Considere que los puntos para el cálculo se reciben como una lista de tuplas (cada tupla es 
# un punto (x,y)) y m es el número de las tuplas en la lilsta

# Importamos librerias necesarias
from functools import reduce

# Definimos la lista de puntos como tuplas (x, y)
puntos = [(1, 1.3), (2, 3.5), (3, 4.2), (4, 5), (5, 7), (6,8.8), (7,10.1), (8,12.5),(9,13),(10,15.6)]
# Imprimimos la lista de puntos
print("Lista de puntos:", puntos)

# Definimos m como el número de puntos
m = len(puntos)

# Calculamos las sumatorias necesarias utilizando reduce y map
sum_x = reduce(lambda x, p: x + p[0], puntos, 0)
sum_y = reduce(lambda y, p: y + p[1], puntos, 0)
sum_xy = reduce(lambda xy, p: xy + p[0] * p[1], puntos, 0)
sum_x2 = reduce(lambda x2, p: x2 + p[0] ** 2, puntos, 0)
# Imprimimos las sumatorias
print()
print("Σ(xi^2):", sum_x2)
print("Σyi:", sum_y)    
print("Σ(xi * yi):", sum_xy)
print("Σxi:", sum_x)
print()
# Calculamos los coeficientes a1 y a0 utilizando las fórmulas dadas
a0 = (sum_x2 * sum_y - sum_xy * sum_x) / (m * sum_x2 - sum_x ** 2)
a1 = (m * sum_xy - sum_x * sum_y) / (m * sum_x2 - sum_x ** 2)

# Imprimimos los coeficientes
print("Coeficiente a1:", a1)
print("Coeficiente a0:", a0)
# La ecuación de la recta resultante es y = a0 + a1 * x
print()
print(f"La ecuación de la recta resultante es: y = {a0} + {a1} * x")





