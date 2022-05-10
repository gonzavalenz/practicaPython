'''
La empresa RawInput S.A. desea hacer una clasificación de sus clientes según su ubicación
geográfica. Para esto, analizará su base de datos de correos electrónicos con el fin obtener
información sobre el lugar de procedencia de cada cliente.
En una dirección de correo electrónico, el dominio es la parte que va después de la arroba,
y el TLD es lo que va después del último punto. Por ejemplo, en la dirección
fulano.de.tal@alumnos.usm.cl, el dominio es alumnos.usm.cl y el TLD es cl.
Algunos TLD no están asociados a un país, sino que representan otro tipo de entidades.
Estos TLD genéricos son los siguentes:
genericos = {'com', 'gov', 'edu', 'org', 'net', 'mil'}
1. Escriba la función obtenerDominios(correos) que reciba como parámetro una lista
de correos electrónicos, y retorne la lista de todos los dominios, sin repetir, y en
orden alfabético.
2. Escriba la función contarTld(correos) que reciba como parámetro la lista de correos
electrónicos, y retorne un diccionario que asocie a cada TLD la cantidad de veces
que aparece en la lista. No debe incluir los TLD genéricos.

c = ['fulano@usm.cl', 'erika@lala.de', 'li@zi.cn', 'a@a.net', 'gudrun@lala.de',
'otto.von.d@lorem.ipsum.de', 'org@cn.de.cl', 'yayita@abc.cl', 'jozin@baz.cz', 'jp@foo.cl',
'dawei@hao.cn', 'pepe@gmail.com', 'ana@usm.cl', 'polo@hotmail.com', 'fer@x.com',
'ada@alumnos.usm.cl', 'dj@foo.cl', 'jan@baz.cz', 'd@abc.cl']
obtenerDominios(c) se obtiene:
['abc.cl', 'alumnos.usm.cl', 'baz.cz', 'cn.de.cl', 'foo.cl',
'hao.cn', 'lala.de', 'lorem.ipsum.de', 'usm.cl', 'zi.cn']
contarTld(c) se obtiene: {'cz': 2, 'de': 3, 'cn': 2, 'cl': 8}
'''

genericos = ['com', 'gov', 'edu', 'org', 'net', 'mil']

def obtenerDominios(correos):
    lista = []
    for correo in correos:
        correo = correo.split('@')[1]
        if correo not in lista and correo.split('.')[-1] not in genericos:
            lista.append(correo)
    lista.sort()
    return lista

def contarTld(correos):
    tlds = {}
    for correo in correos:
        tld = correo.split('.')[-1]
        if tld not in genericos:
            if tld not in tlds:
                tlds[tld] = 1
            else:
                tlds[tld] += 1
    return tlds


mail = ['fulano@usm.cl', 'erika@lala.de', 'li@zi.cn', 'a@a.net','gudrun@lala.de',
'otto.von.d@lorem.ipsum.de', 'org@cn.de.cl', 'yayita@abc.cl', 'jozin@baz.cz', 'jp@foo.cl',
'dawei@hao.cn', 'pepe@gmail.com', 'ana@usm.cl', 'polo@hotmail.com', 'fer@x.com',
'ada@alumnos.usm.cl', 'dj@foo.cl', 'jan@baz.cz', 'd@abc.cl']

print(obtenerDominios(mail))
print(contarTld(mail))