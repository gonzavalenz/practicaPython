""" Escribir un programa que permita ingresar las coordenadas (x,y) de un punto en el plano y
verifique si el punto está dentro del círculo con centro en (0,0) y radio 10, o está fuera o en
la circunferencia. Mostrar los mensajes adecuados. """

# Ingresamos las cordenadas 
x = float(input('Ingrese la coordenada en el eje x: '))
y = float(input('Ingrese la coordenada en el eje y: '))
# r = al radio(10) al cuadrado
r = 10 ** 2

# La suma de los cuadrados de (x,y) tiene que ser menor al radio al cuadrado
if x**2+y**2 < r:
    print('El punto esta dentro de la circunferencia.')
# Si es igual, entonces se encuentra en el limite
elif x**2+y**2 == r:
    print('El punto esta en el limite de la circunferencia.')
# Si es mayor se encuentra por fuera de la circunferencia
else:
    print('El punto no se encuentra en la circunferencia.')

