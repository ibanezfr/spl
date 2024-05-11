""" Archivo:        /comun/src/app.py 
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
        - Mostrar cola de tareas en progreso 
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

import testdata
from testdata import *

RO = "\033[91m" #Rojo
VE = "\033[92m" #Verde
AM = "\033[93m" #Amarillo
AZ = "\033[94m" #Azul
BB = "\033[1;37m" #Bold Blanco ("Negrita")
R = "\033[0m" #Reset

ERROR_VALUE_STRING = f"\n\t{RO}Valor incorrecto, vuelva a intentar{R}"
ERROR_EMPTY_STRING = f"\n\t{AM}Lista de tareas VACIA, Enter para continuar...{R}"
ERROR_LOADED_STRING = f"\n\t{RO}Datos de prueba ya cargados, Enter para continuar...{R}"
CONTINUE_STRING = f"\n\t{AM}Enter para terminar...{R}"
CONTINUE_STRING_2 = f"\n\t{AM}Enter para continuar...{R}"
DATOS_CARGADOS = False

def main():
    global DATOS_CARGADOS
    listadoTareas = crearListado()
    listadoEmpleados = crearEmpleados()
    colaTareasEnProgreso = crearCola()

    clear()
    imprimir_banner()
    imprimir_menu()
    while True:
        try:
            e = input(f"\n\tIngrese su opción {BB}>{R} ")
            eleccion = int(e)
        except ValueError:
            print(ERROR_VALUE_STRING)
            continue
        if len(e) > 1:
            print(ERROR_VALUE_STRING)
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
           case 9:
                if not DATOS_CARGADOS:
                    DATOS_CARGADOS = opcionCargarDatos(listadoTareas, listadoEmpleados)
                else:
                    input(ERROR_LOADED_STRING)
           case 0:
                print(f"\n{AM}Cerrando...{R}\n")
                sys.exit()
           case _:
                print(ERROR_VALUE_STRING)
                continue

        clear()
        imprimir_banner()
        imprimir_menu()
        
### Funciones auxiliares para menu ###
def imprimir_banner():
    print("\tGrupo 01 - Sintaxis y Semántica del Lenguaje - 2024")
    print(f"\t\t\t{BB}*** TIENDA SOFT ***{R}") 


def imprimir_menu():
    print(f"\n\t{BB}1{R}. Agregar Tarea")
    print(f"\n\t{BB}2{R}. Modificar Tarea")
    print(f"\n\t{BB}3{R}. Eliminar Tarea")
    print(f"\n\t{BB}4{R}. Mostrar Listado Completo")
    print(f"\n\t{BB}5{R}. Actualizar Fechas de Vencimiento Por Lote")
    print(f"\n\t{BB}6{R}. Reporte de Tareas Agrupadas por Estado")
    print(f"\n\t{BB}7{R}. Eliminar Tareas de un Empleado {AM}<WIP>{R}")
    print(f"\n\t{BB}8{R}. Imprimir Cola de Tareas En Progreso {AM}<WIP>{R}")
    if not DATOS_CARGADOS: 
        print(f"\n\t{BB}9{R}. Cargar Datos de Prueba")
    else:
        print(f"\n\t{VE}9. Cargar Datos de Prueba {R}")
    print(f"\n\t{BB}0{R}. Cerrar Aplicación\n")

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

### Funciones del menu ###

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
    if tamanio(listadoTareas) == 0:
        input(ERROR_EMPTY_STRING)
        return
    tarea = seleccionarTarea(listadoTareas)
    tareaTemporal = crearTarea()
    while True:
        print("\n\tIngrese los valores a modificar")
        nombre = input(f'\t{BB}Nombre{R} (actual: {verNombre(tarea)}): ')
        descripcion = input(f'\t{BB}Descripcion{R} (actual: {verDescripcion(tarea)}): ')
        print(f'\t{BB}Empleado asignado{R} (actual: {verAsignado(tarea)}): ')
        asignado = seleccionarEmpleado(listadoEmpleados)
        print(f'\t{BB}Estado{R} (actual: {verEstado(tarea)}): ')
        estado = seleccionarEstado()
        d = date.fromisoformat(verVencimiento(tarea))
        print(f'\t{BB}Fecha de vencimiento{R} (actual: {d.day}-{d.month}-{d.year}): ')
        vencimiento = seleccionarFecha()
        cargarTarea(tareaTemporal, nombre, descripcion, asignado, estado, vencimiento)
        imprimirTarea(tareaTemporal)
        r = input(f"\n\t{AM}¿Los datos son correctos? Y/n >{R} ")
        if r == "n":
            continue
        break
    asignarTarea(tarea, tareaTemporal)


def opcionEliminarTarea(listadoTareas):
    if tamanio(listadoTareas) == 0:
        input(ERROR_EMPTY_STRING)
        return
    tarea = seleccionarTarea(listadoTareas)
    eliminarTarea(listadoTareas, tarea)


def opcionMostrarListadoCompleto(listadoTareas):
    totTareas = tamanio(listadoTareas)
    tareasEnPantalla = 3

    if totTareas == 0:
        input(ERROR_EMPTY_STRING)
        return
    
    for i in range(0, totTareas, tareasEnPantalla):
        clear()
        imprimir_banner()
        print(f"\n\t{BB}Listado Completo{R}")
        print(f"\t{AZ}****************{R}")

        for j in range(tareasEnPantalla):
            tareaActual = i + j
            if tareaActual < totTareas:
                imprimirTarea(recuperarTarea(listadoTareas, i + j))
        restantes = totTareas - (i + tareasEnPantalla)
        if restantes > 0:
            input(f"\n\t{AM}Restan {restantes} tarea/s, Enter para continuar...{R}")
        else:
            input(CONTINUE_STRING)
                      
def opcionActualizarPorLote(listadoTareas):
    if tamanio(listadoTareas) == 0:
        input(ERROR_EMPTY_STRING)
        return

    print("\n\tFecha inical:")
    fechaInicial = date.fromisoformat(seleccionarFecha())
    print("\tFecha final:")
    fechaFinal = date.fromisoformat(seleccionarFecha())
    print("\tFecha nueva:")
    fechaNueva = seleccionarFecha()
    mod = 0
    for i in range(tamanio(listadoTareas)):
        t = recuperarTarea(listadoTareas, i)
        d = date.fromisoformat(verVencimiento(t))
        if d >= fechaInicial and d <= fechaFinal:
            modVencimiento(t, fechaNueva)
            mod += 1
    print(f'Se modificaron {mod} tarea/s')
    input(CONTINUE_STRING)

def opcionReporteTareasPorEstado(listadoTareas):
    listadoPendiente = crearListado()
    listadoProgreso = crearListado()
    listadoCompleto = crearListado()
    for i in range(tamanio(listadoTareas)):
        t = recuperarTarea(listadoTareas, i)
        match verEstado(t):
            case "Pendiente":
                agregarTarea(listadoPendiente, t)
            case "En Progreso":
                agregarTarea(listadoProgreso, t)
            case "Completada":
                agregarTarea(listadoCompleto, t)

    imprimirSeccion(listadoPendiente, 3, "Pendiente")
    imprimirSeccion(listadoProgreso, 3, "En Progreso")
    imprimirSeccion(listadoCompleto, 3, "Completada")

#TODO
def opcionEliminarTareasEmpleado():
    print(f"\n\t{RO}Función no implementada <WIP>{R}")
    input(CONTINUE_STRING)

#TODO
def opcionImprimirTareasDelMes():
    print(f"\n\t{RO}Función no implementada <WIP>{R}")
    input(CONTINUE_STRING)

def opcionCargarDatos(listaTareas, listadoEmpleados):
    cargarDatos(listaTareas, listadoEmpleados)
    return True

def imprimirSeccion(listado, tareasEnPantalla, estado):
    totTareas = tamanio(listado)
    for i in range(0, totTareas, tareasEnPantalla):
        clear()
        imprimir_banner()
        print(f"\n\tSección: {estado}")
        print(f"\t{AZ}********************{R}")
        for j in range(tareasEnPantalla):
            tareaActual = i + j
            if tareaActual < totTareas:
                imprimirTarea(recuperarTarea(listado, i + j))
        restantes = totTareas - (i + tareasEnPantalla)
        if restantes > 0:
            input(f"\n\t{AM}Restan {restantes} tarea/s, Enter para continuar...{R}")
        else:
            input(CONTINUE_STRING_2)

def imprimirTarea(tarea):
    print(f'\n\t{BB}Nombre:{R} \t\t{verNombre(tarea)}')
    print(f'\t{BB}Descripcion:{R} \t\t{verDescripcion(tarea)}')
    print(f'\t{BB}Empleado Asignado:{R} \t{verAsignado(tarea)}')
    print(f'\t{BB}Estado:{R} \t\t{verEstado(tarea)}')
    f = date.fromisoformat(verVencimiento(tarea))
    print(f'\t{BB}Fecha de vencimiento:{R} \t{f.day}-{f.month}-{f.year}')

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
    #if estado == "En Progreso":
        #Encolar
    return tarea

### Funciones auxiliares ###
def seleccionarTarea(listadoTareas):
    tarea = crearTarea()
    for i in range(tamanio(listadoTareas)):
        print(f'{i}. Nombre: {verNombre(recuperarTarea(listadoTareas, i))}')
    while True:
        try:
            cod = int(input("Ingrese el codigo de la tarea deseada: "))
        except:
            print(ERROR_VALUE_STRING)
            continue
        if cod >= tamanio(listadoTareas) or cod < 0:
            print(ERROR_VALUE_STRING)
            continue
        print("Tarea seleccionada:")
        tarea = recuperarTarea(listadoTareas, cod)
        imprimirTarea(tarea)
        r = input("Es esta la tarea deseada? Y/n")
        if r == 'n':
            continue
        break
    return tarea

def seleccionarEmpleado(listadoEmpleados):
    while True:
        print("\n\tIngrese el código correspondiente al empleado a asignar")
        for i in range(tamanio(listadoEmpleados)):
            print(f'{i}. {recuperarEmpleado(listadoEmpleados, i)}')
        print(f'{str(tamanio(listadoEmpleados))}. Nuevo empleado')
        try:
            codEmpleado = int(input(f"\t {BB}>{R} "))
        except ValueError:
            print(ERROR_VALUE_STRING)
            continue
        if codEmpleado < 0 or codEmpleado > tamanio(listadoEmpleados):
            print(ERROR_VALUE_STRING)
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
            print(ERROR_VALUE_STRING)
            continue
        match codEstado:
            case 1:
                return "Pendiente"
            case 2:
                return "En Progreso"
            case 3:
                return "Completada"
            case _:
                print(ERROR_VALUE_STRING)
                continue

def seleccionarFecha():
    while True:
        try:
            strFecha = input("\n\tIngrese la fecha de vencimiento (DD-MM-AAAA) > ")
            dia, mes, anio = map(int, strFecha.split('-'))
            fecha = datetime.date(anio, mes, dia)
        except ValueError:
            print(ERROR_VALUE_STRING)
            continue
        break
    return fecha.isoformat()

if __name__ == '__main__':
    main()
