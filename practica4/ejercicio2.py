'''
Dada una matriz de n x m elementos (una lista que contiene n listas de tamaño m) donde
cada fila representa una cadena de ADN de longitud m como la siguiente:

    A T C C A G C T
    G G G C A A C T
    A T G G A T C T
    A A G C A A C C
    T T G G A A C T
    A T G C C A T T
    A T G G C A C T

Obtener otra matriz de la siguiente forma:

A   5 1 0 0 5 5 0 0    
C   0 0 1 4 2 0 6 1
G   1 1 6 3 0 1 0 0
T   1 5 0 0 0 1 1 6

donde en cada fila tenemos la cantidad de repeticiones de cada letra por columnas que
forma un codón, además obtener una lista donde se muestra por columnas cuál es el
símbolo que se repite más veces, para el ejemplo anterior se tiene como resultado:

    A T G C A A C T

'''

matriz = [
    ['A','T','C','C','A','G','C','T'],
    ['G','G','G','C','A','A','C','T'],
    ['A','T','G','G','A','T','C','T'],
    ['A','A','G','C','A','A','C','C'],
    ['T','T','G','G','A','A','C','T'],
    ['A','T','G','C','C','A','T','T'],
    ['A','T','G','G','C','A','C','T']
]


profile = {
    'A':[0,0,0,0,0,0,0,0],   
    'C':[0,0,0,0,0,0,0,0],
    'G':[0,0,0,0,0,0,0,0],
    'T':[0,0,0,0,0,0,0,0]
}

consensus = []

for lista in matriz:
    for i in range(len(lista)):
        if lista[i] == 'A':
            profile['A'][i] += 1 
        if lista[i] == 'C':
            profile['C'][i] += 1 
        if lista[i] == 'G':
            profile['G'][i] += 1 
        if lista[i] == 'T':
            profile['T'][i] += 1 

for letra, lista in profile.items():
    print(letra)
    print(lista)

max1 = ''
max2 = ''
for i in range(len(profile['A'])):
    if profile['A'][i] >= profile['C'][i]:
        max1 = 'A'
    else:
        max1 = 'C'
    if profile['G'][i] >= profile['T'][i]:
        max2 = 'G'
    else:
        max2 = 'T'
    if profile[max1][i] >= profile[max2][i]:
        consensus.append(max1)
    else:
        consensus.append(max2)
        
print(consensus)