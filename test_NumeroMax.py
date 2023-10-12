import unittest

import NumeroMax

class TestNumeroMax(unittest.TestCase):
    def test_maximo_x(self):
        resultado = NumeroMax.NumeroMax(10, 5, 8)
        self.assertEqual(resultado, (10, "x"))

    def test_maximo_y(self):
        resultado = NumeroMax.NumeroMax(5, 8, 3)
        self.assertEqual(resultado, (8, "y"))

    def test_maximo_z(self):
        resultado = NumeroMax.NumeroMax(5, 10, 12)
        self.assertEqual(resultado, (12, "z"))

    def test_iguales(self):
        resultado = NumeroMax.NumeroMax(5, 5, 5)
        self.assertEqual(resultado, (5, "y"))


if __name__ == "__main__":
    unittest.main()
