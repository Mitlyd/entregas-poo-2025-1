class Matriz:
    """
    Clase que representa una matriz 2x2 y permite operaciones de suma, resta y multiplicación.
    """
    def __init__(self, valores):
        if len(valores) != 2 or any(len(fila) != 2 for fila in valores):
            raise ValueError("La matriz debe ser de tamaño 2x2")
        self.valores = valores

    def __add__(self, other):
        return Matriz([
            [self.valores[i][j] + other.valores[i][j] for j in range(2)]
            for i in range(2)
        ])

    def __sub__(self, other):
        return Matriz([
            [self.valores[i][j] - other.valores[i][j] for j in range(2)]
            for i in range(2)
        ])

    def __mul__(self, other):
        a = self.valores
        b = other.valores
        return Matriz([
            [
                a[0][0]*b[0][0] + a[0][1]*b[1][0],
                a[0][0]*b[0][1] + a[0][1]*b[1][1]
            ],
            [
                a[1][0]*b[0][0] + a[1][1]*b[1][0],
                a[1][0]*b[0][1] + a[1][1]*b[1][1]
            ]
        ])

    def mostrar(self):
        print(f"|{self.valores[0][0]}  {self.valores[0][1]}|")
        print(f"|{self.valores[1][0]}  {self.valores[1][1]}|")


def leer_matriz(numero):
    print(f"Ingrese los valores de la Matriz {numero}:")
    matriz = []
    for i in range(2):
        fila = []
        for j in range(2):
            valor = int(input(f"Matriz {numero}: elemento {i},{j} -> "))
            fila.append(valor)
        matriz.append(fila)
    return Matriz(matriz)


def menu():
    print("\nEscriba:")
    print("1 para suma")
    print("2 para resta")
    print("3 para multiplicación")
    return int(input("Opción -> "))


if __name__ == "__main__":
    matriz1 = leer_matriz(1)
    matriz2 = leer_matriz(2)

    print("\nMatriz 1:")
    matriz1.mostrar()

    print("Matriz 2:")
    matriz2.mostrar()

    opcion = menu()

    if opcion == 1:
        resultado = matriz1 + matriz2
        print("\nLa suma de las dos matrices es:")
    elif opcion == 2:
        resultado = matriz1 - matriz2
        print("\nLa resta de las dos matrices es:")
    elif opcion == 3:
        resultado = matriz1 * matriz2
        print("\nLa multiplicación de las dos matrices es:")
    else:
        print("Opción inválida.")
        exit()

    resultado.mostrar()
