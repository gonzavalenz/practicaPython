'''
Escribir un programa que permita ingresar el mes y el año y muestre la cantidad de días 
del mes. Por ejemplo, si el usuario ingresa mes 2 y año 2000, el programa debe responder
que Febrero 2000 tiene 29 días. Si el usuario ingresa mes 3 y año 2005, el programa
responderá que Marzo 2005 tiene 31 días.
'''
# Diccionario con los meses
meses = {
    1:'Enero',
    2:'Febrero',
    3:'Marzo',
    4:'Abril',
    5:'Mayo',
    6:'Junio',
    7:'Julio',
    8:'Agosto',
    9:'Septiembre',
    10:'Octubre',
    11:'Noviembre',
    12:'Diciembre'
}

# Meses con 31 dias y con 30  dias
meses31 = [1,3,5,7,8,10,12]
meses30 = [4,6,9,11]

mes = int(input('Ingrese el mes en formato numero: '))
year = int(input('Ingrese el year: '))

# Variable que identifica si un año es biciesto o no.
year_bi = False

# Buscamos si el mes se encuentra en meses31 o meses30.
if mes in meses31:
   print(f'{meses[mes]} {year} tiene 31 dias')
elif mes in meses30:
   print(f'{meses[mes]} {year} tiene 30 dias')
# Si el mes es 2 puede tener 28 o 29 dias.
elif mes == 2:
    # Los años biciestos son multiplos de 4, no son de 100 pero si de 400
    if year % 4 == 0 and year % 100 != 0:
        year_bi = True
    elif year % 4 == 0 and year % 400 == 0:
        year_bi = True
    if year_bi:
        print(f'{meses[mes]} {year} tiene 29 dias')
    else:
        print(f'{meses[mes]} {year} tiene 28 dias')
