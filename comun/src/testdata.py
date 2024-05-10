import tadTarea, tadListado, tadEmpleados, datetime
from datetime import date
from tadTarea import *
from tadListado import *
from tadEmpleados import *

def cargarDatos(listadoTareas, listadoEmpleados):
    for i in range(1, 16):
        t = crearTarea()
        n = f"Tarea {i}"
        d = f"Descripcion {i}"
        a = f"Empleado {i%3}"
        match i%3:
            case 0:
                e = "Pendiente"
            case 1:
                e = "En Progreso"
            case 2:
                e = "Completada"
        f = datetime.date(i+2000,1+i%12, i).isoformat()
        cargarTarea(t, n, d, a, e, f)
        agregarEmpleado(listadoEmpleados, a)
        agregarTarea(listadoTareas, t)
