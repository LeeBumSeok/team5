import unittest

from word import Word

class TestWord(unittest.TestCase):

    def setUp(self):
        self.word1 = Word('words.txt')

    def tearDown(self):
        pass

    def testrandFromDB(self):
        word_prev = self.word1.randFromDB()
        word_current = self.word1.randFromDB()

        self.assertIsNotNone(word_prev)
        self.assertIsNotNone(word_current)

if __name__ == '__main__':
    unittest.main()