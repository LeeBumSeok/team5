import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QBoxLayout,QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()
        self.msg=''

    def initUI(self):
        
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        name = QLabel('Name:')
        age = QLabel('Age:')
        score = QLabel('Score:')
        amount = QLabel('Amount:')
        key = QLabel('Key:')

        self.nameedit = QLineEdit()
        self.ageedit = QLineEdit()
        self.scoreedit = QLineEdit()
        self.amountedit = QLineEdit()
        self.keycombo = QComboBox(self)

        self.keycombo.addItem('Age')
        self.keycombo.addItem('Name')
        self.keycombo.addItem('Score')

        add = QPushButton('Add')
        delete = QPushButton('Del')
        find = QPushButton('Find')
        inc = QPushButton('Inc')
        show = QPushButton('Show')

        result = QLabel('Result:')

        self.resultedit = QTextEdit(self)

        #set Layout

        hbox = QHBoxLayout()
        hbox.addWidget(name)
        hbox.addWidget(self.nameedit)
        hbox.addWidget(age)
        hbox.addWidget(self.ageedit)
        hbox.addWidget(score)
        hbox.addWidget(self.scoreedit)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(amount)
        hbox2.addWidget(self.amountedit)
        hbox2.addWidget(key)
        hbox2.addWidget(self.keycombo)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(add)
        hbox3.addWidget(delete)
        hbox3.addWidget(find)
        hbox3.addWidget(inc)
        hbox3.addWidget(show)

        hbox4 = QHBoxLayout()
        hbox4.addWidget(result)

        hbox5 = QHBoxLayout()
        hbox5.addWidget(self.resultedit)

        vbox = QVBoxLayout()
        vbox.addStretch(5)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)

        self.setLayout(vbox)

        #event connect

        add.clicked.connect(self.Add)
        delete.clicked.connect(self.Delete)
        find.clicked.connect(self.Find)
        inc.clicked.connect(self.Inc)
        show.clicked.connect(self.Show)

        self.setGeometry(300,300,500,300)
        self.show()

    def closeEvent(self, event):

        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
            return self.scoredb
        except:
            print("Empty DB: ", self.dbfilename)
        else:
            print("Open DB: ", self.dbfilename)
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')

        #change Type to int

        for i in self.scoredb:
            i['Age'] = int(i['Age'])
            i['Score'] = int(i['Score'])

        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):

        #get values of scoredb

        sss = self.readScoreDB()
        aaa=''

        #show scoredb in TextEdit by using String variable

        for i in sorted(sss, key=lambda person: person['Name']):

            for j in sorted(i):

                if j == 'Age' or j == 'Score':

                    i[j] = str(i[j])

                aaa += (j + '=' + i[j] + '\t')

            aaa += '\n'

        self.resultedit.setText(aaa)

    def Add(self):

        # get value from each LineEdit

        name = self.nameedit.text()
        age = self.ageedit.text()
        score = self.scoreedit.text()

        #set new Dictionary and append to Scoredb

        new = {'Age':age, 'Name':name, 'Score':score}
        self.scoredb.append(new)

        self.writeScoreDB()
        self.showScoreDB()


    def Delete(self):

        #get value from LineEdit 'Name'

        new_scoredb = []
        delname = self.nameedit.text()

        #Compare with scoredb and append to new_Scoredb

        for i in self.scoredb:
            if i['Name'] != delname:
                new_scoredb.append(i)

        #modify scoredb

        self.scoredb = new_scoredb

        self.writeScoreDB()
        self.showScoreDB()


    def Find(self):

        #get value from LineEdit 'Name'

        find_name = self.nameedit.text()
        bbb=''
        find_scoredb=[]

        #set find_List about same Name

        for i in self.scoredb:
            if i['Name'] == find_name:
                find_scoredb.append(i)

        #show find_List

        for p in find_scoredb:
            for z in p:
                if z == 'Age' or z == 'Score':
                    p[z] = str(p[z])
                bbb += (z + '=' + p[z] + '\t')
            bbb += '\n'
        self.resultedit.setText(bbb)

    def Inc(self):

        #get value from LineEdit 'Name' and 'Amount'

        inc_name = self.nameedit.text()
        inc_amount = self.amountedit.text()

        #Change Type and add amount

        for i in self.scoredb:
            if i['Name'] == inc_name:
                i['Score'] = int(i['Score'])
                i['Score'] += int(inc_amount)

        #modify Scoredb value and show

        self.writeScoreDB()
        self.showScoreDB()


    def Show(self,text):
        text = self.keycombo.currentText()      #get value from combobox
        strdb = self.readScoreDB()
        msg=''

        # set Text to TextEditBox from Scoredb

        for i in sorted(strdb, key=lambda person: person[text]):
            for j in sorted(i):
                if j == 'Age' or j == 'Score':
                    i[j] = str(i[j])
                msg += (j + '=' + i[j] + '\t')
            msg += '\n'
        self.resultedit.setText(msg)

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())





