'''
Una palabra es "alfabética" si todas sus letras están ordenadas alfabéticamente. Por
ejemplo, "amor", "chino" e "himno" son palabras "alfabéticas". Diseña un programa que lea
una palabra y nos diga si es alfabética o no.
'''

# Ingresar la palabra
palabra = input('Ingrese una palabra: ')
# Val: Validar que la palabra esté ordenada
val = True

# Recorrer la palabra y el rango de su largo
for c, p in zip(palabra, range(len(palabra))):
    # Si p es 0, pasar a la siguiente letra
    if p == 0:
        pass
    # Si la latra (c) es menor a letra anterior, val = False
    elif c < palabra[p-1]:
        val = False
        break

# Mostrar el resultado
if val:
    print(f'La palabara {palabra} esta ordenada.')
else:
    print(f'La plabra {palabra} no está ordenada.')


