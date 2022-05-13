'''
Una palabra es "alfabética" si todas sus letras están ordenadas alfabéticamente. Por
ejemplo, "amor", "chino" e "himno" son palabras "alfabéticas". Diseña un programa que lea
una palabra y nos diga si es alfabética o no.
'''

def alfabetica(palabra):
    # Recorrer la palabra
    for letra, i in zip(palabra,range(len(palabra))):
        if i != 0:
            # Si la letra es menor a la anterior retornar falso
            if letra < palabra[i-1]:
                return False
    return True

palabra = input('Ingrese una palabra: ')

if alfabetica(palabra):
    print('La palabra es alfabética.')
else:
    print('La palabra no es alfabética.')