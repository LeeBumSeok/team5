while True : 
    num = int(input("enter number:"))
    fact = 1
    if num < -1 :
        print("error")
    elif num == -1 :
        print("done")
        break
    else : 
        for i in range(1,num+1):
            fact=fact*i
        print(fact)


