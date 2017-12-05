import unittest

from hangman import Hangman

class TestHangman(unittest.TestCase):

    def setUp(self):
        self.hman = Hangman()

    def tearDown(self):
        pass

    def testDecreaseLife(self):
        remainingLives_prev = self.hman.remainingLives
        self.assertTrue(self.hman.remainingLives)
        self.hman.decreaseLife()
        self.assertNotEqual(remainingLives_prev, self.hman.remainingLives)

    def testCurrentShape(self):
        self.assertEqual(self.hman.currentShape(),'''\
   ____
  |    |
  |
  |
  |
  |
 _|_
|   |______
|          |
|__________|\
''')
        self.hman.decreaseLife()
        self.assertEqual(self.hman.currentShape(),'''\
   ____
  |    |
  |    o
  |
  |
  |
 _|_
|   |______
|          |
|__________|\
''')


if __name__ == '__main__':
    unittest.main()