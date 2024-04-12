/*
Enunciado: •Cargar 4 libros a una librería
           •Imprimir los datos de todos los libros de la librería
           •Recuperar e imprimir el segundo libro
           •Eliminar el libro recuperado e imprimir los datos de todos los 
           libros de la librería
           •Eliminar todos los libros de una editorial determinada de todos los
           libros de la libreria.
           •Imprimir todos los libros de la librería

Autor: Franco E. Ibañez
Fecha: 12-04-24
*/

import TadLibro, TadLibreria
from TadLibro import *
from TadLibreria import *

libreria = crearLibreria()

#Carga de datos
for i in range(4):
    L = crearLib()
    n = input("Ingrese Nombre > ")
    e = input("Ingrese Editorial > ")
    a = input("Ingrese Autor > ")
    p = float(input("Ingrese Precio > "))
    cargarLibro(L,n,e,a,p)
    agregarLibro(libreria,L)

#Impresión de datos
for i in range(tamanio(libreria) + 1):
    libro = recuperarLibro(libreria,i)
    print(f"\nLibro {i + 1}")
    print(verNom(libro))
    print(verEdit(libro))
    print(verAutor(libro))
    print(verPre(libro))

#Recupera e imprime el 2do libro
segundoL = recuperarLibro(libreria,2)
print(f"\nLibro 2")
print(verNom(segundoL))
print(verEdit(segundoL))
print(verAutor(segundoL))
print(verPre(segundoL))

#Elimina el 2do libro
eliminarLibro(libreria,segundoL)

#Imprime la libreria completa
for i in range(tamanio(libreria) + 1):
    libro = recuperarLibro(libreria,i)
    print(f"\nLibro {i + 1}")
    print(verNom(libro))
    print(verEdit(libro))
    print(verAutor(libro))
    print(verPre(libro))

#Borrar todos los libros de una Editorial determinada de la librería
edit = input("Ingrese la Editorial a eliminar > ")

i = 1
while i <= tamanio(libreria):
    libro = recuperar(libreria,i)
    if (verEdit(libro) == edit):
        print(verNom(libro))
        print(verEdit(libro))
        print(verAutor(libro))
        print(verPre(libro))
        eliminarLibro(libreria,libro)
    else:
        i += 1


#Imprime la libreria completa
for i in range(tamanio(libreria) + 1):
    libro = recuperarLibro(libreria,i)
    print(f"\nLibro {i + 1}")
    print(verNom(libro))
    print(verEdit(libro))
    print(verAutor(libro))
    print(verPre(libro))
       
