import unittest
from src.Maths.Matrix import Matrix

class TestMatrix(unittest.TestCase):

    def test_ctor(self):
        self.assertIsNotNone(Matrix(10, 20))


    def test_rows(self):
        m = Matrix(20, 22)
        self.assertEqual(20, m.rows)


if __name__ == '__main__':
    unittest.main()
