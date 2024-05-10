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
            eleccion = int(input(f"\n\tIngrese su opción {BB}>{R} "))
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
                opcionReporteTareasPorEstado(listadoTareas)
           case 7:
                opcionEliminarTareasEmpleado()
           case 8:
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
        clear()
        imprimir_banner()

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


def opcionEliminarTarea():
    if tamanio(listadoTareas) == 0:
        input(f"\n\t{AM}Lista de tareas VACIA, Enter para continuar...{R}");
        return
    tarea = seleccionarTarea(listadoTareas)
    eliminarTarea(listadoTareas, tarea)

def opcionMostrarListadoCompleto(listadoTareas):

    totTareas = tamanio(listadoTareas)
    tareasEnPantalla = 3

    if totTareas == 0:
        input(f"\n\t{AM}Lista de tareas VACIA, Enter para continuar...{R}");
    else:
        for i in range(0, totTareas, tareasEnPantalla):
            for j in range(tareasEnPantalla):
                tareaActual = i + j
                if tareaActual < totTareas:
                    imprimirTarea(recuperarTarea(listadoTareas, i + j))
            restantes = totTareas - (i + tareasEnPantalla)
            if restantes > 0:
                input(f"\n\t{AM}(Restan {restantes} tareas, Enter para continuar...{R}")
            else:
                input(f"\n\t{AM}Enter para terminar...{R}")
                      
#TODO
def opcionActualizarPorLote():
    print("Fecha inical:")
    fechaInicial = seleccionarFecha()
    print("Fecha final:")
    fechaFinal = seleccionarFecha()
    print("Fecha nueva:")
    fechaNueva = seleccionarFecha()

def opcionReporteTareasPorEstado(listadoTareas):
    estados = ["Pendiente", "En Progreso", "Completada"]
    totTareas = tamanio(listadoTareas)
    tareasEnPantalla = 3

    if totTareas == 0:
        input(f"\n\t{AM}Lista de tareas VACIA, Enter para continuar...{R}");
    else:
        for i in estados:
            print(f"\n\tSección: {i}")
            print(f"\t{AZ}********************{R}")
            ctr = imprimirTareasFiltrado(listadoTareas, totTareas,
                                         tareasEnPantalla, i)
            if ctr == 0:
                print(f"\n\tNo hay Tareas en estado {AM}{i}{R}")
        input(f"\n\t{AM}Enter para terminar...{R}")
        

def imprimirTareasFiltrado(listadoTareas, totTareas, tareasEnPantalla, estado):
    ctr = 0
    #input(f"\n\t{AM}Lista de tareas VACIA, Enter para continuar...{R}");
    for i in range(0, totTareas, tareasEnPantalla):
        for j in range(tareasEnPantalla):
            tareaActual = i + j
            if tareaActual < totTareas:
                rta = recuperarTarea(listadoTareas, i + j)
                if verEstado(rta) == estado:
                    imprimirTarea(recuperarTarea(listadoTareas, i + j))
                    ctr = ctr + 1
        restantes = totTareas - (i + tareasEnPantalla)
        if restantes > 0:
            input(f"\n\t{AM}(Restan {restantes} tareas, Enter para continuar...{R}")
        #else:
        #    input(f"\n\t{AM}Enter para terminar...{R}")
    return ctr


#TODO
def opcionEliminarTareasEmpleado():
    print("Hola")

#TODO
def opcionImprimirTareasDelMes():
    print("Hola")

def imprimirTarea(tarea):
    print(f'\n\t{BB}Nombre:{R} \t\t{verNombre(tarea)}')
    print(f'\t{BB}Descripcion:{R} \t\t{verDescripcion(tarea)}')
    print(f'\t{BB}Empleado Asignado:{R} \t{verAsignado(tarea)}')
    print(f'\t{BB}Estado:{R} \t\t{verEstado(tarea)}')
    print(f'\t{BB}Fecha de vencimiento:{R} \t{verVencimiento(tarea)}\n')

def seleccionarEmpleado(listadoEmpleados):
    while True:
        print("\n\tIngrese el código correspondiente al empleado a asignar")
        for i in range(tamanio(listadoEmpleados)):
            print(f'{i}. {recuperarEmpleado(listadoEmpleados, i)}')
        print(str(tamanio(listadoEmpleados)) + ". Nuevo empleado")
        try:
            codEmpleado = int(input(f"\t {BB}>{R} "))
        except ValueError:
            print(ERROR_STRING)
            continue
        if codEmpleado < 0 or codEmpleado > tamanio(listadoEmpleados):
            print(ERROR_STRING)
            continue
        break
    if codEmpleado == tamanio(listadoEmpleados):
        asignado = input("\n\tIngrese el nombre del empleado a quien se le asignará esta tarea: > ")
        agregarEmpleado(listadoEmpleados, asignado)
    else:
        asignado = recuperarEmpleado(listadoEmpleados, codEmpleado)
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
    match codEstado:
        case 1:
            return "Pendiente"
        case 2:
            return "En progreso"
        case 3:
            return "Completada"
        case _:
            print(ERROR_STRING)
            #continue
            #TODO SyntaxError: 'continue' not properly in loop

def seleccionarFecha():
    while True:
        try:
            strFecha = input("\n\tIngrese la fecha de vencimiento \n\tde la tarea (YYYY-MM-DD) > ")
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
    nombre = input("\n\n\tIngrese el nombre de la tarea \n\t> ")
    descripcion = input("\n\tIngrese la descripción de la tarea \n\t> ")
    if tamanio(listadoEmpleados) == 0:
        asignado = input("\n\tIngrese el nombre del empleado\n\ta quien se le asignará esta tarea \n\t> ")
    else:
        asignado = seleccionarEmpleado(listadoEmpleados)
    estado = seleccionarEstado()
    vencimiento = seleccionarFecha()
    cargarTarea(tarea, nombre, descripcion, asignado, estado, vencimiento)
    #if estado == "En progreso":
        #Encolar
    return tarea


if __name__ == '__main__':
    main()
