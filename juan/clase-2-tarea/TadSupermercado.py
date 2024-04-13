"""
Spec:
    Supermercado:
        List of Producto
"""
def crearSupermercado():
    """Retorna un supermercado vacio"""
    supermercado = []
    return supermercado 

def agregarProducto(supermercado , p):
    """Agrega un producto al supermercado
        Parametros:
            supermercado (Supermercado): Supermercado a quien agregarle el producto
            p (Producto): Producto a agregar
    """
    supermercado.append(p)

def eliminarProducto(supermercado, p):
    """Elimina un producto del supermercado
        Parametros:
            supermercado (Supermercado): Supermercado a quien eliminarle el producto
            p (Producto): Producto a eliminar
    """
    supermercado.remove(p)

def recuperarProducto(supermercado, i):
    """Retorna el producto en la posicion i (el indice empieza en 0)"""
    return supermercado[i]

def tamanio(supermercado):
    """Retorna la cantidad de productos que tiene un supermercado"""
    return len(supermercado)

