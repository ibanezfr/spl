"""
Archivo:        /comun/src/app.py
Fecha:          5 de mayo de 2024
Modificación:   
Autores:        Piazza J., Ibañez F., Lucas M.


Spec Menu:
    - Agregar Tarea
    - Modificar Tarea
    - Eliminar Tarea
    - Mostrar Listado Completo
    - Modificar fecha de vecimiento (entre Fecha1 y Fecha2 -> cambia a FechaFinal)
    - Reporte de tareas agrupadas por estado
    - Eliminar todas las tareas asignadas a un empleado especifico
    - Mostrar cola de tareas del mes

"""

import tadTarea, tadListado, tadCola, datetime
from tadTarea import *
from tadListado import *
from tadCola import *
from datetime import date


def imprimirTarea(tarea):
    print(f'Nombre: {verNombre(tarea)}')
    print(f'Descripcion: {verDescripcion(tarea)}')
    print(f'Empleado Asignado: {verAsignado(tarea)}')
    print(f'Estado: {verEstado(tarea)}')
    print(f'Fecha de vencimiento: {verVencimiento(tarea)}')

# TODO: extraer listaEmpleados a un TAD
listaEmpleados = []
def seleccionarEmpleado():
    while True:
        print("Ingrese el codigo correspondiente al empleado a asignar:")
        for i, e in enumerate(listaEmpleados):
            print(f'{i}. {e}')
        print(str(len(listaEmpleados)) + ". Nuevo empleado")
        try:
            codEmpleado = int(input())
        except ValueError:
            print("Valor incorrecto, vuelva a intentar")
            continue
        if codEmpleado < 0 or codEmpleado > len(listaEmpleados):
            print("Valor incorrecto, vuelva a intentar")
            continue
        break
    if codEmpleado == len(listaEmpleados):
        asignado = input("Ingrese el nombre del empleado a quien se le asignara esta tarea: ")
        listaEmpleados.append(asignado)
    else:
        asignado = listaEmpleados[codEmpleado]
    return asignado

def seleccionarEstado():
    while True:
        try:
            print("Elija el estado de la tarea:")
            print("1. Pendiente")
            print("2. En Progreso")
            print("3. Completada")
            codEstado = int(input())
        except ValueError:
            print("Valor incorrecto, vuelva a intentar")
            continue
        if codEstado < 1 or codEstado > 3:
            print("Valor incorrecto, vuelva a intentar")
            continue
        break
    match(codEstado):
        case 1:
            return "Pendiente"
        case 2:
            return "En progreso"
        case 3:
            return "Completada"

def seleccionarFecha():
    while True:
        try:
            strFecha = input("Ingrese la fecha de vencimiento de la tarea (YYYY-MM-DD)")
            anio, mes, dia = map(int, strFecha.split('-'))
            fecha = datetime.date(anio, mes, dia)
        except ValueError:
            print("Valor incorrecto, vuelva a intentar")
            continue
        break
    return strFecha

def inputTarea():
    tarea = crearTarea()
    nombre = input("Ingrese el nombre de la tarea: ")
    descripcion = input("Ingrese la descripcion de la tarea: ")
    if len(listaEmpleados) == 0:
        asignado = input("Ingrese el nombre del empleado a quien se le asignara esta tarea: ")
        listaEmpleados.append(asignado)
    else:
        asignado = seleccionarEmpleado()
    estado = seleccionarEstado()
    vencimiento = seleccionarFecha()
    cargarTarea(tarea, nombre, descripcion, asignado, estado, vencimiento)
    #if estado == "En progreso":
        #Encolar
    return tarea

