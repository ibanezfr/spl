# File:     tadCola.py
# Author:   Ibañez F.
# Date:     11 de Mayo de 2024
# Modified: 27/05/2024
"""
Spec:
    Cola:
        queue of Tarea
"""
from tadTarea import sonIguales

def crearCola():
    """Crea una cola vacía"""
    cola = []
    return cola


def colaEsVacia(cola):
    """Retorna True si la cola no tiene elementos"""
    return len(cola) == 0


def encolar(cola, elem):
    """Agrega un elemento al final de la cola"""
    cola.append(elem)


def desencolar(cola):
    """Retorna y elimina el primer elemento de la cola"""
    elem = cola.pop(0)
    return elem


def tamanioCola(cola):
    """Retorna la cantidad de elementos de la cola"""
    return len(cola)


def copiarCola(cola1, cola2):
    """Copia los elementos de cola2 en cola1"""
    aux = crearCola()

    while not colaEsVacia(cola2):
        elem = desencolar(cola2)
        encolar(aux, elem)

    while not colaEsVacia(aux):
        elem = desencolar(aux)
        encolar(cola1, elem)
        encolar(cola2, elem)


def eliminarEncolado(cola, tarea):
    """Recibe una cola y una tarea como argumentos. Busca la tarea
    dentro de la cola y, si la encuentra, la elimina."""
    colaAux = crearCola()
    
    while tamanioCola(cola) != 0:
        tareaAux = desencolar(cola)
        if sonIguales(tarea, tareaAux):
            continue
        else:
            encolar(colaAux, tareaAux)

    copiarCola(cola, colaAux)


def modificarEncolado(cola, tOriginal, tModificada):
    """Recibe una cola, una tarea de referencia y una tarea modificada, busca
    la tarea de referencia en la cola y, si la encuentra, la intercambia
    por la tarea modificada"""
    colaAux = crearCola()

    while tamanioCola(cola) != 0:
        tareaAux = desencolar(cola)
        if sonIguales(tOriginal, tareaAux):
            tareaAux = tModificada
            encolar(colaAux, tareaAux)
        else:
            encolar(colaAux, tareaAux)

    copiarCola(cola, colaAux)

