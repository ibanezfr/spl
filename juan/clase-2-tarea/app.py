#a) especificar el tad producto y el tad supermercado para el manejo de productos
#b) realizar una applicacion que permita cargar todos los productos del supermercado
#c) Aumentarle un 5% el precio de los productos lacreos. Luego imprimir el listado de productos completo
import TadProducto, TadSupermercado
from TadProducto import *
from TadSupermercado import *

def inputProducto():
    """Realiza la carga de un producto y lo devuelve"""
    producto = crearProducto()
    nombre = input("Ingrese el nombre del producto: ")
    marca = input("Ingrese la marca del producto: ")
    tipo = input("Ingrese el tipo de producto: ")
    while True:
        try:
            codigo = int(input("Ingrese el codigo del producto: "))
        except ValueError:
            print("Valor incorrecto, vuelva a intentar")
            continue
        break
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
        except ValueError:
            print("Valor incorrecto, vuelva a intentar")
            continue
        break
    cargarProducto(producto, nombre, marca, tipo, codigo, precio)
    return producto

def imprimirProducto(producto):
    """Realiza la impresion en pantalla de un producto"""
    print("Nombre: " + verNombre(producto))
    print("Marca: " + verMarca(producto))
    print("Tipo: " + verTipo(producto))
    print("Codigo: " + str(verCodigo(producto)))
    print("Precio: " + str(verPrecio(producto)))

supermercado = crearSupermercado()
print("Iniciando carga de productos:")
while True:
    agregarProducto(supermercado, inputProducto())
    leave = input("Desea seguir cargando productos? Y/n ")
    if leave == "n":
        break

for i in range(tamanio(supermercado)):
    producto = recuperarProducto(supermercado, i)
    if (verTipo(producto) == "lacteos"):
        modPrecio(producto, verPrecio(producto) * 1.05)

for i in range(tamanio(supermercado)):
    imprimirProducto(recuperarProducto(supermercado, i))
