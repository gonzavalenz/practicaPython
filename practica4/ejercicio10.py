'''
Ejercicio 10:
En el juego ScrabbleTM, cada letra tiene asociado un valor numérico. El puntaje total de una
palabra es la suma de los valores numéricos de cada letra. Las letras más comunes tienen
menor valor que las letras menos comunes. Los puntos asociados a cada letra se muestran
en la siguiente tabla:
puntos      letras
1           A,E,I,L,N,O,R,S,T, U
2           D,G
3           B,C,M,P
4           F,H,V,W,Y
5           K
8           J,X
10          Q,Z
Escribir un programa que calcule y muestre el puntaje de una palabre. Crear un
diccionario para almacenar la tabla anterior.
'''

diccionario = {
    1: ['A','E','I','L','N','O','R','S','T','U'],
    2: ['D','G'],
    3: ['B','C','M','P'],
    4: ['F','H','V','W','Y'],
    5: ['K'],
    8: ['J','X'],
    10: ['Q','Z']
}

def puntaje_palabra(palabra):
    puntaje = 0
    for l in palabra:
        for puntos, letras in diccionario.items():
            if l in letras:
                puntaje += puntos
    return puntaje

while True:
    try:
        palabra_ingresada = input('Ingrese una palabra: ')
        assert palabra_ingresada.isalpha()
        palabra_ingresada = palabra_ingresada.upper()
        break
    except:
        print('Palabra ingresada incorrecta.')

resultado = puntaje_palabra(palabra_ingresada)

print(f'El puntaje de la palabra "{palabra_ingresada}" es: {resultado}.')