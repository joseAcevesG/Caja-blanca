import unittest
import MCD

class TestMCD(unittest.TestCase):        
    def test_TC1(self):
        self.assertEqual(MCD.mcd(0, 1), -1)
    def test_TC2(self):
        self.assertEqual(MCD.mcd(1, 0), -1)
    def test_TC3(self):
        self.assertEqual(MCD.mcd(1, 2), 1)
    def test_TC4(self):
        self.assertEqual(MCD.mcd(2, 1), 1)
    def test_TC5(self):
        self.assertEqual(MCD.mcd(2, 2), 2)
    def test_TC6(self):
        self.assertEqual(MCD.mcd(6, 2), 2)
    def test_TC7(self):
        self.assertEqual(MCD.mcd(2, 6), 2)

if __name__ == "__main__":
    unittest.main()
