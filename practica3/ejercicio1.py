'''
Escribir una función que reciba una cadena que contiene un número entero largo y
devuelva una cadena con el número y las separaciones de miles. Por ejemplo, si recibe
’1234567890’, debe devolver ’1.234.567.890’.
'''

# Pedir un número
n = int(input('Ingrese un número: '))

# Con format le indicamos que queremos separar con coma el número
def dar_formato(numero):
    return (f'{numero:,}'.replace(',','.'))

n = dar_formato(n)
print(n)