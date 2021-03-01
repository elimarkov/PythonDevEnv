import unittest

from src.Maths.Matrix import Matrix

class TestMatrix(unittest.TestCase):

  def test_ctor(self):
    self.assertIsNotNone(Matrix(10, 20))

if __name__ == '__main__':
    unittest.main()
