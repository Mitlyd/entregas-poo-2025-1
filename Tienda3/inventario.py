from tabulate import tabulate

class Producto:
    """
    Clase que representa un producto en la tienda.
    """
    def __init__(self, nombre, precio, cantidad, descripcion, clasificacion):
        """
        Inicializa un producto con los atributos dados.
        """
        self.nombre = nombre
        self.precio = float(precio)
        self.cantidad = int(cantidad)
        self.descripcion = descripcion
        self.clasificacion = clasificacion

    def calcula_precio(self, cantidad):
        """Devuelve el precio total al comprar 'cantidad' unidades."""
        return self.precio * cantidad

    def inventario_precio(self):
        """Devuelve el valor total de mercancía de este producto en el inventario."""
        return self.precio * self.cantidad


def obtener_productos():
    """Genera una lista de productos predeterminados."""
    productos = [
        Producto("SALCHICHA RANCHERA", 4500, 10, "SALCHICHA RANCHERA x3 marca", "alimentación"),
        Producto("Queso Mozzarella", 9400, 8, "QUESO MOZZARELLA TAJADO x400", "alimentación"),
        Producto("Tocino Carnudo", 10000, 12, "TOCINO CARNUDO x500 GRS", "alimentación"),
        Producto("Yogurt Melocotón", 3000, 14, "Yogurt Alpina Melocotón x150", "alimentación"),
        Producto("Leche Deslactosada", 34000, 14, "Leche Colanta Deslactosada S", "alimentación")
    ]
    return productos


def ingresar_productos():
    productos = obtener_productos()
    cantidad_productos = int(input("¿Cuántos productos adicionales va a ingresar? "))

    for i in range(1, cantidad_productos + 1):
        print(f"\nProducto {i}, ¿cuál es el nombre?")
        nombre = input("> ")
        precio = float(input(f"¿Cuál es el precio de '{nombre}'? > "))
        cantidad = int(input(f"¿Qué cantidad hay de '{nombre}'? > "))
        descripcion = input(f"Introduzca la descripción de '{nombre}': > ")
        clasificacion = input(f"¿Qué clasificación tiene '{nombre}'? > ")
        productos.append(Producto(nombre, precio, cantidad, descripcion, clasificacion))

    return productos


def mostrar_resumen(productos):
    """Muestra el resumen de los productos ingresados en formato de tabla."""
    
    tabla_productos = []
    
    for producto in productos:
        tabla_productos.append([
            producto.nombre, 
            f"{producto.cantidad} unidades",
            f"{producto.precio:,.2f} pesos",
            producto.descripcion[:22] + "..." if len(producto.descripcion) > 22 else producto.descripcion,
            producto.clasificacion,
            f"{producto.inventario_precio():,.2f} pesos",
            f"{producto.calcula_precio(5):,.2f} pesos"
        ])

    headers = ["Producto", "Cantidad", "Precio", "Descripción", "Clasificación", "Total en inventario", "Precio x5 unidades"]

    print("\n Resumen de Productos:\n")
    print(tabulate(tabla_productos, headers=headers, tablefmt="fancy_grid"))

    calcular_precio_por_clasificacion(productos)


def calcular_precio_por_clasificacion(productos):
    """Calcula y muestra el precio total por clasificación en una tabla organizada."""
    precios_por_clasificacion = {}

    for producto in productos:
        precio_total_producto = producto.inventario_precio()
        if producto.clasificacion in precios_por_clasificacion:
            precios_por_clasificacion[producto.clasificacion] += precio_total_producto
        else:
            precios_por_clasificacion[producto.clasificacion] = precio_total_producto

    tabla_clasificacion = [[clasificacion, f"{precio_total:,.2f} pesos"] for clasificacion, precio_total in precios_por_clasificacion.items()]

    print("\n Precios por Clasificación:\n")
    print(tabulate(tabla_clasificacion, headers=["Clasificación", "Precio Total"], tablefmt="fancy_grid"))


if __name__ == "__main__":
    productos = ingresar_productos()
    mostrar_resumen(productos)

