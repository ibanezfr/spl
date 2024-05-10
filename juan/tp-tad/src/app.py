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

import tadTarea, tadListado, tadEmpleados, tadCola, datetime, os, sys
from tadTarea import *
from tadListado import *
from tadEmpleados import *
from tadCola import *
from datetime import date
from os import system, name


RO = "\033[91m"
VE = "\033[92m"
AM = "\033[93m"
AZ = "\033[94m"
BB = "\033[1;37m"
R = "\033[0m"

ERROR_STRING = f"\n\t{RO}Valor incorrecto, vuelva a intentar{R}"

def main():
    listadoTareas = crearListado()
    listadoEmpleados = crearEmpleados()

    clear()
    imprimir_banner()
    imprimir_menu()
    while True:
        try:
            eleccion = int(input("\n\tIngrese su opción > "))
        except ValueError:
            print(ERROR_STRING)
            continue

        match eleccion:
           case 1:
                opcionAgregarTarea(listadoTareas, listadoEmpleados)
           case 2:
                opcionModificarTarea(listadoTareas, listadoEmpleados)
           case 3:
                opcionEliminarTarea(listadoTareas)
           case 4:
                opcionMostrarListadoCompleto(listadoTareas)
           case 5:
                opcionActualizarPorLote(listadoTareas)
           case 6:
                opcionReporteTareasPorEstado()
           case 7:
                opcionEliminarTareasEmpleado()
           case 8:
                opcionImprimirTareasDelMes()
           case 0:
                print("\nCerrando programa...")
                sys.exit()
           case _:
                print(ERROR_STRING)
                continue


        clear()
        imprimir_banner()
        imprimir_menu()

def imprimir_banner():
    print("\tGrupo 01 - Sintaxis y Semántica del Lenguaje - 2024")
    print(f"\n\n\t\t\t{BB}*** TIENDA SOFT ***{R}") 

def imprimir_menu():
    print(f"\n\t{BB}1{R}. Agregar Tarea")
    print(f"\n\t{BB}2{R}. Modificar Tarea")
    print(f"\n\t{BB}3{R}. Eliminar Tarea")
    print(f"\n\t{BB}4{R}. Mostrar Listado Completo")
    print(f"\n\t{BB}5{R}. Actualizar Fechas de Vencimiento Por Lote")
    print(f"\n\t{BB}6{R}. Reporte de Tareas Agrupadas por Estado")
    print(f"\n\t{BB}7{R}. Eliminar Tareas de un Empleado {AM}<WIP>{R}")
    print(f"\n\t{BB}8{R}. Imprimir Lista de Tareas del Mes {AM}<WIP>{R}")
    print(f"\n\t{BB}0{R}. Cerrar Aplicación\n")

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def opcionAgregarTarea(listadoTareas, listadoEmpleados):
    while True:
        tarea = inputTarea(listadoEmpleados)
        imprimirTarea(tarea)
        r = input(f"\n\t{AM}¿Los datos son correctos? Y/n >{R} ")
        if r == "n":
            continue
        break

    agregarTarea(listadoTareas, tarea)

    if tamanio(listadoEmpleados) == 0:
        agregarEmpleado(listadoEmpleados, verAsignado(tarea))

def opcionModificarTarea(listadoTareas, listadoEmpleados):
    tarea = seleccionarTarea(listadoTareas)
    tareaTemporal = crearTarea()
    while True:
        print("Ingrese los valores a modificar")
        n = input(f'Nombre (actual: {verNombre(tarea)}): ')
        d = input(f'Descripcion (actual: {verDescripcion(tarea)}): ')
        print(f'Empleado asignado(actual: {verAsignado(tarea)}): ')
        em = seleccionarEmpleado(listadoEmpleados)
        print(f'Estado (actual: {verEstado(tarea)}): ')
        es = seleccionarEstado()
        print(f'Fecha de vencimiento (actual: {verVencimiento(tarea)}): ')
        f = seleccionarFecha()
        cargarTarea(tareaTemporal, n, d, em, es, f)
        imprimirTarea(tareaTemporal)
        r = input("¿Los datos son correctos? Y/n > ")
        if r == "n":
            continue
        break
    asignarTarea(tarea, tareaTemporal)

