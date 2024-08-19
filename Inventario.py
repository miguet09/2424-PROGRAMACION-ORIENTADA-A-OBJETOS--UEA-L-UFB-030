# inventario.py

from producto import Producto

class Inventario:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto):
        if not any(p.get_id() == producto.get_id() for p in self.productos):
            self.productos.append(producto)
            print("Producto añadido exitosamente.")
        else:
            print("Error: El ID del producto ya existe.")

    def eliminar_producto(self, id):
        self.productos = [p for p in self.productos if p.get_id() != id]
        print("Producto eliminado si existía.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                print("Producto actualizado exitosamente.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            for p in encontrados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos_productos(self):
        if self.productos:
            for p in self.productos:
                print(p)
        else:
            print("No hay productos en el inventario.")
            