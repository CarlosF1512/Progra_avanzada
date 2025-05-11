""" 
Desarrolle un programa en Python que gener un arreglo NumPy tridimensional de tamaño 5x4x3 con valores aleatorios entre 0 y 100
Posteriormente el programa debe encontrar el elementos más pequeño y el más grande e indicar de dichos elementos dentro del arreglo
Imprima la matriz, los valores menor y mayor, así como sus ubicaciones.

"""

# Importamos líbrerias
import numpy as np

# Creamos la matriz aleatoria de 5x4x3
arreglo = np.array(np.random.randint(0, 100, size=(5, 4, 3)))
print(arreglo.ndim)
print(arreglo)

# Encontrar el elemento más pequeño y el más grande
min_v = arreglo.min()
max_v = arreglo.max()
print(f'EL elemento más pequeño en los arreglos es {min_v}, mientras que el elemenos más grande es {max_v}')

# Encontrar las ubicaciones de los valores
for i in range(0,5):
    for j in range(0,4):
        for k in range(0,3):
            posicion = arreglo[i][j][k]
            if posicion == min_v:
                #min = posicion
                ub_min = (i,j,k)
            if posicion == max_v:
                #max = posicion
                ub_max = (i,j,k)

print(f'La ubicación del valor más pequño es {ub_min} y la ubicación del valor más grande es {ub_max}')