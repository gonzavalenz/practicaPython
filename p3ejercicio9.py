'''
ISBN-13 es un nuevo estandar para identificar libros. Usa 13 dígitos:
d1d2d3d4d5d6d7d8d9d10d11d12d13 .
El último dígito, es el dígito verificador y se calcula con la siguiente fórmula:
10 - (d1 + 3*d2 + d3 + 3*d4 + d5 + 3*d6 + d7 + 3*d8 + d9 + 3*d10 + d11 + 3*d12) % 10
Si el dígito verificador es 10 se reemplaza por 0. El programa deberá permitir ingresar un
número como un string y mostrar el ISBN-13, ejemplo:
978013213080 ---> 9780132130806
978013213079 ---> 9780132130790
'''

isbn = input('Ingrese el número de isbn: ')

acumulador = 0


for d, i in zip(isbn,range(len(isbn))):
    i += 1
    d = int(d)
    if i % 2 == 0:
        acumulador += 3 * d
    else:
        acumulador += d

dig_ver = 10 - acumulador % 10

if dig_ver == 10:
    isbn += '0'
else: 
    isbn += str(dig_ver)

print(isbn)
