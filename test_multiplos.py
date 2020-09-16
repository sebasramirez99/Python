import unittest
import funcionesCICLOS 

class Test_par(unittest.TestCase):
    def test_par(self):
        self.assertEqual(funcionesCICLOS.multiplosrango(2,21,3),([3,6,9,12,15,18,21]))

if __name__ == "__main__":
    unittest.main()
