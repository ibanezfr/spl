""" Spec Menu:
    - Agregar Tarea franco
    - Modificar Tarea juan
    - Eliminar Tarea juan
    - Mostrar Listado Completo juan
    - Modificar fecha de vecimiento (entre Fecha1 y Fecha2 -> cambia a FechaFinal) juan
    - Reporte de tareas agrupadas por estado franco
    - Eliminar todas las tareas asignadas a un empleado especifico franco
    - Mostrar cola de tareas del mes franco
"""

import tadTarea, tadListado, tadCola, datetime
from tadTarea import *
from tadListado import *
from tadCola import *
from datetime import date

ERROR_STRING = "Valor incorrecto, vuelva a intentar"

def imprimirTarea(tarea):
    print(f'Nombre: {verNombre(tarea)}')
    print(f'Descripcion: {verDescripcion(tarea)}')
    print(f'Empleado Asignado: {verAsignado(tarea)}')
    print(f'Estado: {verEstado(tarea)}')
    print(f'Fecha de vencimiento: {verVencimiento(tarea)}')

def seleccionarTarea(listadoTareas):
    for i, e in enumerate(listadoTareas):
        print(f'{i}. Nombre: {verNombre(e)}')
    while True:
        try:
            cod = int(input("Ingrese el codigo de la tarea deseada: "))
        except:
            print(ERROR_STRING)
            continue
        if cod > tamanio(listado) or cod < 0:
            print(ERROR_STRING)
            continue
        print("Tarea seleccionada:")
        imprimirTarea(e)
        r = input("Es esta la tarea deseada? Y/n")
        if r == 'n':
            continue
        break
    return e


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
            print(ERROR_STRING)
            continue
        if codEmpleado < 0 or codEmpleado > len(listaEmpleados):
            print(ERROR_STRING)
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
            print(ERROR_STRING)
            continue
        match codEstado:
            case 1:
                return "Pendiente"
            case 2:
                return "En progreso"
            case 3:
                return "Completada"
            case _:
                print(ERROR_STRING)
                continue

def seleccionarFecha():
    while True:
        try:
            strFecha = input("Ingrese la fecha de vencimiento de la tarea (YYYY-MM-DD)")
            anio, mes, dia = map(int, strFecha.split('-'))
            fecha = datetime.date(anio, mes, dia)
        except ValueError:
            print(ERROR_STRING)
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
