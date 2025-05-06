#''' 
# Sucesión de Fibonacci versión lista: 
# La función recibe como argumento la cantidad de cifras de la serie
# El calculo del número áureo está dado por \varphi = lim_{n\rightarrow \infty} = \dfrac{fib(n+1)}{n}
# ''' 
# Comentario en bloque

def Fib(n=10): #Parametro por defecto
    lista = [0,1]
    for _ in range(n): # "_" es una variable desechable, no se usa pero se necesita para el rango
        lista.append(lista[-1]+lista[-2]) # (lista[i]+lista[i+1]) # Agrega un elemento al final de la lista 
    return lista

# print(Fib(25)) # Imprime la lista de Fibonacci

n = 500
sucesion = Fib(n) 
# print(sucesion) 
print("El número áureo es: ", sucesion[-1]/sucesion[-2]) # Imprime el número áureo

