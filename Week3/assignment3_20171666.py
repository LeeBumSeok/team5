import pickle

dbfilename = 'assignment3.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb =  pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()

def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':  #새로운 이름을 입력해도 오류가나지않음.
            try:
                record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
                scdb += [record]
            except:  #list index out of range 예외처리.
                print("Please input 'Name','Age','Score' in sequence")
        elif parse[0] == 'del': # modified 'del', 새로운 이름을 입력하는 경우에 오류는 나지않음.> 없다고 표시.
            rmlist = []
            for p in scdb:
                if p['Name'] == parse[1]:
                    rmlist.append(p)
            for p in rmlist:
                scdb.remove(p)
            if not(bool(rmlist)):  # 빈 리스트는 false값을 가지므로,, rmlist가 비어있으면 프린트할것.
                print("There is no person matches with input name")         
        elif parse[0] == 'show':
            try:
                sortKey ='Name' if len(parse) == 1 else parse[1]
                showScoreDB(scdb, sortKey)
            except:
                print("Please enter 'Show' only.")
        elif parse[0] == 'find': # created 'find'  find뒤에 이상한 이름이 입력됐을때도 처리.
                flist=[]
                for p in scdb: # flist .. to print.
                    if p['Name'] == parse[1]:
                            flist.append(p)
                for p in flist:
                    print('Age='+p['Age']+' '+'Name='+p['Name']+' '+'Score='+p['Score'])
                if not(bool(flist)):  #없을때.
                    print("Please Enter existing name")
        elif parse[0] == 'inc': # about inc,, creating inc / inc 뒤의 name이 없는 name일 경우. 예외처리 아직 다 못함!!!
            try:
                if (int(p['Score'])+int(parse[2])) <= 100:  #100을 초과하는 점수가 만들어질경우.
                    for p in scdb:
                        if p['Name'] == parse[1]:
                            p['Score'] = str(int(p['Score'])+int(parse[2]))
                else:
                    print("The Maximum score is 100")
            except:
                print("I beg your pardon")
        elif parse[0] == 'quit':
            break
        else: # 없는 명령에대한 예외처리는 이미 되어있음. 
            print("Invalid command: " + parse[0])
            

def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()
    

scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)

