from os import system

from ingi2i import ingi2i

from f1_suma import Sumar
from f2_resta import Resta
from f3_producto import Producto
from f4_cociente import Cociente
from f5_modulo import Modulo
from f6_potencia import Potencia
from f9_p1 import p1_f9
from f10_p1 import p1_f10
from f11_p1 import p1_f11
from f12_genrnd import genrnd
from f13_combinatoria import f13

#region f1 Suma
print("Calcular sumar: \n")
numeros = ingi2i()
print(Sumar(numeros[0],numeros[1]))

input("\npulse una tecla para continuar ...\n")
system("cls")
#endregion

#region f2 Resta
print("Calcular Resta: \n")
numeros = ingi2i()
print(Resta(numeros[0],numeros[1]))

input("pulse una tecla para continuar ...")
system("cls")
#endregion

#region f3 Producto
print("Calcular producto: \n")
numeros = ingi2i()
print(Producto(numeros[0],numeros[1]))

input("pulse una tecla para continuar ...")
system("cls")
#endregion

#region f4 Cociente
print("Calcular cociente: \n")
numeros = ingi2i()
print(Cociente(numeros[0],numeros[1]))

input("pulse una tecla para continuar ...")
system("cls")
#endregion

#region f5 Modulo
print("Calcular modulo: \n")
numeros = ingi2i()
print(Modulo(numeros[0],numeros[1]))

input("pulse una tecla para continuar ...")
system("cls")
#endregion

#region f6 Potencia
print("Calcular potencia: \n")
numeros = ingi2i()
print(Potencia(numeros[0],numeros[1]))

input("pulse una tecla para continuar ...")
system("cls")
#endregion

#region f9 p1
print("función p1, retorna el producto de los 2 primero más el 3er parámetros, usando las funciones anteriores.")
numeros = ingi2i()
tercero = int(input("ingrese 3° numero: "))
print(p1_f9(numeros[0],numeros[1],tercero))

input("pulse una tecla para continuar ...")
system("cls")
#endregion 

#region f10 p1
print("función p1, retorna la suma de los 2 primero por el 3er parámetros, usando las funciones anteriores.")
numeros = ingi2i()
tercero = int(input("ingrese 3° numero: "))
print(p1_f10(numeros[0],numeros[1], tercero))

input("pulse una tecla para continuar ...")
system("cls")
#endregion 

#region f11 p1
print("función p1, retorna la resta de los 2 primero por el 3er parámetros, usando las funciones anteriores.")
numeros = ingi2i()
tercero = int(input("ingrese 3° numero: "))
print(p1_f11(numeros[0],numeros[1], tercero))

input("pulse una tecla para continuar ...")
system("cls")
#endregion 

#region f12 genrnd
print("12- función genrnd que retorna una lista con 50 números aleatorios.")
for item in (genrnd()):
    print(item, end=" - ")

input("pulse una tecla para continuar ...")
system("cls")
#endregion

#region f13 combinatoria
print("# 13- función que devuelva la suma de las combinaciones posibles de los números generados por la función genrnd tomados de a dos.")
for item in (f13()):
    print(item, end=" - ")

input("pulse una tecla para continuar ...")
system("cls")
#endregion