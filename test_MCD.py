import unittest

import MCD


class TestMCD(unittest.TestCase):
    def test_add(self):
        self.assertEqual(MCD.mcd(1, 0), -1)
        self.assertEqual(MCD.mcd(0, 1), -1)
        self.assertEqual(MCD.mcd(1, 2), 1)
        self.assertEqual(MCD.mcd(2, 1), 1)
        self.assertEqual(MCD.mcd(2, 2), 2)


if __name__ == "__main__":
    unittest.main()
