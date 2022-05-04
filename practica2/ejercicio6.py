'''
Diseñar un programa que genere una lista de números usando el siguiente proceso:
comenzar con un entero n que deberá ingresar el usuario. Si n es par, dividirlo por 2. Si n
es impar, multiplicarlo por 3 y sumarle 1. Repetir este proceso hasta que el nuevo valor
obtenido para n sea 1.
Ejemplo, para n = 22, la secuencia que se obtiene es:
22 11 33 17 52 26 13 40 20 10 5 16 8 4 2 1
'''

lista = []

n = int(input('Ingrese un numero entero: '))
lista.append(n)

while n != 1:
    # Si el num es par dividirlo, si es impar multiplicarlo y sumarle 1
    if n % 2 == 0:
        n = n // 2
    else: 
        n = (n * 3) + 1

    # Agregamos el nuevo num a la lista
    lista.append(n)

print(lista)
