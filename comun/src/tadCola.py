# File:     tadCola.py
# Author:   Ibañez F.
# Date:     11 de Mayo de 2024
# Modified: 27 de Mayo de 2024
"""
Spec:
    Cola:
        queue of Tarea
"""


def crearCola():
    """
    Crea una cola vacía

        Args:
            None

        Returns:
            list: Una lista vacia que representa una cola
    """
    cola = []
    return cola


def colaEsVacia(cola):
    """
    Retorna True si la cola no tiene elementos

        Args:
            cola(list): La cola a verificar si esta vacia o no.

        Returns:
            Valor booleano True si la cola esta vacia, False en caso contrario
    """
    return len(cola) == 0


def encolar(cola, elem):
    """
    Agrega un elemento al final de la cola

        Args:
            cola(list): La cola a agregar el elemento
            elem(Tarea): El elemento a agregar a la cola

        Returns:
            None
    """
    cola.append(elem)


def desencolar(cola):
    """
    Retorna y elimina el primer elemento de la cola

        Args:
            cola(list): La cola de la que se eliminara el elemento

        Returns:
            Tarea: devuelve el primer elementod e la cola
    """
    elem = cola.pop(0)
    return elem


def tamanioCola(cola):
    """
    Retorna la cantidad de elementos de la cola

        Args:
            cola(list): La cola de la que se calculara el tamano

        Returns:
            int: La cantidad de elementos en la cola
    """
    return len(cola)


def copiarCola(cola1, cola2):
    """
    Copia los elementos de cola2 en cola1

        Args:
            cola1(list): La cola destino donde se copiaran los elementos
            cola2(list): La cola origen cuyos elementos seran copiados

        Returns:
            None
    """
    aux = crearCola()

    while not colaEsVacia(cola2):
        elem = desencolar(cola2)
        encolar(aux, elem)

    while not colaEsVacia(aux):
        elem = desencolar(aux)
        encolar(cola1, elem)
        encolar(cola2, elem)

def eliminarEncolado(cola, tarea):
    """
    Elimina una tarea de una cola.
    
        Parámetros:
            cola (list): La cola de tareas.
            tarea: La tarea a eliminar de la cola.
    
        Devuelve:
            list: La cola actualizada después de la eliminación.
    """
    colaAux = crearCola()
    
    while tamanioCola(cola) != 0:
        tareaAux = desencolar(cola)
        if sonIguales(tarea, tareaAux):
            continue
        else:
            encolar(colaAux, tareaAux)

    copiarCola(cola, colaAux)


def modificarEncolado(cola, tOriginal, tModificada):
    """
    Intercambia una tarea de referencia por una tarea modificada en una cola.
    
        Args:
            cola (list): La cola de tareas.
            tarea_referencia: La tarea de referencia a buscar en la cola.
            tarea_modificada: La tarea modificada que reemplazará a la tarea de referencia.
    
        Devuelve:
            list: La cola actualizada después del intercambio.
    """
    colaAux = crearCola()

    while tamanioCola(cola) != 0:
        tareaAux = desencolar(cola)
        if sonIguales(tOriginal, tareaAux):
            tareaAux = tModificada
            encolar(colaAux, tareaAux)
        else:
            encolar(colaAux, tareaAux)

    copiarCola(cola, colaAux)

