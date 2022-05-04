'''
Implementa un programa que muestre todos los múltiplos de 6 entre 6 y 150, ambos
inclusive.
'''

multiplos = []
# Recorrer todos los numeros entre 6 y 150 inclusives
for x in range(6,151):
    # Los multiplos de 6 los agregamos a la lista
    if x % 6 == 0:
        multiplos.append(x)

# Mostrar la lista por consola
print(multiplos)
