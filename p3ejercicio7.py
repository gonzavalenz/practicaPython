'''
Escribir un programa que ingrese un número telefónico como un string y convierta los
caracteres a el dígito correspondiente, ejemplo:
 1-800-FLOWERS ---> 1-800-3569377
'''
# Diccionario con las teclas 
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

# String con las letras
letras = 'abcdefghijklmnopqrstuvwxyz'

# Ingresar el número telefónico
number = input('Ingrese el número telefónico: ')

# Recorrer el número para reemplazar las letras
tecla = ''
for c in number:
    if c in letras:
        for tcl, lts in teclado.items():
            if c in lts:
                tecla = str(tcl)
                
        number = number.replace(c,tecla)

# Mostrar el resultado 
print(number)
