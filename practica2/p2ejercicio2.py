'''
Diseña un programa que solicite la lectura de un número entre 0 y 10 (ambos inclusive).
Si el usuario teclea un número fuera del rango válido, el programa solicitará nuevamente
la introducción del valor cuantas veces sea menester.
'''


while True:
    # Ingresar el número 
    n = int(input('Ingrese un numero entre 0 y 10: '))
    # Si no se encuentra entre 0 y 10 inclusives, salir del while
    if n >= 0 and n<=10:
        break
