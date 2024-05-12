import tadTarea, tadListado, tadEmpleados, datetime, tadCola
from datetime import date
from tadTarea import *
from tadListado import *
from tadEmpleados import *
from tadCola import *

"""
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
"""


<<<<<<< HEAD
def cargarDatos(listadoTareas, listadoEmpleados):
=======
def cargarDatos(listadoTareas, listadoEmpleados, cola):
>>>>>>> 289ac705231134ad38a3f0b08f48001f092f4489

    listaDatosTareasFicticias = [
    [
        "Revisión de requisitos del cliente",
        "Diseñar y desarrollar la interfaz de usuario del software,\n\t\t\t\tasegurando una experiencia de usuario intuitiva.",
        "María López",
        "Pendiente",
        "2024-05-30",
    ],
    [
        "Diseño de la arquitectura del sistema",
        "Diseñar la arquitectura técnica del sistema, incluyendo la \n\t\t\t\tselección de tecnologías y la definición de la estructura general.",
        "Carlos García",
        "Completada",
        "2024-04-30",
    ],
    [
        "Desarrollo del backend",
        "Programar la lógica del backend del software, incluyendo la \n\t\t\t\tgestión de datos y la implementación de API.",
        "Luis Hernández",
        "En Progreso",
        "2024-05-20",
    ],
    [
        "Desarrollo de la interfaz de usuario",
        "Diseñar y desarrollar la interfaz de usuario del software, \n\t\t\t\tasegurando una experiencia de usuario intuitiva.",
        "María López",
        "Pendiente",
        "2024-05-30",
    ],
    [
        "Pruebas de unidad",
  "Realizar pruebas exhaustivas a nivel de unidad para garantizar el \n\t\t\t\tcorrecto funcionamiento de cada componente del sistema.",
        "Pedro Ramírez",
        "Completada",
        "2024-05-10",
    ],
    [
        "Integración de sistemas",
        "Integrar los diferentes módulos del sistema para asegurar su \n\t\t\t\tfuncionamiento conjunto.",
        "Ana Martínez",
        "En Progreso",
        "2024-05-25",
    ],
    [
        "Pruebas de integración",
        "Realizar pruebas para verificar la integración entre los \n\t\t\t\tdiversos componentes del sistema.",
        "Carlos García",
        "Pendiente",
        "2024-06-05",
    ],
    [
        "Implementación en entorno de producción",
        "Desplegar el software en el entorno de producción del cliente, \n\t\t\t\tasegurando una transición sin problemas.",
        "Luis Hernández",
        "Pendiente",
        "2024-06-15",
    ],
    [
        "Capacitación de usuarios",
        "Realizar sesiones de capacitación para los usuarios finales del \n\t\t\t\tsoftware, garantizando su correcto uso.",
        "María López",
        "Pendiente",
        "2024-06-20",
    ],
    [
        "Soporte post-implementación",
        "Brindar soporte técnico continuo después de la implementación del \n\t\t\t\tsoftware, para resolver cualquier problema que surja.",
        "Pedro Ramírez",
        "Pendiente",
        "2024-06-30",
    ],
    [
        "Auditoría de seguridad",
        "Realizar una auditoría exhaustiva de seguridad en el sistema para \n\t\t\t\tidentificar posibles vulnerabilidades.",
        "Ana Martínez",
        "Pendiente",
        "2024-07-10",
    ],
    [
        "Optimización de rendimiento",
        "Realizar ajustes y optimizaciones en el sistema para mejorar su \n\t\t\t\trendimiento y eficiencia.",
        "Carlos García",
        "Pendiente",
        "2024-07-15",
    ],
    [
        "Actualización de documentación",
        "Actualizar la documentación del sistema, incluyendo manuales de \n\t\t\t\tusuario y guías de instalación.",
        "Luis Hernández",
        "Pendiente",
        "2024-07-20",
    ],
    [
        "Evaluación de retroalimentación del cliente",
        "Recopilar y evaluar la retroalimentación del cliente sobre el \n\t\t\t\tsoftware implementado, para identificar áreas de mejora.",
        "María López",
        "Pendiente",
        "2024-07-25",
    ],
    [
        "Planificación de futuras actualizaciones",
        "Planificar las futuras actualizaciones y mejoras del software en \n\t\t\t\tfunción de las necesidades del cliente y las tendencias del mercado.",
        "Pedro Ramírez",
        "Pendiente",
        "2024-07-30",
    ],
]

    

    for tarea in listaDatosTareasFicticias:
        t = crearTarea()
        n = tarea[0]
        d = tarea[1]
        a = tarea[2]
        e = tarea[3]
        f = tarea[4]
        cargarTarea(t, n, d, a, e, f)
        agregarEmpleado(listadoEmpleados, a)
        agregarTarea(listadoTareas, t)
        if tarea[3] == "En Progreso":
            encolar(cola, tarea)
