'''
Diseñar una función que genere una lista en forma de telescopio .
Ejemplo: genTelescopio(5) --> [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
'''

def genTelescopio(n):
    lista = []
    for i in range(1,n+1):
        for x in range(i):
            lista.append(i)
        return lista


resultado = genTelescopio(5)
print(resultado)