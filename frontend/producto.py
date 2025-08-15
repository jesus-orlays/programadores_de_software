from utils.terminal import limpiar
import backend.producto as Producto
from tabulate import tabulate

headers = ["Id", "Nombre", "Precio", "Cantidad"]

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
def mostrarMenuDeClientes():
    bienvenida = "futuros programadores"
    separador = "="*20
    opciones = {
        "1": listarProductos,
        "2": consultarProductos,
    }
    solicitud = "Ingrese una opción: "
    salida = False
    
    while True:
        menu = f"{bienvenida if salida == False else separador}\n1. Listar clientes\n2. Buscar cliente\n3. Salir"
        print(menu)
        opcion = input(solicitud)
        salida = False
        
        if opcion == "3":
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
