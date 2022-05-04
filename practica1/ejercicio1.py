"""
Diseña un programa que lea la edad de dos personas y diga quién es más joven, la primera o la segunda. Ten en cuenta que ambas pueden tener la misma edad. En tal caso, hazlo saber con un mensaje adecuado.
"""


# Ingresar 2 personas y sus edades
persona1 = input('Ingrese el nombre de la primer persona: ')
edad1 = int(input(f'Ingrese la edad de {persona1}: '))
persona2 = input('Ingrese el nombre de la segunda persona: ')
edad2 = int(input(f'Ingrese la edad de {persona2}: '))

# Comparar la edad de las 2 personas y mostrar cual es más joven
if edad1 < edad2:
    print(f'{persona1} es más joven.')
elif edad1 > edad2:
    print(f'{persona2} es más joven.')
else:
    print(f'{persona1} y {persona2} tienen la misma edad.')
