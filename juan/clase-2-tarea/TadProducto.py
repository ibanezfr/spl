#Spec:
# Producto {
#   nombre: string
#   marca: string
#   tipo: string
#   precio: float
#   codigo: int
#}


def crearProducto():
    """Retorna un producto vacio"""
    return ["", "", "", 0, 0]

def cargarProducto(producto, nombre, marca, tipo, codigo, precio):
    """Carga los valores de un producto
        Parametros:
            producto (Producto): producto a cargar
            nombre (str): Nombre del producto
            marca (str): Marca del producto
            tipo (str): Tipo de producto (ej: lacteos, enlatados)
            codigo (int): Codigo numerico del producto
            precio (float): Precio del producto
    """
    producto[0] = nombre
    producto[1] = marca
    producto[2] = tipo
    producto[3] = codigo
    producto[4] = precio

def verNombre(producto):
    """Retorna el nombre del producto"""
    return producto[0]

def verMarca(producto):
    """Retorna la marca del producto"""
    return producto[1]

def verTipo(producto):
    """Retorna el tipo del producto"""
    return producto[2]

def verCodigo(producto):
    """Retorna el codigo del producto"""
    return producto[3]

def verPrecio(producto):
    """Retorna el precio del producto"""
    return producto[4]

def modNombre(producto, nombre):
    """Modifica el nombre del producto"""
    producto[0] = nombre

def modMarca(producto, marca):
    """Modifica la marca del producto"""
    producto[1] = marca

def modTipo(producto, tipo):
    """Modifica el tipo del producto"""
    producto[2] = tipo

def modCodigo(producto, codigo):
    """Modifica el codigo del producto"""
    producto[3] = codigo

def modPrecio(producto, precio):
    """Modifica el precio del producto"""
    producto[4] = precio

def asignarProducto(producto1, producto2):
    """Asigna el valor de un producto a otro
        Parametros:
            producto1: Producto a quien se le asignaran los nuevos valores
            producto2: Producto a copiar
    """
    producto1[0] = producto2[0]
    producto1[1] = producto2[1]
    producto1[2] = producto2[2]
    producto1[3] = producto2[3]
    producto1[4] = producto2[4]
