from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout

from keypad import numPadList, operatorList, constantList, functionList

import calcFunctions  # 팩토리얼같은 연산을 하는 애들을 모아놓은 모듈
import constantDef  # 키가 눌리면 그 값에 대응하는 str를 돌려주는 모듈


class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Display Window
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        # Layout settings.
        numLayout = QGridLayout()
        opLayout = QGridLayout()
        constantLayout = QGridLayout()
        funcLayout = QGridLayout()

        buttonGroups = {
            'num': {'buttons': numPadList, 'layout': numLayout, 'columns': 3},
            'op': {'buttons': operatorList, 'layout': opLayout, 'columns': 2},
            'constants': {'buttons': constantList, 'layout': constantLayout, 'columns': 1},
            'functions': {'buttons': functionList, 'layout': funcLayout, 'columns': 1},
        }

        for label in buttonGroups.keys():
            r = 0; c = 0
            buttonPad = buttonGroups[label]
            for btnText in buttonPad['buttons']:
                button = Button(btnText, self.buttonClicked)
                buttonPad['layout'].addWidget(button, r, c)
                c += 1
                if c >= buttonPad['columns']:
                    c = 0; r += 1

        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)
        mainLayout.addLayout(numLayout, 1, 0)
        mainLayout.addLayout(opLayout, 1, 1)
        mainLayout.addLayout(constantLayout, 2, 0)
        mainLayout.addLayout(funcLayout, 2, 1)
        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")

    def buttonClicked(self):
        button = self.sender()
        key = button.text()

        if key == '=':
            # eval해서 이상한 일이 생길때
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except:
                # broad exception.. 어떠한 에러가 발생하는 경우, syntax,zero,type ...
                # 에러가 발생하는 input을 지우고 에러가 발생했다는 메세지박스를 띄운다.
                # time...을 사용해서 멈춰두고 싶었으나 불가능했음. 차선.
                self.display.setText('')
                QMessageBox.question(self, 'Error!', 'Error occurred', QMessageBox.Ok)  # 선택지로 ok만 나옴
        elif key in functionList:
            try:
                # @ calcFunction(제공)에서 exception이 되어있어서 내가 원하는 상황이 안나옴
                # @  ^ 에서 except를 지워버림.
                n = self.display.text()
                value = calcFunctions.calcFunctions(key, n)
                self.display.setText(value)
            except:
                self.display.setText('')
                QMessageBox.question(self, 'Error!', 'Error occurred', QMessageBox.Ok)  # 선택지로 ok만 나옴
        elif key == 'C':
            self.display.setText('')
        elif key in constantList:
            #  constantDef 모듈안의> constantsDef 함수를 가지고 와서 사용.
            #  @ 이 상수에 factorial 같은 키를 누르면> Error.
            self.display.setText(self.display.text() + constantDef.constantsDef(key))
        else:
            self.display.setText(self.display.text() + key)

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
