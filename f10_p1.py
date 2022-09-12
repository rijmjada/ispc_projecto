"""10- función p1, retorna la suma de los 2 primero por el 3er parámetros, usando las
funciones anteriores."""


from f1_suma import Sumar
from f3_producto import Producto

def p1_f10(n1 : int, n2 :int , n3 :int) :
    return Producto(Sumar(n1, n2) , n3)