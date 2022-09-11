from os import system
from ingi2i import ingi2i
from suma import Sumar
from resta import Resta
from producto import Producto
from cociente import Cociente
from modulo import Modulo
from potencia import Potencia


#region Suma
print("Calcular sumar: \n")
numeros = (ingi2i())
print(Sumar(numeros[0],numeros[1]))

input("\npulse una tecla para continuar ...\n")
system("cls")
#endregion

#region Resta
print("Calcular Resta: \n")
numeros = (ingi2i())
print(Resta(numeros[0],numeros[1]))

input("pulse una tecla para continuar ...")
system("cls")
#endregion

#region Producto
print("Calcular producto: \n")
numeros = (ingi2i())
print(Producto(numeros[0],numeros[1]))

input("pulse una tecla para continuar ...")
system("cls")
#endregion

#region Cociente
print("Calcular cociente: \n")
numeros = (ingi2i())
print(Cociente(numeros[0],numeros[1]))

input("pulse una tecla para continuar ...")
system("cls")
#endregion

#region Modulo
print("Calcular modulo: \n")
numeros = (ingi2i())
print(Modulo(numeros[0],numeros[1]))

input("pulse una tecla para continuar ...")
system("cls")
#endregion

#region Potencia
print("Calcular potencia: \n")
numeros = (ingi2i())
print(Potencia(numeros[0],numeros[1]))

input("pulse una tecla para continuar ...")
system("cls")
#endregion