'''
Escribir una programa que permita ingresar un texto y un caracter e imprima la palabra
más larga en la que se encuentra ese carácter.
'''
# Ingresar el texto y el caracter
texto = input('Ingrese un texto: ')
c = input('Ingrese un caracter: ')

# Separar el texto en una lista
texto_lista = texto.split()
# Lista con las palabras con el caracter
palabras_c = []
max_largo = 0

# Recorrer la lista, agregar a la lista las palabras que tienen el caracter y guardar el max_largo
for palabra in texto_lista:
    if c in palabra:
        palabras_c.append(palabra)
        if len(palabra)>max_largo:
            max_largo = len(palabra)
        

# Comparar en la segunda lista, si la palabra es igual al largo máximo y mostrar la misma.
for palabra in palabras_c:
    if len(palabra) == max_largo:
        print(palabra)

