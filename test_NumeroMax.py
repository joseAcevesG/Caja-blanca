import unittest

import NumeroMax


class TestNumeroMax(unittest.TestCase):
    def test_add(self):
        self.assertEqual(NumeroMax.NumeroMax(10, 5, 8), (10, "x"))
        self.assertEqual(NumeroMax.NumeroMax(5, 8, 3), (8, "y"))
        self.assertEqual(NumeroMax.NumeroMax(5, 10, 12), (12, "z"))
        self.assertEqual(NumeroMax.NumeroMax(6, 5, 15), (15, "Z"))


if __name__ == "__main__":
    unittest.main()
