import unittest

from guess import Guess

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')

    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.g1.guess('z')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.g1.guess('b')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')


    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
        self.g1.guess('z')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u z ')
        self.g1.guess('b')
        self.assertEqual(self.g1.displayGuessed(), ' a b e n t u z ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a b e n t u z ')

    def testFinished(self):
        self.g1.currentStatus = 'default'
        self.assertTrue(self.g1.finished())
        self.g1.currentStatus = 'defauld'
        self.assertFalse(self.g1.finished())
        self.g1.currentStatus = ''
        self.assertFalse(self.g1.finished())

    def testGuess(self):
        self.assertIsNotNone(self.g1.guessedChars)
        self.assertEqual(self.g1.guessedChars, { '', 'e', 'n'})
        self.assertEqual(self.g1.currentStatus, '_e_____')

        self.assertTrue(self.g1.guess('a'))
        self.assertEqual(self.g1.guessedChars, {'a', '', 'e', 'n'})
        self.assertEqual(self.g1.currentStatus, '_e_a___')

        self.assertTrue(self.g1.guess('t'))
        self.assertEqual(self.g1.guessedChars, {'t', 'a', '', 'e', 'n'})
        self.assertEqual(self.g1.currentStatus, '_e_a__t')

        self.assertTrue(self.g1.guess('u'))
        self.assertEqual(self.g1.guessedChars, {'u', 't', 'a', '', 'e', 'n'})
        self.assertEqual(self.g1.currentStatus, '_e_au_t')

        self.assertFalse(self.g1.guess('b'))
        self.assertEqual(self.g1.guessedChars, {'b', 'u', 't', 'a', '', 'e', 'n'})
        self.assertEqual(self.g1.currentStatus, '_e_au_t')

        self.assertFalse(self.g1.guess('z'))
        self.assertEqual(self.g1.guessedChars, {'z', 'b', 'u', 't', 'a', '', 'e', 'n'})
        self.assertEqual(self.g1.currentStatus, '_e_au_t')


if __name__ == '__main__':
    unittest.main()
