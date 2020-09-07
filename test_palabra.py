import unittest
import funciones 

class Test_palabra(unittest.TestCase):
    def test_palabra(self):
        self.assertEqual(funciones.pala("sebas"),("s","s"))

if __name__ == "__main__":
    unittest.main()