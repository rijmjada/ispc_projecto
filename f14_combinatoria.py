 # 14- función que devuelva el producto de las combinaciones posibles de los números generados por la función genrnd tomados de a dos.

from f12_genrnd import genrnd
from f3_producto import Producto

def f14():
    lista_sumas = []
    lista_rnd = genrnd()
    len_rnd = len(lista_rnd)
    
    for i in range(0, len_rnd, 1):
        for j in range(i+1, len_rnd, 1):
            lista_sumas.append(Producto(lista_rnd[i], lista_rnd[j]))
        
    return lista_sumas
      
