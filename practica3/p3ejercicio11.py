'''
La ley de Chargaff dice que en el ADN de un organismo la cantidad de Adenina es la
misma que la de Tiamina, y la de Citosina es la misma que la de Guanina. Dada una
secuencia de nucleótidos del estilo de ATTACCAGTACA... podemos comprobar si cumple
dicha ley de la siguiente forma:
Contamos la cantidad de A, T, C y G presentes en la cadena y calculamos los coeficientes

a = (Na-Nt) / (Na+Nt)   y   c = (Nc-Ng)/(Nc+Ng)

donde NX indica la cantidad de nucleótidos del tipo X presentes en la secuencia.
Partiremos de una cadena que contiene una cantidad indeterminada de caracteres, que
solo pueden ser A, T, G ó C. Calcula a partir de dicha cadena los coeficientes a y c.
'''

#Ingresar la cadena 
cadena = input('Ingrese la cadena: ')
cadena = cadena.upper()


na = 0
nt = 0
nc = 0
ng = 0

# Contar los caracteres
for c in cadena:
    if c == 'A':
        na += 1
    elif c == 'T':
        nt += 1
    elif c == 'C':
        nc += 1
    elif c == 'G':
        ng += 1

# Hacer la formula 
a = (na - nt) / (na + nt)
c = (nc - ng) / (nc + ng)

print(f'a = {a:.2} \tc = {c:.2}')

