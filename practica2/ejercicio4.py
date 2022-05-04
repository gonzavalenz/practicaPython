'''
Construir un programa que permita multiplicar dos números enteros positivos empleando
el método denominado multiplicación rusa. Este método permite calcular el producto de N
por M dela siguiente forma:
En pasos sucesivos se divide M por 2 (división entera) y se multiplica N por 2. Este
proceso se repite hasta que M es 0. El resultado de la multiplicación deseada se obtiene
acumulando aquellos valores sucesivos de N para los cuales el valor correspondiente de M
es impar.
 Ejemplo: 31 * 27
     N | M
 *  31 | 27
 *  62 | 13
   124 | 6
 * 248 | 3
 * 496 | 1
   992 | 0
Si sumamos los valores marcados con un asterisco (que son los que corresponden a un
valor de M impar) obtenemos: 31 + 62 + 248 + 496 = 837 = 31 * 27
'''
# Ingresar los números
m = int(input('Ingrese un numero entero: '))
n = int(input('Ingrese un numero entero: '))
acumulador = 0

# Mientras m sea mayor a 0 repetir el proceso
while m >= 1:
    # Si m es impar, sumamos n al acumulador
    if m % 2 == 1:
        acumulador += n
    # Dividimos m y multiplicamos n 
    m = m // 2
    n = n * 2

# Mostramos el resultado en pantalla
print(acumulador)
