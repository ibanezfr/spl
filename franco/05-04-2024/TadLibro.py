# Tad Libro
# Autor: Franco Ibañez
# Fecha: 7 de abril de 2024


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
    libro2[0] = libro1[0]
    libro2[1] = libro1[1]
    libro2[2] = libro1[2]
    libro2[3] = libro1[3]

