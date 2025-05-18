# Práctica 2 - Ejercicio 1 
import numpy as np
import math

class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"

    def magnitud(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def angle(self):
        return math.atan2(self.y, self.x)
    
    def grados(self):
        return math.degrees(self.angle())
    
    def __add__(self, other):
        return vector(self.x + other.x, self.y + other.y)
    
p = vector(5,-1)
q = vector(2,-4)

print("Vector p: ", p)
print("Vector q: ", q)  

print("Magnitud de p: ","{:.4f}".format(p.magnitud()))
print("Magnitud de q: ","{:.4f}".format(q.magnitud()))
print(f'Angulo de p: ',"{:.4f}".format(p.angle()),'rad',':',"{:.2f}".format(p.grados()),'°')
print(f'Angulo de q: ',"{:.4f}".format(q.angle()),'rad',':',"{:.2f}".format(q.grados()),'°')

print("Suma de p y q: ", p + q)