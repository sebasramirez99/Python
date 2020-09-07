import unittest
import funciones 

class Test_edad(unittest.TestCase):
    def test_edad(self):
        self.assertEqual(funciones.edad(21,2020), 26)

if __name__ == "__main__":
    unittest.main()