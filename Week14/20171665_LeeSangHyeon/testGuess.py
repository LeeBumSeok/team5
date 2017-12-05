import unittest

from guess import Guess


class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')
        self.g2 = Guess('self')

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
        self.g1.guess('r')  # 속하지 않을때
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.g2.guess('t')
        self.assertEqual(self.g2.displayCurrent(), '_ e _ _ ')
        self.g2.guess('f')
        self.assertEqual(self.g2.displayCurrent(), '_ e _ f ')

    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
        self.g1.guess('r')  # 상관없이 새로운 문자가 들어가야할 곳에 들어가는지?
        self.assertEqual(self.g1.displayGuessed(), ' a e n r t u ')
        self.g2.guess('t')
        self.assertEqual(self.g2.displayGuessed(), ' e n t ')
        self.g2.guess('f')
        self.assertEqual(self.g2.displayGuessed(), ' e f n t ')

    def testGuess(self):
        self.assertEqual(self.g1.guess('a'), True)
        self.assertEqual(self.g1.guess('g'), False)
        self.assertEqual(self.g1.guess('x'), False)
        self.assertEqual(self.g2.guess('t'), False)
        self.assertEqual(self.g2.guess('f'), True)

    # def testWord(self):
    #     self.assertEqual(self.g2.test(), 'default')

if __name__ == '__main__':
    unittest.main()
