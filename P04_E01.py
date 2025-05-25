# Ejercicio 1 - Implemente una clase Rectangulo que represente un rectángulo y que tenga dos atributos base y altura.

class Rectangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

# Use __eq__ para comparar si dos rectángulos son iguales
    def __eq__(self, other):
        if self.base == other.base and self.altura == other.altura:
            print('Réctangulos iguales: ')
            return True
        else:
            print('Réctangulos iguales: ')
            return False

# Use __ne__ para verificar si son diferentes
    def __ne__(self,other):
        if self.base != other.base or self.altura != other.altura:
            print('Réctangulos diferentes: ')
            return True
        else:
            print('Réctangulos diferentes: ')
            return False 

# Función para determinar el área de los rectangulos
    def area(self):
        return self.base*self.altura

# Utilice los métodos __gt__ y __lt__ para comparar el áre de dos rectángulos
    def __gt__(self,other):
        if self.area() > other.area():
            print('Réctangulo A > B: ')
            return True
        else:
            print('Réctangulo A > B: ')
            return False
        
    def __lt__(self,other):
        if self.area() < other.area():
            print('Réctangulo A < B: ')
            return True
        else:
            print('Réctangulo A < B: ')
            return False

r1 = Rectangulo(5,10) 
r2 = Rectangulo(5,10) 
r3 = Rectangulo(6,12)

print(r1 == r2)
print(r2 == r3)

print(r1 != r2)
print(r2 != r3)

print(r1 > r3)
print(r1 < r3)