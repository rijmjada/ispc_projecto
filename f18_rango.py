#18- función que calcule el rango del vector obtenido en genrnd.

# Entendiendo al rango con la siguiente definición: 
# El rango es un valor numérico que indica la diferencia entre el valor máximo y el mínimo de una población o muestra estadística.

from contextlib import nullcontext
from f12_genrnd import genrnd

def f18():
    lista_rnd = genrnd()
    lista_rnd.sort()             
    len_lista = len(lista_rnd)   
    
    return lista_rnd[len_lista - 1] - lista_rnd[0]

