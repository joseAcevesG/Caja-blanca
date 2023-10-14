import unittest
import NumeroMax

class TestNumeroMax(unittest.TestCase):
    def test_TC1(self):
        resultado = NumeroMax.NumeroMax(3, 2, 1)
        self.assertEqual(resultado, (3, "x"))

    def test_TC2(self):
        resultado = NumeroMax.NumeroMax(1, 2, 3)
        self.assertEqual(resultado, (3, "z"))

    def test_TC3(self):
        resultado = NumeroMax.NumeroMax(1, 3, 2)
        self.assertEqual(resultado, (3, "y"))

    def test_TC4(self):
        resultado = NumeroMax.NumeroMax(2, 2, 3)
        self.assertEqual(resultado, (3, "z"))

if __name__ == "__main__":
    unittest.main()