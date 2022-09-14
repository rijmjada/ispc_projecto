# 22- función genrnd que retorna una lista con 500.000.000.000.000.000 números aleatorios.
from random import randint

def f22():
    lista = []
    count = 500000000000000000
        
    while(count > 0):
        lista.append(randint(0, 100))
        count -= 1
        
    return lista
