""" Diseña un programa que, dado un número entero, determine si éste es el doble de un
número impar. (Ejemplo: 14 es el doble de 7, que es impar.) """

# Ingresar el número entero.
n = int(input('Ingresar un número entero: '))

# Dividir el número por 2, sacar el resto del resultado y determinar si es par o impar.
resultado = n / 2 
resto = resultado % 2
if resto == 1: print(f'{n} es el doble de {int(resultado)}, que es impar.')
else: print(f'{n} no es el doble de un número entero impar.')