import unittest
from calculadora_matriz import Matriz

class TestMatriz(unittest.TestCase):
    def test_suma(self):
        m1 = Matriz([[1, 2], [3, 4]])
        m2 = Matriz([[5, 6], [7, 8]])
        resultado = m1 + m2
        self.assertEqual(resultado.valores, [[6, 8], [10, 12]])

    def test_resta(self):
        m1 = Matriz([[5, 5], [5, 5]])
        m2 = Matriz([[2, 2], [2, 2]])
        resultado = m1 - m2
        self.assertEqual(resultado.valores, [[3, 3], [3, 3]])

    def test_multiplicacion(self):
        m1 = Matriz([[1, 2], [3, 4]])
        m2 = Matriz([[2, 0], [1, 2]])
        resultado = m1 * m2
        self.assertEqual(resultado.valores, [[4, 4], [10, 8]])

if __name__ == '__main__':
    unittest.main()
