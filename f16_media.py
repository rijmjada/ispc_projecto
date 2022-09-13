# 16- función que calcule la media del vector obtenido en genrnd.

from f1_suma import Suma
from f4_cociente import Cociente
from f12_genrnd import genrnd

def f16():
    acumulador = 0
    lista_rnd = genrnd()
    len_rnd = len(lista_rnd)
    
    for i in range(0, len_rnd, 1):
        acumulador = Suma(acumulador,lista_rnd[i])
        
    return Cociente(acumulador,len_rnd)

