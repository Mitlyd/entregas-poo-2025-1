import unittest

from mascotas2 import Perro, Gato, Conejo, Pajaro, Tortuga

class TestMascota(unittest.TestCase):
    def test_creacion_perro(self):
        perro = Perro("Ratona", 2, "Pitbull Blue")
        self.assertEqual(perro.nombre, "Ratona")
        self.assertEqual(perro.edad, 2)
        self.assertEqual(perro.raza, "pitbull blue")
        self.assertIsNotNone(perro.fecha_ingreso)

    def test_creacion_gato(self):
        gato = Gato("Darko", 2, "Criollo")
        self.assertEqual(gato.nombre, "Darko")
        self.assertEqual(gato.edad, 2)
        self.assertEqual(gato.raza, "Criollo")
        self.assertIsNotNone(gato.fecha_ingreso)

    def test_creacion_conejo(self):
        conejo = Conejo("Max", 1, "rex")
        self.assertEqual(conejo.nombre, "Max")
        self.assertEqual(conejo.edad, 1)
        self.assertEqual(conejo.raza, "rex")
        self.assertIsNotNone(conejo.fecha_ingreso)

    def test_creacion_pajaro(self):
        pajaro = Pajaro("Matius", 4, "Canario")
        self.assertEqual(pajaro.nombre, "Matius")
        self.assertEqual(pajaro.edad, 4)
        self.assertEqual(pajaro.especie, "Canario")
        self.assertIsNotNone(pajaro.fecha_ingreso)

    def test_creacion_tortuga(self):
        tortuga = Tortuga("Mar", 1, "Terrestre")
        self.assertEqual(tortuga.nombre, "Mar")
        self.assertEqual(tortuga.edad, 1)
        self.assertEqual(tortuga.tipo, "Terrestre")
        self.assertIsNotNone(tortuga.fecha_ingreso)

if __name__ == "__main__":
    unittest.main()
