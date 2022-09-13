# 9- función p1, retorna el producto de los 2 primero más el 3er parámetros, usando las funciones anteriores.

from f3_producto import Producto

def p1_f9(n1 : int, n2 :int , n3 :int) :
    return Producto(Producto(n1, n2) , n3)
