'''
Escribe un programa que lea dos cadenas y devuelva el prefijo común más largo de
ambas. Ejemplo: las cadenas "politécnico" y "polinización" tienen como prefijo común más
largo a la cadena "poli".
'''

# Ingresar las cadenas
cadena1 = input('Ingrese la primer cadena: ')
cadena2 = input('Ingrese otra cadena: ')
prefijo = ''

# Recorrer las 2 cadenas caracter por caracter
for c1, c2 in zip(cadena1,cadena2):
    # Si los caracteres son igueles, los agregamos al prefijo
    if c1 == c2:
        prefijo += c1
    # Si son distintos, salir del for
    else:
        break

print(prefijo)