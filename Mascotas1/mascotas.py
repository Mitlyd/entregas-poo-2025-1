from datetime import datetime
from tabulate import tabulate

class Mascota:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.fecha_ingreso = datetime.now().isoformat()
    
    def obtener_datos(self):
        return [self.__class__.__name__, self.nombre, f"{self.edad} años", self.raza, self.fecha_ingreso]

class Perro(Mascota):
    pass

class Gato(Mascota):
    pass

class Conejo(Mascota):
    pass

class Ave(Mascota):
    pass

def registrar_mascotas():
    mascotas = []
    cantidad = int(input("¿Cuántas mascotas va a ingresar? "))
    
    for i in range(1, cantidad + 1):
        tipo = input(f"Mascota {i}, ¿qué clase es? (Perro, Gato, Conejo, Ave, etc.) ").strip().capitalize()
        nombre = input(f"¿Cuál es el nombre del {tipo}? ").strip()
        
        while True:
            try:
                edad = int(input(f"¿Qué edad tiene '{nombre}'? ").strip())
                break
            except ValueError:
                print("Por favor, ingrese solo un número para la edad.")
        
        raza = input(f"¿De qué raza es '{nombre}'? ").strip()
        
        if tipo == 'Perro':
            mascota = Perro(nombre, edad, raza)
        elif tipo == 'Gato':
            mascota = Gato(nombre, edad, raza)
        elif tipo == 'Conejo':
            mascota = Conejo(nombre, edad, raza)
        elif tipo == 'Ave':
            mascota = Ave(nombre, edad, raza)
        else:
            print("Tipo de mascota no válido, inténtelo de nuevo.")
            continue
        
        mascotas.append(mascota)
    
    print("\nResumen:")
    headers = ["Clase", "Nombre", "Edad", "Raza", "Fecha de ingreso"]
    table = [mascota.obtener_datos() for mascota in mascotas]
    print(tabulate(table, headers=headers, tablefmt="grid"))
    
if __name__ == "__main__":
    registrar_mascotas()

