import time


def fibo(n):  # 원래의 피보나치 재귀구조.
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)


def iterfibo(a):  # 반복구조를 사용한 재귀구조.
    rst = 0
    t1 = 1
    t2 = 0
    if a == 0:  # f(0) == 0.
        return 0
    elif a <= 2:  # f(1),f(2) == 1.
        return 1
    else:  # 아닌경우 반복을 통한 피보나치. f(n) = f(n-1) + f(n-2)
        for i in range(a-1):
            rst = t1 + t2
            t2, t1 = t1, rst  # t2 = t1, t1 = rst.
        return rst


while True:  # 제공된 구조.
    nbr = int(input("Enter a number: "))
    if nbr == -1:  # 종료조건에 부합하는 경우.
        print("Your fibo is ended")
        break
    elif nbr >= 0:  # 종료조건이 아닌 경우.
        ts = time.time()
        fibonumber = iterfibo(nbr)
        ts = time.time() - ts
        print("IterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
        ts = time.time()
        fibonumber = fibo(nbr)
        ts = time.time() - ts
        print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
    else:  # fibo가 불가능한 음수를 입력한 경우.
        print("Please enter natural number to start :)")
