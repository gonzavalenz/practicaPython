'''
Escribir un programa que verifique si un string es una password correcta. Las reglas para
determinar si es correcta son:
~Debe tener como mínimo 8 caracteres.
~Sólo puede tener letras y dígitos.
~Como mínimo debe tener dos dígitos.
'''

caracteres = 'abcdefghijklmnopqrstuvwxyz'
digitos = '0123456789'
pswd_ok = True

# Ingresar el password
pswd = input('Ingrese la password: ')

# Verificar el largo
if len(pswd) < 8:
    pswd_ok = False

# Verificar si contiene caracteres y al menos 2 digitos
contador_digitos = 0
for c in pswd:
    if c not in caracteres and c not in digitos:
        pswd_ok = False
    if c in digitos:
        contador_digitos += 1 

if contador_digitos < 2:
    pswd_ok = False

if pswd_ok:
    print('La contraseña es correcta.')
else:
    print('La contraseña es incorrecta.')
