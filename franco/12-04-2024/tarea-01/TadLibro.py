'''
Tad Libro
Autor: Franco Ibañez
Fecha: 7 de abril de 2024
'''

def crearLib():
    #Crea un libro vacío
    libro=["","","",0]
    return libro

def cargarLib(libro,n,e,a,p):
    #Carga los datos de un libro
    # Nom, Edit, Autor, Precio
    libro[0] = n
    libro[1] = e
    libro[2] = a
    libro[3] = p

def verNom(libro):
    #Retorna el nombre de un libro
    return libro[0]

def verEdit(libro):
    #Retorna la editorial de un libro
    return libro[1]

def verAutor(libro):
    #Retorna el autor de un libro
    return libro[2]

def verPre(libro):
    #Retorna el autor de un libro
    return libro[3]

def modNom(libro,n):
    #Modifica el nombre de un libro
    libro[0] = n

def modEdit(libro,e):
    #Modifica la editorial de un libro
    libro[1] = e

def modAutor(libro,a):
    #Modifica el autor de un libro
    libro[2] = a

def modPre(libro,p):
    #Modifica el precio de un libro
    libro[3] = p

def asignarLib(libro1,libro2):
    #Asigna datos de un libro en otro
    modNom(libro1, verNom(libro2))
    modEdit(libro1, verEdit(libro2))
    modAutor(libro1, verAutor(libro2))
    modPre(libro1, verPre(libro2))

