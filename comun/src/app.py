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

RO = "\033[91m"
VE = "\033[92m"
AM = "\033[93m"
AZ = "\033[94m"
BB = "\033[1;37m"
R = "\033[0m"

ERROR_STRING = f"\n\t{RO}Valor incorrecto, vuelva a intentar{R}"

def main():
    listadoTareas = crearListado()

    clear()
    imprimir_banner()
    imprimir_menu()
    while True:
        try:
            eleccion = int(input(f"\n\tIngrese su opción {BB}>{R} "))
        except ValueError:
            print(ERROR_STRING)
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
                print(f"\n{AM}Cerrando...{R}\n")
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
    print(f"\n\t{BB}3{R}. Mostrar Listado Completo")
    print(f"\n\t{BB}4{R}. Actualizar Fechas de Vencimiento Por Lote")
    print(f"\n\t{BB}5{R}. Reporte de Tareas Agrupadas por Estado")
    print(f"\n\t{BB}6{R}. Eliminar Tareas de un Empleado {AM}<WIP>{R}")
    print(f"\n\t{BB}7{R}. Imprimir Lista de Tareas del Mes {AM}<WIP>{R}")
    print(f"\n\t{BB}0{R}. Cerrar Aplicación\n")

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def opcionAgregarTarea(listadoTareas):
   
    clear()
    imprimir_banner()

    while True:
        clear()
        imprimir_banner()

        tarea = inputTarea()
        imprimirTarea(tarea)
        cod=input(f"\n\t{AM}¿Los datos son correctos? Y/n >{R} ")
        if cod == "n":
            continue
        break

    agregarTarea(listadoTareas, tarea)

    if len(listaEmpleados) == 0:
        listaEmpleados.append(verAsignado(tarea))
 

def opcionModificarTarea(l):
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
    print(f'\n\t{BB}Nombre:{R} \t\t{verNombre(tarea)}')
    print(f'\t{BB}Descripcion:{R} \t\t{verDescripcion(tarea)}')
    print(f'\t{BB}Empleado Asignado:{R} \t{verAsignado(tarea)}')
    print(f'\t{BB}Estado:{R} \t\t{verEstado(tarea)}')
    print(f'\t{BB}Fecha de vencimiento:{R} \t{verVencimiento(tarea)}\n')

# TODO: extraer listaEmpleados a un TAD
listaEmpleados = []
def seleccionarEmpleado():
    while True:
        print("\n\tIngrese el código correspondiente al empleado a asignar")
        for i, e in enumerate(listaEmpleados):
            print(f'\n\t{i}. {e}')
        print("\t" +  str(len(listaEmpleados)) + ". Nuevo empleado\n")
        try:
            codEmpleado = int(input(f"\t {BB}>{R} "))
        except ValueError:
            print(ERROR_STRING)
            continue
        if codEmpleado < 0 or codEmpleado > len(listaEmpleados):
            print(ERROR_STRING)
            continue
        break
    if codEmpleado == len(listaEmpleados):
        asignado = input("\n\tIngrese el nombre del empleado a quien se le asignará esta tarea: > ")
        listaEmpleados.append(asignado)
    else:
        asignado = listaEmpleados[codEmpleado]
    return asignado

def seleccionarEstado():
    while True:
        try:
            print("\n\tElija el estado de la tarea:")
            print(f"\t\t{BB}1{R}. Pendiente")
            print(f"\t\t{BB}2{R}. En Progreso")
            print(f"\t\t{BB}3{R}. Completada")
            codEstado = int(input("\n\t\t> "))
        except ValueError:
            print(ERROR_STRING)
            continue
        if codEstado < 1 or codEstado > 3:
            print(ERROR_STRING)
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
            strFecha = input("\n\tIngrese la fecha de vencimiento \n\tde la tarea (YYYY-MM-DD) > ")
            anio, mes, dia = map(int, strFecha.split('-'))
            fecha = datetime.date(anio, mes, dia)
        except ValueError:
            print(ERROR_STRING)
            continue
        break
    return strFecha

def inputTarea():
    tarea = crearTarea()
    nombre = input("\n\n\tIngrese el nombre de la tarea \n\t> ")
    descripcion = input("\n\tIngrese la descripción de la tarea \n\t> ")
    if len(listaEmpleados) == 0:
        asignado = input("\n\tIngrese el nombre del empleado\n\ta quien se le asignará esta tarea \n\t> ")
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
