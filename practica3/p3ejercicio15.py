'''
Dos palabras son anagramas si tienen las mismas letras pero en otro orden. Por ejemplo,
«torpes» y «postre» son anagramas, mientras que «aparta» y «raptar» no lo son, ya que
«raptar» tiene una r de más y una a de menos.
Escriba la función sonAnagramas(p1, p2) que indique si las palabras p1 y p2 son
anagramas:
sonAnagramas('torpes', 'postre') ---> True
sonAnagramas('aparta', 'raptar') ---> False
'''

def son_anagramas(palabra1,palabra2):
    # Ordenar las palabras y comparar
    return sorted(palabra1) == sorted(palabra2)

# Ingresar las palabras.
cadena1 = input('Ingrese una palabra: ')
cadena2 = input('Ingrese otra palabra: ')

print(son_anagramas(cadena1,cadena2))