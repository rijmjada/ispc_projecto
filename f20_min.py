# 20- función que calcule devuelva el mínimo del vector obtenido en genrnd.

from f12_genrnd import genrnd

def f20():
    lista = genrnd()
    lista.sort()
    return lista[0]

