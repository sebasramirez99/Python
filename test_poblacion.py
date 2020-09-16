import unittest
import funcionesCICLOS 

class Test_par(unittest.TestCase):
    def test_par(self):
        self.assertEqual(funcionesCICLOS.superarpoblacion(35,19.9,2,3),(2022))

if __name__ == "__main__":
    unittest.main()