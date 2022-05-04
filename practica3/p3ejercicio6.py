'''
Escribir un programa que retorne el número que le corresponde a una letra en mayúscula
de acuerdo al teclado telefónico.
'''
# Diccionario con las teclas del teléfono
teclado = {
    2:'abc',
    3:'def',
    4:'ghi',
    5:'jkl',
    6:'mno',
    7:'pqrs',
    8:'tuv',
    9:'wxyz'
}

# Ingresar la letra 
l = input('Ingrese una letra mayúscula: ')
l = l.lower()
tecla = ''
pos = 0

# Recorrer el diccionario, guardar la tecla donde está la letra y su posición 
for n, letras in teclado.items():
    if l in letras:
        tecla = str(n)
        pos = letras.index(l) + 1

# Mostrar el resultado en consola
print(f'#{tecla * pos}')


