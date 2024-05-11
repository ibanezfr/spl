# File:     tadCola.py
# Author:   Ibañez F.
# Date:     11 de Mayo de 2024 
# Modified: 
"""
Spec:
    Cola:
        queue of Tarea
"""

def crearCola():
    """Crea una cola vacía"""
    cola=[]
    return cola

def esVacia(cola):
    """Retorna True si la cola no tiene elementos"""
    return len(cola)==0

def encolar(cola,elem):
    """Agrega un elemento al final de la cola"""
    cola.append(elem)

def desencolar(cola):
    """Retorna y elimina el primer elemento de la cola"""
    elem = cola.pop(0)
    return elem

def tamanio(cola):
    """Retorna la cantidad de elementos de la cola"""
    return len(cola)

def copiarCola(cola1,cola2):
    """Copia los elementos de cola2 en cola1"""
    aux=creaCola()

    while not esVacia(cola2):
        elem=desencolar(cola2)
        encolar(aux,elem)

    while not esVacia(aux):
        elem=desencolar(aux)
        encolar(cola1,elem)
        encolar(cola2,elem)

