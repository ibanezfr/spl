"""
Spec:
    Listado:
        List of string
"""


def crearEmpleados():
    """Retorna un listado de empleados vacio"""
    empleados = []
    return empleados


def agregarEmpleado(empleados, e):
    """Agrega un empleado al listado de empleados
        Parametros:
            empleados (Empleados): Listado al cual agregarle el empleado
            e (str): Empleado a ser agregado
    """
    empleados.append(e)


def eliminarEmpleado(empleados, e):
    """Elimina un empleado del listado de empleados
        Parametros:
            empleados (Empleados): Listado del cual eliminar el empleado
            e (str): Empleado a ser eliminado
    """
    empleados.remove(e)


def recuperarEmpleado(empleados, i):
    """Retorna el empleado en la posicion i (el indice empieza en 0)"""
    return empleados[i]


def tamanio(empleados):
    """Retorna la cantidad de empleados en el listado"""
    return len(empleados)
