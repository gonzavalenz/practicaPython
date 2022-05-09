'''
Diseñar una función que determine si una lista de números enteros, cada número i entre 1
y n aparece i veces consecutivas.
Ejemplo: sonConsecutivos(5,[3,3,3,1,2,2,5,5,5,5,5,4,4,4,4]) --> verdadero
'''

def contador(lista,n):
    con = 0
    for x in lista:
        if n == x:
            con += 1
    if n == con:
        return True
    else: 
        return False

def consecutivos(lista,n):
    for i in range(n):
        if i + 1 not in lista:
            return False
    for x in lista:
        if not(contador(lista,x)):
            return False
    for x in range(len(lista)):    
        if x == 0:
            for n in range(lista[x]):
                if lista[x] != lista[x+n]:
                    return False
        else:
            if lista[x] != lista[x-1]:
                for n in range(lista[x]):
                    if lista[x] != lista[x+n]:
                        return False

    return True

lista = [2,2,3,3,3,1,4,4,4,4]

print(consecutivos(lista,4))
    