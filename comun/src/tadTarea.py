#Spec:
#   tarea:
#       nombre: string
#       descripcion: string
#       asignado: string (nombre de empleado)
#       estado: string o tadEstado (pendiente, en progreso, completada)
#       fecha de vencimiento: datetime
from datetime import date

def crearTarea():
    """Retorna una tarea vacia"""
    return ["", "", "", "", 0]

def cargarTarea(tarea, nombre, descripcion, asignado, estado, vencimiento):
    """Carga los valores de una tarea
        Parametros:
            tarea (Tarea): tarea a cargar
            nombre (str): nombre de la tarea
            descripcion (str): descripcion de la tarea
            asignado (str): nombre del empleado a quien se le asigna la tarea
            estado (str): estado de la tarea, valores validos: pendiente, en progreso, completado
            vencimiento (str): fecha de vencimiento de la tarea, formato ISO 8601 (YYYY-MM-DD)
    """
    tarea[0] = nombre
    tarea[1] = descripcion
    tarea[2] = asignado
    tarea[3] = estado
    tarea[4] = date.fromisoformat(vencimiento)

def verNombre(tarea):
    """Retorna el nombre de la tarea"""
    return tarea[0]

def verDescripcion(tarea):
    """Retorna la descripcion de la tarea"""
    return tarea[1]

def verAsignado(tarea):
    """Retorna el nombre del empleado que tiene asignada la tarea"""
    return tarea[2]

def verEstado(tarea):
    """Retorna el estado de la tarea"""
    return tarea[3]

def verVencimiento(tarea):
    """Retorna la fecha de vencimiento de la tarea en formato ISO 8061"""
    return date.isoformat(tarea[4])

def modNombre(tarea, nombre):
    """Modifica el nombre de la tarea"""
    tarea[0] = nombre

def modDescripcion(tarea, descripcion):
    """Modifica la descripcion de la tarea"""
    tarea[1] = descripcion

def modAsignado(tarea, asignado):
    """Modifica el empleado que tiene asignada la tarea"""
    tarea[2] = asignado

def modEstado(tarea, estado):
    """Modifica el estado de la tarea"""
    tarea[3] = estado

def modVencimiento(tarea, vencimiento):
    """Modifica la fecha de vencimiento de la tarea"""
    tarea[4] = date.fromisoformat(vencimiento)

def asignarTarea(tareaDestino, tareaFuente):
    """Asigna el valor de la tarea fuente a la tarea destino"""
    modNombre(tareaDestino, verNombre(tareaFuente))
    modDescripcion(tareaDestino, verDescripcion(tareaFuente))
    modAsignado(tareaDestino, verAsignado(tareaFuente))
    modEstado(tareaDestino, verEstado(tareaFuente))
    modVencimiento(tareaDestino, verVencimiento(tareaFuente))

