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
    
    Preguntas:
    Cortar las fechas? Fecha mínima?
"""

import tadTarea, tadListado, tadCola, datetime, os, sys
from tadTarea import *
from tadListado import *
from tadCola import *
from datetime import date
from os import system, name

def main():
    listadoTareas = crearListado()


    imprimir_menu()
    while True:
        try:
            eleccion = int(input("\n\tIngrese su opción > "))
        except ValueError:
            print("Valor incorrecto, vuelva a intentar")
            continue

        match eleccion:
           case 1:
                opcionAgregarTarea(listadoTareas)
           case 2:
                opcionModificarTarea(listadoTareas)
           case 3:
                opcionMostrarListadoCompleto()
           case 4:
                opcionActualizarPorLote()
           case 5:
                opcionReporteTareasPorEstado()
           case 6:
                opcionEliminarTareasEmpleado()
           case 7:
                opcionImprimirTareasDelMes()
           case 0:
                print("\nCerrando programa...")
                sys.exit()
           case _:
                print("Valor incorrecto, vuelva a intentar")
                continue

        imprimir_menu()
        

def imprimir_menu():
    clear()
    print("\tGrupo 01 - Sintaxis y Semántica del Lenguaje - 2024")
    print("\n\n\t\t\t*** Tienda Soft ***") 
    print("\n\t1. Agregar Tarea")
    print("\t2. Modificar Tarea")
    print("\t3. Mostrar Listado Completo")
    print("\t4. Actualizar Fechas de Vencimiento Por Lote")
    print("\t5. Reporte de Tareas Agrupadas por Estado")
    print("\t6. Eliminar Tareas de un Empleado")
    print("\t7. Imprimir Lista de Tareas del Mes")


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def opcionAgregarTarea(listadoTareas):
   
    while True:
        tarea = inputTarea()
        imprimirTarea(tarea)
        cod=input("¿Los datos son correctos? Y/n > ")
        if cod == "n":
            continue
        break

    agregarTarea(listadoTareas, tarea)

    if len(listaEmpleados) == 0:
        listaEmpleados.append(verAsignado(tarea))
 

def opcionModificarTarea():
    print("Hola")

def opcionMostrarListadoCompleto():
    print("Hola")

def opcionActualizarPorLote():
    print("Hola")

def opcionReporteTareasPorEstado():
    print("Hola")

def opcionEliminarTareasEmpleado():
    print("Hola")

def opcionImprimirTareasDelMes():
    print("Hola")


    

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
    nombre = input("\n\tIngrese el nombre de la tarea: ")
    descripcion = input("Ingrese la descripcion de la tarea: ")
    if len(listaEmpleados) == 0:
        asignado = input("Ingrese el nombre del empleado a quien se le asignara esta tarea: ")
        #listaEmpleados.append(asignado)
    else:
        asignado = seleccionarEmpleado()
    estado = seleccionarEstado()
    vencimiento = seleccionarFecha()
    cargarTarea(tarea, nombre, descripcion, asignado, estado, vencimiento)
    #if estado == "En progreso":
        #Encolar
    return tarea


if __name__ == '__main__':
    main()
