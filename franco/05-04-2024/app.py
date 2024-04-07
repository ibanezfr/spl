'''
Enunciado de Aplicación

Cargar dos libros
Imprimir los datos de cada libro
Imprimir noombre de libro de menor precio
Incremente el precio en un 10% del libro de menor precio

Autor: Franco Ibañez
Fecha: 7 de abril de 2024
'''

import TadLibro
from TadLibro import *

#Definición Variables
L1 = crearLib()
L2 = crearLib()


#Carga de Datos
n = input("Ingrese Nombre L1 > ")
e = input("Ingrese Editorial L1 > ")
a = input("Ingrese Autor L1 > ")
p = float(input("Ingrese Precio L1 > "))
cargarLib(L1,n,e,a,p)

n = input("Ingrese Nombre L2 > ")
e = input("Ingrese Editorial L2 > ")
a = input("Ingrese Autor L2 > ")
p = float(input("Ingrese Precio L2 > "))
cargarLib(L2,n,e,a,p)

#Impresión de Datos
print("\nLibro 1:")
print("\t" + verNom(L1))
print("\t" + verEdit(L1))
print("\t" + verAutor(L1))
print("\t$" + str(verPre(L1)))

print("\nLibro 2:")
print("\t" + verNom(L2))
print("\t" + verEdit(L2))
print("\t" + verAutor(L2))
print("\t$" + str(verPre(L2)))

if verPre(L1) < verPre(L2):
    print("\nMenor precio: " + verNom(L1) + "\n")
    modPre(L1, verPre(L1) * 1.1)
else:
    print("\nMenor precio: " + verNom(L2) + "\n")
    modPre(L2, verPre(L2) * 1.1)
