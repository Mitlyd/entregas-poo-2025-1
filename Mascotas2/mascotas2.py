from datetime import datetime

class Visualizador:
    """Clase que permite visualizar un resumen de la mascota."""

    @staticmethod
    def resumen(mascotas):
        """Imprime el resumen de las mascotas."""
        print("> Resumen:")
        print("> |Clase |Nombre   |Edad   |Raza         |Fecha de ingreso          |")
        for mascota in mascotas:
            print(f"> |{mascota.__class__.__name__:6}|"
                  f"{mascota.nombre:8}|"
                  f"{mascota.edad} años |"
                  f"{mascota.raza:13}|"
                  f"{mascota.fecha_ingreso}|")

class Mascota:
    """Clase base para todas las mascotas."""

    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.fecha_ingreso = datetime.now().isoformat()

class Perro(Mascota, Visualizador):
    """Clase que representa un perro."""
    pass

class Gato(Mascota, Visualizador):
    """Clase que representa un gato."""
    pass

def ingresar_mascota(indice):
    """Función para ingresar datos de una mascota."""
    while True:
        tipo = input(f"> Mascota {indice}, ¿qué clase es (P)erro o (G)ato?\n< ").strip().lower()
        if tipo in ('p', 'g', 'perro', 'gato'):
            break
        print("Por favor ingrese 'P' para perro o 'G' para gato.")
    
    nombre = input(f"> ¿Cuál es el nombre del {'Perro' if tipo.startswith('p') else 'Gato'}?\n< ").strip()
    edad = int(input(f"> ¿Qué edad tiene '{nombre}'?\n< ").strip())
    raza = input(f"> ¿De qué raza es '{nombre}'?\n< ").strip()

    if tipo.startswith('p'):
        return Perro(nombre, edad, raza)
    else:
        return Gato(nombre, edad, raza)

def main():
    """Función principal del programa."""
    mascotas = []
    cantidad = int(input("> ¿Cuántas mascotas va a ingresar?\n< ").strip())
    for i in range(1, cantidad + 1):
        mascota = ingresar_mascota(i)
        mascotas.append(mascota)

    # Usamos el método resumen de Visualizador
    Visualizador.resumen(mascotas)

if __name__ == "__main__":
    main()
