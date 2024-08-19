# main.py

from inventario import Inventario
from producto import Producto


def mostrar_menu():
    print("\nMenú de Gestión de Inventario")
    print("1. Añadir nuevo producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto(s) por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")


def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == '1':
            id = input("Ingrese ID del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad: "))
            precio = float(input("Ingrese precio: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == '2':
            id = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == '3':
            id = input("Ingrese ID del producto a actualizar: ")
            cantidad = input("Ingrese nueva cantidad (deje en blanco si no desea cambiarla): ")
            precio = input("Ingrese nuevo precio (deje en blanco si no desea cambiarlo): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == '4':
            nombre = input("Ingrese nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == '5':
            inventario.mostrar_todos_productos()

        elif opcion == '6':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida, por favor elija nuevamente.")


if __name__ == "__main__":
    main()
    