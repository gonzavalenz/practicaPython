'''
Escribir un programa que verifique si un string es una password correcta. Las reglas para
determinar si es correcta son:
~Debe tener como mínimo 8 caracteres.
~Sólo puede tener letras y dígitos.
~Como mínimo debe tener dos dígitos.
'''

from click import password_option


caracteres = 'abcdefghijklmnopqrstuvwxyz'
digitos = '0123456789'

def verificar_password(password):
    contador_digitos = 0
    if len(password) < 8:
        return False
    for c in password:
        if c not in caracteres and c not in digitos:
            return False
        if c in digitos:
            contador_digitos += 1
    if contador_digitos < 2:
        return False
    return True

password = input('Ingrese el password: ')
print(verificar_password(password))
    