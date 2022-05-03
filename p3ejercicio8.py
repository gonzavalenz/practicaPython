'''
Un ISBN-10 (International Standard Book Number) consiste de 10 dígitos:
d1d2d3d4d5d6d7d8d9d10.
El último dígito, d10, es el dígito verificador que se calcula como sigue:
(d1 x 1 + d2 x 2 + d3 x 3 + d4 x 4 + d5 x 5 + d6 x 6 + d7 x 7 + d8 x 8 + d9 x 9) % 11
Si el dígito verificador es 10, el último dígito es x, de acuerdo a las normas ISBN. Escribir
un programa que permita ingresar los primeros 9 dígitos como una cadena y muestre el
número ISBN.
Ejemplo:
013601267 ---> 0136012671
013031997 ---> 013601267X
'''

# Ingresar el número
isbn = input('Ingrese el ISBN-10: ')
acumulador = 0

if not (len(isbn) == 9):
    print('ISBN-10 no válido')
    exit()

# Recorrer la cadena, multiplicarlo por su posición +1 y sumarlo en el acumulador 
for d, i in zip(isbn,range(len(isbn))):
    acumulador += int(d) * (i + 1)

# Guardar el digito verificador
digito_verificador = acumulador % 11

# Si el digito verificador es 10 agreagamos un x
if digito_verificador == 10:
    isbn += 'x'
else:
    isbn += str(digito_verificador)

print(isbn)
