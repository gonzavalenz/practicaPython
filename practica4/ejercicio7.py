'''
La ciudad de Babilonia tiene una alta congestión de vehículos circulando por sus calles.
Las autoridades han decidido aplicar restricción vehicular para descongestionar la ciudad
en base a las patentes de los vehículos.
La patente de un vehículo es un string de cuatro letras y dos dígitos, y la restricción
depende sólo del penúltimo dígito. Por ejemplo, para la patente GEEA78, el dígito 7 es el
utilizado para evaluar la restricción.
La restricción vehícular de los días hábiles de la semana se encuentra ingresada en el
diccionario digitos, cuyas llaves son los días de la semanas, y cuyos valores son tuplas de
cuatro enteros que representan los dígitos con restricción de ese día.
• Implemente la función estaConRestriccion(digitos,dia, patente), que indique si el
vehículo está o no con restricción.
• Implemente la función diasConRestriccion(digitos,patente), que retorne la lista de
los días en que el vehículo no puede circular.
• Implemente la función diasSinRestriccion(digitos,patente), que retorne el conjunto
de los días en que el vehículo sí puede circular.
digitos = {'lunes': (3, 4, 5, 6), 'martes': (7, 8, 9, 0),...,'miercoles': (1, 2, 3, 4), 'jueves':
(5, 6, 7, 8), ... , 'viernes': (9, 0, 1, 2)}
estaConRestriccion(digitos, 'lunes', 'BBDT35') ---> True
diasConRestriccion(digitos, 'BBDT35') ---> ['lunes', 'miercoles']
diasSinRestriccion(digitos, 'BBDT35') ---> set(['jueves', 'martes', 'viernes'])
'''

from curses.ascii import isalpha


digitos = {
    'lunes':        ('3', '4', '5', '6'),
    'martes':       ('7', '8', '9', '0'),
    'miercoles':    ('1', '2', '3', '4'),
    'jueves':       ('5', '6', '7', '8'),
    'viernes':      ('9', '0', '1', '2')
    }

def estaConRestriccion(digitos,dia,patente):
    if patente[5] in digitos[dia]:
        return True 
    else: 
        return False

def diasConRestriccion(digitos,patente):
    dias = []
    for dia, digit in digitos.items():
        if patente[5] in digit:
            dias.append(dia)
    return dias

def diasSinRestriccion(digitos,patente):
    dias = []
    for dia, digit in digitos.items():
        if patente[5] not in digit:
            dias.append(dia)
    return dias


while True:
    try:
        patente = input('Ingrese la patente (XXXX99): ')
        assert patente[:4].isalpha() and patente[4:].isdigit()
        break
    except:
        patente = input('Ingrese la patente (XXXX99): ')

while True:
    try:
        dia = input('Ingrese el día: ')
        assert dia in ['lunes','martes','miercoles','jueves','viernes']
        break
    except:
        dia = input('Ingrese el día: ')

resultado1 = estaConRestriccion(digitos,dia,patente)
resultado2 = diasConRestriccion(digitos,patente)
resultado3 = diasSinRestriccion(digitos,patente)

if resultado1:
    print('Está con restricción.')
else:
    print('Está sin restricción.')

print(f'Los días con restricción son {resultado2}')
print(f'Los días sin restricción son {resultado3}')