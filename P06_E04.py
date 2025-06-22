# Utiliza una expresión generadora para calcular la varianza de una lista de números. La varianza se calcula como 
# la media de los cuadrados de las diferencias con la media. 

# Importamos librerias necesarias
from functools import reduce
# Definimos la lista de números
numeros = [10, 12, 23, 23, 16, 23, 21, 16]
# Imprimimos la lista de números
print("Lista de números:", numeros)
# Calculamos la media utilizando una expresión generadora
media = sum(numeros) / len(numeros) #if numeros else 0
# Calculamos la varianza utilizando una expresión generadora
varianza = sum((x - media) ** 2 for x in numeros) / len(numeros) #if numeros else 0
# Imprimimos la media y la varianza
print("Media:", media)      
print("Varianza:", varianza)