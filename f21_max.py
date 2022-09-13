# 21- función que calcule devuelva el máximo del vector obtenido en genrnd.

from f12_genrnd import genrnd

def f21():
    lista = genrnd()
    lista.sort()
    return lista[len(lista)-1]

print(f21())