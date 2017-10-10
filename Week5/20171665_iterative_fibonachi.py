import time

def fibo(n):
    fibolist = []
    for i in range(n+1):
        if i == 0:
            fibolist.append(i)
        elif i == 1:
            fibolist.append(i)
        else:
            a = fibolist[i-1] + fibolist[i-2]
            fibolist.append(a)
    return fibolist[n]

if __name__ == '__main__':
    while True:
        nbr = int(input("Enter number: "))
        if nbr == -1:
            print("done!")
            break
        ts = time.time()
        result = fibo(nbr)
        ts = time.time() -ts
        print ("Fibo (%d) = %d, time %.6f" %(nbr, result, ts))





