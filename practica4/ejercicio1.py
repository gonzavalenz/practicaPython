'''
Escribir funciones que, tomando como entrada una lista de números enteros, decida si la
lista:
● está ordenada crecientemente.
● está ordenada decrecientemente.
● es gaspariforme. Se dice que un lista de n elementos es gaspariforme si todas sus
sumas parciales son no negativas, y la suma total es igual a 0. Las sumas parciales de
una lista a de n elementos está definida por
k
s k =∑ a i para k = 0,...,n-1
i =0
Ejemplo:
Si a = [ 10, 5, 2, 20, 6], n = 5
s0 = 10
s1 = 10 + 5 = 15
s2 = 10 + 5 + 2 = 15 + 2 = 17
s3 = 10 + 5 + 2 + 20 = 17 + 20 = 37
s4 = 10 + 5 + 2 + 20 + 6= 17 + 20 + 6 = 37 + 6 = 43
● es melchoriforme. Se dice que una lista es melchoriforme si alguno de sus elementos es
un centro . Un elemento es un centro si su valor coincide con la suma de los otros
elementos de la lista.
'''

def creciente(lista):
    for i in range(1,len(lista)):
        if lista[i] < lista[i-1]:
            return False
    return True

def decreciente(lista):
    for i in range(1,len(lista)):
        if lista[i] > lista[i-1]:
            return False
    return True

def gaspiforme(lista):
    acumulador = 0
    for x in lista:
        acumulador += x
        if acumulador < 0:
            return False
    if acumulador != 0:
        return False
    else: 
        return True


def suma(lista):
    acumulador = 0
    for x in lista:
        acumulador += x
    return acumulador

def melchoriforme(lista):
    acumulador = suma(lista)
    for x in lista:
        if (acumulador-x) == x:
            return x
    

lista = [1,2,3,4,10]

if creciente(lista):
    print('La lista es creciente.')
elif decreciente(lista):
    print('La lista es decreciente.')

if gaspiforme(lista):
    print('La lista es gaspiforme')
else: 
    print('La lista no es gaspifomre')

if melchoriforme(lista) != None:
    print(f'El centro de la lista melchoriforme es {melchoriforme(lista)}')
