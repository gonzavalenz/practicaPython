'''
Las palabras panvocálicas son las que tienen las cinco vocales. Por ejemplo: centrifugado,
bisabuelo, hipotenusa. Escriba la función esPanvocalica(palabra) que indique si una
palabra es panvocálica o no:
esPanvocalica('educativo') ---> True
esPanvocalica('pedagogico') ---> False
'''

def panvolicas(palabra):
    palabra = palabra.lower()
    vocales = ['a','e','i','o','u']
    # Comprobar si todas las vocales estan en la palabra
    for vocal in vocales:
        if vocal not in palabra:
            return False
    return True

cadena = input('Ingrese una palabra: ')
print(panvolicas(cadena))