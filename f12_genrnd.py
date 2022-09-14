"""12- función genrnd que retorna una lista con 50 números aleatorios."""

from random import randint

def genrnd():
    lista = []
    count = 50
        
    while(count > 0):
        lista.append(randint(0, 100))
        count -= 1
        
    return lista


