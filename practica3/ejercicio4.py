'''
Haz un programa que lea dos cadenas que representen sendos números binarios. A
continuación, el programa mostrará el número binario que resulta de sumar ambos (y que
será otra cadena). Si, por ejemplo, el usuario introduce las cadenas ’100’ y ’111’, el
programa mostrará como resultado la cadena ’1011’.
Nota: El procedimiento de suma con acarreo que implementes deberá trabajar
directamente con la representación binaria leída.
'''

def verificar_binario(binario):
    digitos = '01'
    binario = str(binario)
    for d in binario:
        if d not in digitos:
            return False
    return True


def sumar_binarios(num1,num2):
    acarreo = 0
    resultado = ''
    num1, num2 = str(num1), str(num2)
    verif = verificar_binario(num1) and verificar_binario(num2)
    if verif == False:
        return 'No se pueden sumar'
    lennum1 = len(num1)
    lennum2 = len(num2)
    maxlen = max(lennum1,lennum2)
    # Igualar el largo de las cadenas rellenando con 0
    if lennum1 != maxlen:
        num1 = num1.zfill(maxlen)
    else:
        num2 = num2.zfill(maxlen)

    for d1, d2 in zip(num1[::-1],num2[::-1]):
        r = acarreo
        
        if d1 == '1':
            r += 1
        if d2 == '1': 
            r += 1 
        # Obtener el resto y sumarlo al número
        if r % 2 == 1:
            resultado = '1' + resultado
        else:
            resultado = '0' + resultado
        # Agregar al acarreo
        if r >= 2:
            acarreo = 1
        else:
            acarreo = 0
    # El sobrante del acarreo, sumarlo al resultado
    if acarreo == 1:
        resultado = '1' + resultado

    return resultado

n1 = input('Ingrese un número binario: ')
n2 = input('Ingrese un número binario: ')

resultado = sumar_binarios(n1,n2)

print(resultado)