class Guess:

    def __init__(self, word):
        self.secretWord = word  # 비밀로 선택된 단어를 인자로 받아, 기록해 둠.
        self.guessedChars = []  # 추측에 이용된 글자들의 집합을 빈 집합으로 초기화
        self.numTries = 0  # 실패란 추측의 횟수를 기록하기 위한 변수
        self.succWord = []  # 지금까지 알아낸 철자들을 기록한다. 어차피 순서대로 입력된다
        self.succWordIndex = []  # 그 위치를 가리키는 데이터, 복수개도 가지고 다닐 수 있어야함.
        self.succWords = ''  # 완성되었는지 확인하는애.
        self.currentStatus = ''
        self.count = 0

    def display(self):
        print("Current:", end=" ")
        if self.count > 0:  # count 가 1 이상이 되는 경우부터 succWordIndex가 있을것.
            for i in range(len(self.secretWord)):  # 원래 단어의 길이만큼 반복하며
                if i in self.succWordIndex:  # 만약 인덱스에 맞는 i 일경우 string을 잘라서 다시 저장
                    self.currentStatus = self.currentStatus[:i] + self.secretWord[i] + self.currentStatus[i+1:]
                else:
                    continue
        else:               # 맨 처음 시작할때 _ 를 추가해주기
            for i in range(len(self.secretWord)):
                self.currentStatus = self.currentStatus + '_'
        print(self.currentStatus)
        print("Already used: ", end="")  # 다음 줄과 붙여서 print하기위해 end=""
        print(self.guessedChars)
        print('Tries: ' + str(self.count))  # tries 와 numTries를 구별했다.

    def guess(self, character):
        self.count += 1
        if character in self.secretWord:  # 그 단어안에 있다면 !!
            for i in range(len(self.secretWord)):  # 단어의 길이만큼 반복한다. i는 동시에 index를 나타낸다.
                if character == self.secretWord[i]:  # 인덱스에 해당하는 철자가 character와 같을때.
                    self.succWords = self.succWords + self.secretWord[i]  # 완성되었는지를 확인하는 succWords에 붙임
                    self.succWordIndex.append(i)  # index list에 철자의 위치를 추가한다.
                    self.succWord.append(self.secretWord[i])  # 알아낸 철자 list에 추가한다.
                else:  # 인덱스에 해당하는 철자가 character와 일치하지 않는다. 계속 진행한다.
                    continue
        else:  # 그 단어안에 없다고? !!
            self.numTries += 1  # 기준이 되는 tries 에 1을 더한다.
            self.guessedChars.append(character)  # 추측에 이용된 글자들의 집합에 무조건 추가한다.
        # succWords의 길이는 성공철자를 모두 합쳐놓은 것이므로, 그 길이가 답글자와 같으면 True를 return한다.
        if len(self.succWords) == len(self.secretWord):
            return True
        else:
            return False
