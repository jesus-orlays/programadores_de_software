from utils.terminal import limpiar
import backend.producto as Producto
from tabulate import tabulate

headers = ["Id", "Nombre", "Precio", "Cantidad"]

def solicitarProducto():
    nombre = input("Ingrese un nombre: ") 
    ide = input(f"Ingrese el numero de id de {nombre}: ")
    precio = input(f"Ingrese el precio de {nombre}: ")
    cantidad = input(f"Ingrese la cantidad {nombre}: ")

    return (ide, nombre, precio, cantidad)


def listarProductos():
    productos = Producto.listarProductos()

    print(tabulate(productos, headers=headers, tablefmt="rounded_grid"))


def consultarProductos():
    ide = input("ingrese el id del producto: ")
    producto = Producto.consultarProductos(ide)

    if producto == None:
        print(f"producto con documento {ide} no existe")
        
        return
    
    print(tabulate([producto[1:]], headers=headers, tablefmt="rounded_grid"))

def agregarProducto():
    nuevo_producto = solicitarProducto()
    producto_creado = Producto.crearProducto(*nuevo_producto)

    if producto_creado:
        print("producto creado exitosamente. .. ")
    else:
        print("error agregando el producto")

def actualizarProducto():
    nuevo_producto = solicitarProducto()
    producto_actualizado = Producto.actualizarProducto(*nuevo_producto)

    if producto_actualizado:
        print("producto actualizado exitosamente. .. ")
    else:
        print("Error verifique si el producto con ese id existe")

def eliminarProducto():
    ide = input("Ingrese el ide del producto: ")

    producto_eliminado = Producto.eliminarProducto(ide)

    if producto_eliminado:
        print("producto eliminado exitosamente ... ")
    else:
        print("Error: verifique que el producto con ese id si exista")


def mostrarMenuDeProductos():
    bienvenida = "futuros programadores"
    separador = "="*20
    opciones = {
        "1": listarProductos,
        "2": consultarProductos,
        "3": agregarProducto,
        "4": eliminarProducto,
        "5": actualizarProducto,
    }
    solicitud = "Ingrese una opción: "
    salida = False
    
    while True:
        menu = f"{bienvenida if salida == False else separador}\n1. Listar productos\n2. Buscar producto\n3. agregar productos\n4. eliminar productos\n5. actualizar productos\n6. salir"
        print(menu)
        opcion = input(solicitud)
        salida = False
        
        if opcion == "6":
            limpiar()
            break
            
        if opcion in opciones:
            salida = True
            solicitud = "Ingrese una opción: "
            limpiar()
            opciones.get(opcion)()
        else:
            solicitud = "Opción inválida, ingrese una nueva opción: "
            limpiar()
