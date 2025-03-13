class prroducto:
"""
Clase que representa un producto en la Tienda.
"""
def __init__(self, nombre, precio, cantidad, descripcion, clasificacion):
     """
    Inicializa un producto con los atributos dados.
    :param nombre:Nombre del Producto.
    :param precio:Precio Unitario del Producto.
    :param cantidad:cantidad Disponible del Producto.
    :param descripcion:Descripcion Detallada del Producto.
    :param clasificacion:Clasificacion o Categoria del Producto
     """

     self.nombre=nombre
     self.precio=float(precio)
     self.cantidad=int(cantidad)
     self.descripcion=descripcion
     self.clasificacion=clasificacion

     def calcula_precio(self,cantidad):  
        """ Devuelve el precio total al comprar 'cantidad' unidades."""
        return self.precio * self.cantidad

     def inventario_precio(self):
        """ Devuelve el valor total de mercancia de este producto en el inventario. """ 
        return self.precio * self.cantidad

     def obtener_productos():
        """ Generera una lista de productos predeterminados."""


        productos = [
           
         Producto("SALCHICHA RANCHERA", 4500, 10, "SALCHICHA RANCHERA x3 marca", "alimentación"),
         Producto("Queso Mozzarella", 9400, 8, "QUESO MOZZARELLA TAJADO x400", "alimentación"),
         Producto("Tocino Carnudo", 10000, 12, "TOCINO CARNUDO x500 GRS", "alimentación"),
         Producto("Yogurt Melocotón", 3000, 14, "Yogurt Alpina Melocotón x150", "alimentación"),
         Producto("Leche Deslactosada", 34000, 14, "Leche Colanta Deslactosada", "alimentación")

         ]
         
         return productos


     def ingresar_productos():
        """ Permitir al usuario ingresar productos manualmente."""
        productos = obtener_productos()
        cantidad_productos = int(input("¿Cuántos productos adicionales va a ingresar?"))

        for i in range(1, cantidad_productos + 1):

            print(f"\nProducto {i}, ¿Cuál es el nombre?")
            nombre = input("> ")
            precio = float(input(f"¿Cuál es el precio de '{nombre}'? > "))
            cantidad = int(input(f"¿Qué cantidad hay de '{nombre}'? >"))
            descripcion = input(f"Introduzca la descripcion de '{nombre}': >")
            clasificacion = input(f"¿Qué clasificación tiene '{nombre}'? >")
            productos.append(Producto(nombre, precio, cantidad, descripcion, clasificacion))

            return productos

            def mostrar_resumen(productos):
                """Mostrara el resumen de los productos ingresados."""

                print("\nResume:")

                print(f"{'Producto':<15}{'Cantidad':<10}{'Precio':<10}{'Descripcion':<25}{'Clasificacion':<15}{'Total Inv.':<15}{'Precio x5'}")
                print("=" * 100)

                for producto in productos:
                    total_inv = producto.inventario_precio()
                    precio_5_unidades = producto.calcula_precio(5)
                    print(f"{producto.nombre:<15}{producto.cantidad:<10}{producto.precio:<10.2f}{producto.descripcion[:22]:<25}{producto.clasificacion:<15}{total_inv:<15.2f}{precio_5_unidades:<10.2f}")

                    calcula_precio_por_clasificacion(productos)

                    def calcula_precio_por_clasificacion(productos):
                        """Calcula y muestra el precio total por Clasificacion"""

                        precios_por_clasificacion = {}

                     for producto in productos:
                        precio_total_producto = producto.inventario_precio()  

                        if producto.clasificacion in precios_por_clasificacion:
                            precios_por_clasificacion[producto.clasificacion] += precio_total_producto
                            else:
                                precios_por_clasificacion[producto.clasificacion] = precio_total_producto

                        print("\nPrecios por clasificación:")
                        print(f"{'Clasificación':<20}{'Precio Total':<15}")
                        print("=" * 40)

                        for clasificacion,precio_total in precios_por_clasificacion.items():
                            print(f"{'clasificacion':<20}{'precio_total':<15.2f}")

                            if __name__ == "__main__":
                                productos = ingresar_productos()
                                mostrar_resumen(productos)