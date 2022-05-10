'''
Debido a la gran cantidad de crímenes y casos sin resolver, la policía local ha decidido
implementar su propio sistema de reconocimiento de sospechosos con la técnica basada en
el uso del DNA.
Para esto la policía mantiene dos listas de información; la primera contiene el nombre de
las personas registradas en la región (nombre y apellido), la otra, un cromosoma
representativo del DNA de cada una de esas personas.
Por simplicidad, un cromosoma se considera como una cadena de 0 (ceros) y 1 (unos), de
largo 20.
El método para determinar el sospechoso, es el siguiente:
• Se obtiene una muestra del cromosoma del autor del delito (20 caracteres)
• Se busca en la lista de cromosomas, aquel cromosoma que esmás parecido a la
muestra. El más parecido se define como el cromosoma que tiene más genes
(caracteres) iguales a la muestra.
• Al terminar la búsqueda, se muestra el nombre de la persona cuyo cromosoma es
sospechoso, con el porcentaje de parentesco.
La información inicial del programa se debe ingresar directamente en el código, es decir,
nombres y cromosomas, en cambio la secuencia encontrada en la escena del crimen, debe
ser ingresada por el usuario.
Desarrolle un programa que lleve a cabo la búsqueda descrita a partir de una muestra de
entrada.
Consideremos, personas como Pedro, Juan y Diego. Sus secuencias serán
• 00000101010101010101
• 00101010101101110111
• 00100010010000001001
Ingrese secuencia: 01010101000011001100
El culpable es Pedro con un parentesco de 60%
'''

personas = {
    'Pedro': '00000101010101010101',
    'Juan': '00101010101101110111',
    'Diego': '00100010010000001001'
}

def sospechoso(dna_sospechoso):
    max_porcentaje = 0
    for nombre, dna in personas.items():
        contador = 0
        porcentaje = 0 
        for gs, gen in zip(dna_sospechoso,dna):
            if gs == gen:
                contador += 1
        porcentaje = contador*100/20
        if porcentaje > max_porcentaje:
            max_porcentaje = porcentaje
            culpable = nombre
    return (f'El culpable es {culpable} con un parentesco de {max_porcentaje}%.')

while True:
    try:
        dna_sospechoso = input('Ingrese el dna del sospechoso: ')
        assert len(dna_sospechoso) == 20
        break
    except:
        print('DNA no es válido.')


print(sospechoso(dna_sospechoso))
                  