'''
Hay un tipo de pasatiempos que propone descifrar un texto del que se han suprimido
las vocales. Por ejemplo, el texto ".n .j.mpl. d. p.s.t..mp.s", se descifra sustituyendo cada
punto con una vocal del texto. La solución es "un ejemplo de pasatiempos". Diseña un
programa que ayude al creador de pasatiempos. El programa recibirá una cadena y
mostrará otra en la que cada vocal ha sido reemplazada por un punto.
'''

caracteres = 'aeiou'

def puntos(texto):
    for c in caracteres:
        texto = texto.replace(c,'.')
    return texto 

cadena = input('Ingrese un texto: ')

print(puntos(cadena))