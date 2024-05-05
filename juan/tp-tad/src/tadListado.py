"""
Spec:
    Listado:
        List of Tareas
"""

def crearListado():
    """Retorna un listado de tareas vacio"""
    listado = []
    return listado

def agregarTarea(listado, t):
    """Agrega una tarea al listado de tareas
        Parametros:
            listado (Listado): Listado al cual agregarle la tarea
            t (Tarea): Tarea a ser agregada
    """
    listado.append(tarea)

def eliminarTarea(listado, t):
    """Elimina una tarea del listado de tareas
        Parametros:
            listado (Listado): Listado del cual eliminar la tarea
            t (Tarea): Tarea a ser eliminada
    """
    listado.remove(t)

def recuperarTarea(listado, i):
    """Retorna la tarea en la posicion i (el indice empieza en 0)"""
    return listado[i]

def tamanio(listado):
    """Retorna la cantidad de tareas en el listado"""
    return len(listado)
