import unittest
import funciones 

class Test_par(unittest.TestCase):
    def test_par(self):
        self.assertEqual(funciones.numeroPar(2),True)

if __name__ == "__main__":
    unittest.main()