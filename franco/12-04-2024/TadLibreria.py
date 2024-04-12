# Tad Librería

def crearLibreria():
    #Crea una librería vacía
    libreria=[]
    return libreria

def agregarLibro(libreria,l):
    #Agrega un libro l de la librearia 
    libreria.append(l)

def eliminarLibro(libreria,l):
    #Elimina un libro l de la libreria
    libreria.remove(l)

def recuperarLibro(libreria,l):
    #Retorna el libro de la posición iésimo
    return libreria[i-1]

def tamanio(libreria):
    #Retorna la cantidad de libros de la libreria
    return len(libreria)

