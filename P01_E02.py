""" 
Dada la matriz H, calcula la transpuesta de cada plano dentro de la matriz tridimensional H. 
"""
# Importamos librerias
import numpy as np

# Creamos la matriz H
H = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

# Slide de los planos
plano0 = H[0]
plano1 = H[1]

# Transpuesta de cada slide
T1 = plano0.T
T2 = plano1.T

# Unimos las transpuestas en una matriz
H_T = np.array([T1,T2])

print("La metriz original es: ")
print(H)
print("Los planos transpuestos son: ")
print(H_T)