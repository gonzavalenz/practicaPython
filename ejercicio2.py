""" 
Diseña un programa que lea un carácter de teclado y muestre por pantalla el mensaje
"Es paréntesis" sólo si el carácter leído es un paréntesis abierto o cerrado. En caso contrario
muestra el mensaje “No es paréntesis”.
"""

# Ingresar un caracter
caracter = input('Ingrese un caracter: ')

# Comparar si el caracter es un paréntesis
if caracter == '(' or caracter == ')': print('El caracter es un paréntesis.')
else: print('El caracter no es un paréntesis.')
    