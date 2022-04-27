'''
Escribir un programa que muestre, de a diez números por línea y separados por un
blanco, todos los números entre 100 y 1000 que sean divisibles por 5 y 6.
'''

contador = 0 
lista = []

# Recorrer el rango de 100 a 1000 y agregar los números divisibles a la lista
for x in range(100,1001):
    if x % 5 == 0 and x % 6 == 0:
        lista.append(x)

# Recorrer la lista, imprimir los números. 
for x in lista:
    print(x,end=' ')
    contador += 1
    # Cuando el contador llegue a 10 insertar un salto de linea
    if contador == 10:
        print('\n')
        contador = 0 


