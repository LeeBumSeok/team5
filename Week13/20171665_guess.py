class Guess:

    def __init__(self, word):

        self.secretWord = word
        self.guessedChars = []
        self.numTries = 0

        self.tempword = word
        self.currentStatus = '_' * len(word)


    def display(self):

        print ('Current: ' + self.currentStatus )
        print ('Tries: ' + str(self.numTries))

    def guess(self, character):

        self.guessedChars.append(character)

        count = False
        secret = '_' * len(self.secretWord)

        while self.tempword != secret:
            if character in self.tempword:
                tempidx = self.tempword.find(character)
                self.currentStatus = self.currentStatus[:tempidx] + character + self.currentStatus[(tempidx + 1):]
                self.tempword = self.tempword[:tempidx] + '_' + self.tempword[(tempidx + 1):]
                count = True
            elif count == True:
                break
            else:
                self.numTries += 1
                break
        else:
            return True