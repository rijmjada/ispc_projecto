# 17- función que calcule la mediana del vector obtenido en genrnd.

from contextlib import nullcontext
from f12_genrnd import genrnd

def f17():
    lista_rnd = genrnd()      # obtengo la lista random
    lista_rnd.sort()             # ordeno la lista
    len_lista = len(lista_rnd)   # obtengo el tamño de la lista
    mediana = nullcontext
    
    # si el tamaño de la lista es par se calcula la mediana sumando ambos numeros del centro y  dividiendolos por 2
    if(len_lista % 2 == 0):      
        mitad = int(len_lista / 2) 
        mediana = (lista_rnd[mitad - 1] + lista_rnd[mitad]) / 2 # tener en cuenta q los index arrancan en 0 por eso es mitad -1
    else: # si el tamaño de la lista es impar el numero del centro representa la mediana
        mitad = int(len_lista / 2)
        mediana = lista_rnd[mitad]
      
    return mediana


