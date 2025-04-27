from datetime import datetime

class Visualizador:
    """Clase que permite visualizar un resumen de las mascotas."""

    @staticmethod
    def resumen(mascotas):
        """Imprime el resumen de las mascotas."""
        print("> Resumen:")
        print("> | Clase   | Nombre   | Edad    | Raza/Tipo   | Fecha de ingreso           |")
        for mascota in mascotas:
            atributo_raza = getattr(mascota, 'raza', getattr(mascota, 'especie', getattr(mascota, 'tipo', '')))
            print(f"> | {mascota.__class__.__name__:8} | "
                  f"{mascota.nombre:8} | "
                  f"{mascota.edad} años | "
                  f"{atributo_raza:10} | "
                  f"{mascota.fecha_ingreso} |")

class Mascota:
    """Clase base para todas las mascotas."""
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.fecha_ingreso = datetime.now().isoformat()

# Clases específicas
class Perro(Mascota, Visualizador):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

class Gato(Mascota, Visualizador):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

class Conejo(Mascota, Visualizador):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

class Pajaro(Mascota, Visualizador):
    def __init__(self, nombre, edad, especie):
        super().__init__(nombre, edad)
        self.especie = especie

class Tortuga(Mascota, Visualizador):
    def __init__(self, nombre, edad, tipo):
        super().__init__(nombre, edad)
        self.tipo = tipo

# Función para ingresar mascota
def ingresar_mascota(indice):
    """Función para ingresar datos de una mascota."""
    while True:
        tipo = input(f"> Mascota {indice}, ¿qué clase es (P)erro, (G)ato, (C)onejo, (Pa)jaro o (T)ortuga?\n< ").strip().lower()
        if tipo in ('perro', 'gato', 'conejo', 'pajaro', 'tortuga', 'perro', 'gato', 'conejo', 'pajaro', 'tortuga'):
            break
        print("Por favor ingrese una opción válida (Perro, Gato, Conejo, Pajaro, Tortuga).")
    
    nombre = input(f"> ¿Cuál es el nombre del {tipo.capitalize()}?\n< ").strip()
    edad = int(input(f"> ¿Qué edad tiene '{nombre}'?\n< ").strip())

    if tipo.startswith('p') and tipo != 'pa':
        raza = input(f"> ¿De qué raza es '{nombre}'?\n< ").strip()
        return Perro(nombre, edad, raza)
    elif tipo.startswith('g'):
        raza = input(f"> ¿De qué raza es '{nombre}'?\n< ").strip()
        return Gato(nombre, edad, raza)
    elif tipo.startswith('c'):
        raza = input(f"> ¿De qué raza es '{nombre}'?\n< ").strip()
        return Conejo(nombre, edad, raza)
    elif tipo.startswith('pa'):
        especie = input(f"> ¿Qué especie de pájaro es '{nombre}'?\n< ").strip()
        return Pajaro(nombre, edad, especie)
    elif tipo.startswith('t'):
        tipo_tortuga = input(f"> ¿Qué tipo de tortuga es '{nombre}'? (ej: acuática, terrestre)\n< ").strip()
        return Tortuga(nombre, edad, tipo_tortuga)

def main():
    """Función principal del programa."""
    mascotas = []
    cantidad = int(input("> ¿Cuántas mascotas va a ingresar?\n< ").strip())
    for i in range(1, cantidad + 1):
        mascota = ingresar_mascota(i)
        mascotas.append(mascota)

    # Mostrar resumen
    Visualizador.resumen(mascotas)

if __name__ == "__main__":
    main()

