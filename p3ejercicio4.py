'''
Haz un programa que lea dos cadenas que representen sendos números binarios. A
continuación, el programa mostrará el número binario que resulta de sumar ambos (y que
será otra cadena). Si, por ejemplo, el usuario introduce las cadenas ’100’ y ’111’, el
programa mostrará como resultado la cadena ’1011’.
Nota: El procedimiento de suma con acarreo que implementes deberá trabajar
directamente con la representación binaria leída.
'''
# Ingresar los números en binario
num1 = input('Ingrese un número binario: ')
num2 = input('Ingrese otro número binario: ')
acarreo = 0
resultado = ''

# Igualar el largo de los números binarios
if len(num1) > len(num2):
    num2 = num2.zfill(len(num1))
elif len(num1) < len(num2):
    num1 = num1.zfill(len(num2))

# Sumar los números
for d in range(len(num1)-1,-1,-1):
    # Sumamos el número acarreado
    r = acarreo
    # Sumamos si el dígito es 1
    if num1[d] == '1':
        r += 1
    if num2[d] == '1':
        r += 1
    # Sumamos r al resultado
    if r % 2 == 1:
        resultado = '1' + resultado
    else:
        resultado = '0' + resultado
    # Actualizamos el número acarreado 
    if r == 2:
        acarreo = 1
    else:
        acarreo = 0

# Sumar lo que queda en el acarreo si es necesario
if acarreo == 1:
    resultado = '1' + resultado

print(resultado)
