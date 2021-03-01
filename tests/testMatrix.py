import unittest

from src.Maths.Matrix import Matrix

class TestMatrix(unittest.TestCase):

  def test_ctor(self):
    self.assertIsNotNone(Matrix())

if __name__ == '__main__':
    unittest.main()
