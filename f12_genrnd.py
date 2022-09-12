"""12- función genrnd que retorna una lista con 50 números aleatorios."""

from random import randint

def genrnd():
    lista = []
    count = 5
    
    while(count > 1):
        lista.append(randint(0, 100))
        count -= 1
        
    return lista


