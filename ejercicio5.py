""" Escribir un programa que permita ingresar dos números enteros y escribirlos en orden creciente. """

# Ingresar 2 números.
num1 = int(input('Ingresar un número: '))
num2 = int(input('Ingresar otro número: '))

# Ordenar los numeros.
if num1 < num2:
    print(num1,num2)
elif num1 > num2:
    print(num2,num1)
else: 
    print('Son iguales.')

