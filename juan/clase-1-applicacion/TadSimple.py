def crearLibro():
    return ["", "", "", 0]

def cargarLibro(libro, nombre, editorial, autor, precio):
    libro[0] = nombre
    libro[1] = editorial
    libro[2] = autor
    libro[3] = precio

def verNom(libro):
    return libro[0]

def verEdit(libro):
    return libro[1]

def verAutor(libro):
    return libro[2]

def verPre(libro):
    return libro[3]

def modNom(libro, nombre):
    libro[0] = nombre

def modEdit(libro, editorial):
    libro[1] = editorial

def modAutor(libro, autor):
    libro[2] = autor

def modPre(libro, precio):
    libro[3] = precio

def asignarLibro(libro1, libro2):
    libro1[0] = libro2[0]
    libro1[1] = libro2[1]
    libro1[2] = libro2[2]
    libro1[3] = libro2[3]