def opcionEliminarTarea(listadoTareas):
    if tamanio(listadoTareas) == 0:
        print("Actualmente el listado de tareas esta vacio")
        input("")
        return
    tarea = seleccionarTarea(listadoTareas)
    eliminarTarea(listadoTareas, tarea)

def opcionMostrarListadoCompleto(listadoTareas):
    if tamanio(listadoTareas) == 0:
        print("No hay tareas para listar")
        input()
        return
    for i in range(tamanio(listadoTareas)):
        imprimirTarea(recuperarTarea(listadoTareas, i))
    input()

def opcionActualizarPorLote():
    print("Fecha inical:")
    fechaInicial = seleccionarFecha()
    print("Fecha final:")
    fechaFinal = seleccionarFecha()
    print("Fecha nueva:")
    fechaNueva = seleccionarFecha()

def opcionReporteTareasPorEstado():
    print("Hola")

def opcionEliminarTareasEmpleado():
    print("Hola")

def opcionImprimirTareasDelMes():
    print("Hola")

def imprimirTarea(tarea):
    print(f'\n\t{BB}Nombre:{R} \t\t{verNombre(tarea)}')
    print(f'\t{BB}Descripcion:{R} \t\t{verDescripcion(tarea)}')
    print(f'\t{BB}Empleado Asignado:{R} \t{verAsignado(tarea)}')
    print(f'\t{BB}Estado:{R} \t\t{verEstado(tarea)}')
    print(f'\t{BB}Fecha de vencimiento:{R} \t{verVencimiento(tarea)}\n')

def seleccionarTarea(listadoTareas):
    tarea = crearTarea()
    for i in range(tamanio(listadoTareas)):
        tarea = recuperarTarea(listadoTareas, i)
        print(f'{i}. Nombre: {verNombre(tarea)}')
    while True:
        try:
            cod = int(input("Ingrese el codigo de la tarea deseada: "))
        except:
            print(ERROR_STRING)
            continue
        if cod > tamanio(listadoTareas) or cod < 0:
            print(ERROR_STRING)
            continue
        print("Tarea seleccionada:")
        imprimirTarea(recuperarTarea(listadoTareas, i))
        r = input("Es esta la tarea deseada? Y/n")
        if r == 'n':
            continue
        break
    return tarea


def seleccionarEmpleado(listadoEmpleados):
    while True:
        print("Ingrese el codigo correspondiente al empleado a asignar:")
        for i in range(tamanio(listadoEmpleados)):
            print(f'{i}. {recuperarEmpleado(listadoEmpleados, i)}')
        print(str(tamanio(listadoEmpleados)) + ". Nuevo empleado")
        try:
            codEmpleado = int(input())
        except ValueError:
            print(ERROR_STRING)
            continue
        if codEmpleado < 0 or codEmpleado > tamanio(listadoEmpleados):
            print(ERROR_STRING)
            continue
        break
    if codEmpleado == tamanio(listadoEmpleados):
        asignado = input("Ingrese el nombre del empleado a quien se le asignara esta tarea: ")
        agregarEmpleado(listadoEmpleados, asignado)
    else:
        asignado = recuperarEmpleado(listadoEmpleados, codEmpleado)
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
            #anio, mes, dia = map(int, strFecha.split('-'))
            #fecha = datetime.date(anio, mes, dia)
            fecha = date.fromisoformat(strFecha)
        except ValueError:
            print(ERROR_STRING)
            continue
        break
    return strFecha

def inputTarea(listadoEmpleados):
    tarea = crearTarea()
    nombre = input("Ingrese el nombre de la tarea: ")
    descripcion = input("Ingrese la descripcion de la tarea: ")
    if tamanio(listadoEmpleados) == 0:
        asignado = input("Ingrese el nombre del empleado a quien se le asignara esta tarea: ")
    else:
        asignado = seleccionarEmpleado(listadoEmpleados)
    estado = seleccionarEstado()
    vencimiento = seleccionarFecha()
    cargarTarea(tarea, nombre, descripcion, asignado, estado, vencimiento)
    #if estado == "En progreso":
        #Encolar
    return tarea


if __name__ == "__main__":
    main()
