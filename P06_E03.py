# Dada una lista de listas de números, utiliza una expresión generadora para calcular la media de todos los números en la lista.
# Importamos librerias necesarias
from functools import reduce 
# Definimos la lista de listas de números
lista_numeros = [[1, 2, 3], [4, 5], [6, 7, 8]]
# Imprimimos la lista de listas de números
print("Lista de listas de números:", lista_numeros)
# Utilizamos una expresión generadora para calcular la suma de todos los números en la lista
suma_total = sum(num for sublista in lista_numeros for num in sublista)
# Calculamos el número total de elementos en la lista
total_elementos = sum(len(sublista) for sublista in lista_numeros)
# Calculamos la media
media = suma_total / total_elementos #if total_elementos > 0 else 0
# Imprimimos la media
print("Media de todos los números en la lista:", media)

