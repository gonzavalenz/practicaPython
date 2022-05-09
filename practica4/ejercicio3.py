'''
Diseñar una función que determine si una lista de números enteros está ordenada de
menor a mayor y cada número i entre 1 y n aparece exactamente i veces.
Ejemplo:
para n = 5
esTelescopio(5,[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]) --> verdadero
'''

def telescopio(lista,numero):
    if numero != lista[-1]:
        return False
    for n, i in zip(lista,range(len(lista))):
        if i != 0:
            if n < lista[i-1]:
                return False
            if n != lista[i-1]:
                for x in range(n):
                    if n != lista[i+x]:
                        return False
                if i+n < len(lista): 
                    if n == lista[i+n]:
                        return False
    return True



lista = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]

resultado = telescopio(lista,5)
print(resultado)