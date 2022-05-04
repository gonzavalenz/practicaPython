'''
Los biólogos usan una secuencia de letras A, C, T, y G para modelar un genoma. Un gen es
un subcadena de un genoma que comienza después de la tripleta ATG y termina con una
tripleta TAG, TAA, ó TGA. La longiutd de una cadena de gen es un múltiplo de 3 y el gen
no contiene a las tripletas ATG, TAG, TAA y TGA. Escribir un programa que permita
ingresar un genoma y muestre todos los genes en el genoma. Si en la cadena no se
encuentran genes, el programa mostrará un mensaje acorde. Ejemplo:
si la cadena es TTATGTTTTAAGGATGGGGCGTTAGTT, el programa mostrará:
TTT
GGGCGT
Si la cadena es TGTGTGTATAT entonces se deberá mostrar "no se encontraron genes".
'''

# Ingresar el genoma
genoma = input('Ingrese un genoma: ')

tripleta_comienzo = 'ATG'
tripleta_fin = ('TAG','TAA','TGA')
genes = []
lista = []
gen = ''

# Recorrer los caracters de genoma y obtener sus indices
for c, i in zip(genoma,range(len(genoma))):
    # Asegurar Genoma mas largo que indice + 2
    if (i+2) < len(genoma):
        # Si la tripleta es una tripleta de comienzo
        if c + genoma[i+1] + genoma [i+2] == tripleta_comienzo:
            cg, fg = 3, 6
            tripleta = genoma[i+cg:i+fg]
            # Mientras que tripleta no sea una tripleta que marque el fin agregar al gen
            while not (tripleta in tripleta_fin):
                gen += tripleta
                cg += 3
                fg += 3
                tripleta = genoma[i+cg:i+fg]
                # Agregar el gen a los genes
                if tripleta in tripleta_fin:
                    genes.append(gen)
            gen = ''

# Mostrar resultado
print(genes)
                  
