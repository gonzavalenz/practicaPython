""" Escribir un programa que permita ingresar tres números enteros y escribirlos en orden creciente. """

# Ingresar los 3 números, crear la lista y ordenar la misma.
lista = list()
for x in range(3):
    n = int(input('Ingrese un número: '))
    lista.append(n)

lista.sort()
print(lista)

