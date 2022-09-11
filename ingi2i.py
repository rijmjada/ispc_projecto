
from array import array
from contextlib import nullcontext

def ingi2i() :
    list = []
    n1 = "" 
    n2 = ""

    while(type(n1) != int):
        try:
            n1 = int(input("Ingrese 1° número entero: "))
            list.insert(0,n1)
        except ValueError:
            print("Error.Debes escribir un número entero.")
            continue

    while(type(n2) != int):
        try:
            n2 = int(input("Ingrese 2° número entero: "))   
            list.insert(1,n2)
        except ValueError:
            print("Error.Debes escribir un número entero.")
            continue

    return list        
    input("pulse una tecla para cotinuar...")