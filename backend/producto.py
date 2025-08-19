from backend.hoja_producto import obtenerHojaDeProductos
from backend.excel import guardarHoja

hoja = obtenerHojaDeProductos()

def listarProductos():
    filas = []

    refFilas = hoja.iter_rows(min_row=2, max_row=hoja.max_row, min_col=1, max_col=4)

    for refFila in refFilas:
        valores = []

        for celda in refFila:
            valores.append(celda.value)

        filas.append(valores)

    return filas

def consultarProductos(id, soloValores = True):
    refFilas = hoja.iter_rows(min_row=2, max_row=hoja.max_row, min_col=1, max_col=4)
    refFilasEnum = enumerate(refFilas)

    for idx, refFila in refFilasEnum:
        if refFila[0].value == id:
            if soloValores:
             valores = []
             valores.append(idx)

             for celda in refFila:
                 valores.append(celda.value)
             return valores
            else:
             return refFila
    else:
        return None


def crearProducto(id, nombre, precio, cantidad):
    if consultarProductos(id) != None:
        return False
    producto = (id, nombre, precio, cantidad)

    hoja.append(producto)

    guardarHoja(hoja)

    return True

def eliminarProducto(id):
    producto = consultarProductos(id)

    if producto == None:
        return False

    hoja.delete_rows(producto[0]+2)

    guardarHoja(hoja)

    return True

def actualizarProducto(id, nombre, precio, cantidad): 
    nuevos_valores = (id, nombre, precio, cantidad)

    refFila = consultarProductos(id, False)

    if refFila == None:
        return False
    
    for celda, nuevo_valor in zip(refFila, nuevos_valores):
        celda.value = nuevo_valor

    guardarHoja(hoja)

    return True




