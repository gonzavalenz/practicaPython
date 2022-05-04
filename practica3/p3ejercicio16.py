'''
Las palabras panvocálicas son las que tienen las cinco vocales. Por ejemplo: centrifugado,
bisabuelo, hipotenusa. Escriba la función esPanvocalica(palabra) que indique si una
palabra es panvocálica o no:
esPanvocalica('educativo') ---> True
esPanvocalica('pedagogico') ---> False
'''

def panvolicas(palabra):
    palabra = palabra.lower()
    if 'a' in palabra and 'e' in palabra and 'i' in palabra and 'o' in palabra and 'u' in palabra:
        return True
    else:
        return False

cadena = input('Ingrese una palabra: ')
print(panvolicas(cadena))