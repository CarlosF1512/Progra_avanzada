# Dadas dos listas de números, por ejemplo [1,2,3] y [4,5,6], genera una nueva lista
# que contenga el producto de los elementos correspondientes. 

# Importamos librerias 
from functools import reduce
# Definimos las listas de números
lista1 = [7, 9, 2]
lista2 = [5, 6, 7]
# Imprimimos las listas originales
print("Lista 1:", lista1)
print("Lista 2:", lista2)
# Utilizamos map para multiplicar los elementos correspondientes de las dos listas
resultado = list(map(lambda x, y: x * y, lista1, lista2))
# Imprimimos el resultado
print("Resultado:", resultado)
