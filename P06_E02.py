# Dada una lista de diccionarios que representan personas con claves "nombre", "edad" y "ciudad"
# genera una nueva lista de nombres de personas que tengan más de 30 años y vivan en "Madrid".

# Importamos librerias necesarias
from functools import reduce
# Definimos la lista de diccionarios
personas = [
    {"nombre": "Ana", "edad": 28, "ciudad": "Madrid"},
    {"nombre": "Luis", "edad": 35, "ciudad": "Barcelona"},
    {"nombre": "Carlos", "edad": 32, "ciudad": "Madrid"},
    {"nombre": "Marta", "edad": 40, "ciudad": "Madrid"},
    {"nombre": "Sofía", "edad": 25, "ciudad": "Valencia"}
]
# Imprimimos la lista de personas
# print("Lista de personas:", personas)

# Utilizamos filter para filtrar las personas que tienen más de 30 años y viven en Madrid
resultado = list(filter(lambda p: p["edad"] > 30 and p["ciudad"] == "Madrid", personas))

# Extraemos los nombres de las personas filtradas
nombres = list(map(lambda n: n["nombre"], resultado))

# Imprimimos los nombres de las personas que cumplen las condiciones
print("Nombres de personas mayores de 30 años y que viven en Madrid:", nombres)