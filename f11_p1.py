# 11- función p1, retorna la resta de los 2 primero por el 3er parámetros, usando las funciones anteriores.

from f3_producto import Producto
from f2_resta import Resta

def p1_f11(n1 : int, n2 :int , n3 :int) :
    return Producto(Resta(n1, n2) , n3)