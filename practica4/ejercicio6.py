'''
Diseña una función que reciba una lista de cadenas y devuelva el prefijo común más
largo. Por ejemplo, la cadena "pol" es el prefijo común más largo de esta lista:
['poliedro', 'policia', 'polifona', 'polinizar', 'polaridad', 'politica']
'''

def prefijos(palabras):
    aux = palabras[0]
    for palabra in palabras:
        prefijo = ''
        try:    
            for i in range(len(aux)):
                if palabra[i] == aux[i]:
                    prefijo += aux[i]
        except IndexError:
            prefijo = palabra
        aux = prefijo

    return prefijo


lista = ['poliedro','policia','polifona','polinizar','polaridad','politica']
resultado = prefijos(lista)
print(resultado)