""" Diseña un programa que, dado un número entero, muestre por pantalla el mensaje "El
número es par." cuando el número sea par y el mensaje "El número es impar." cuando sea
impar. (Una pista: un número es par si el resto de dividirlo por 2 es 0, e impar en caso
contrario.) """

# Ingresar un Número entero.
n = int(input('Ingrese un número entero: '))

# Dividir por 2, si el resto es 0 el número es par.
r = n % 2
if r == 0: print('El número es par.')
else: print('El número no es par.')
