cadena = input('Ingrese un número: ')
cont = 0
cada_tres = 0 
cadena = cadena[::-1]
nueva_cadena = ''
while cont < len(cadena):
    if cada_tres == 3:
        nueva_cadena = nueva_cadena + '.'
        cada_tres = 0
    nueva_cadena += cadena[cont]
    cont += 1
    cada_tres += 1

cadena = nueva_cadena[::-1]
print(cadena)
print('')