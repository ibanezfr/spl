import TadSimple

from TadSimple import *

def leerLibro(libro):
    nombre = input("Ingrese el nombre del libro: ")
    editorial = input("Ingrese la editorial del libro: ")
    autor = input("Ingrese el autor del libro: ")
    precio = float(input("Ingrese el precio del libro: "))
    cargarLibro(libro, nombre, editorial, autor, precio)

def mostrarLibro(libro):
    print("Nombre: " + verNom(libro))
    print("Editorial: " + verEdit(libro))
    print("Autor: " + verAutor(libro))
    print("Precio: " + str(verPre(libro)))

lib1 = crearLibro()
leerLibro(lib1)
print("Libro 1:")
mostrarLibro(lib1)

lib2 = crearLibro()
leerLibro(lib2)
print("Libro 2:")
mostrarLibro(lib2)

#Mustro el nombre del libro de menor precio y aumento el mismo en 10%
if verPre(lib1) < verPre(lib2):
    print("El libro de menor precio se llama: " + verNom(lib1))
    modPre(lib1, verPre(lib1) * 1.1)
elif verPre(lib1) > verPre(lib2):
    print("El libro de menor precio se llama: " + verNom(lib2))
    modPre(lib2, verPre(lib2) * 1.1)
else:
    print("Los dos libros tienen el mismo precio")
