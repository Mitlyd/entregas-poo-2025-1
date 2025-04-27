


import unittest

from mascotas2 import Perro, Gato

class TestMascota(unittest.TestCase):
    def test_creacion_perro(self):
        perro = Perro("Rocky", 2, "Bulldog")
        self.assertEqual(perro.nombre, "Rocky")
        self.assertEqual(perro.edad, 2)
        self.assertEqual(perro.raza, "Bulldog")
        self.assertIsNotNone(perro.fecha_ingreso)

    def test_creacion_gato(self):
        gato = Gato("Mishi", 3, "Angora")
        self.assertEqual(gato.nombre, "Mishi")
        self.assertEqual(gato.edad, 3)
        self.assertEqual(gato.raza, "Angora")
        self.assertIsNotNone(gato.fecha_ingreso)

if __name__ == "__main__":
    unittest.main()
