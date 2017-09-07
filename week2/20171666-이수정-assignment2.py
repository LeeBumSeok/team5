def factorial(a):  # factorial 구현.
    result = 1
    if a == 0:  # 0! = 1.
        return 1
    while a > 0:  # a을 계속 -1 하면서 계산.
        result *= a
        a -= 1
    return result

while True:  # input 값을 int로 제한시켜줌, stack overflow 참조.
    try:
        num = int(input("Enter number to start factorial = "))
        break
    except ValueError:
        print("Please enter natural number.")

while num + 1:  # -1일때 멈추고 아닌 값들에서는 반복동작.
    print(factorial(num))
    while True:  # 반복을 줄일 수 없을까?
        try:
            num = int(input("Enter number to restart factorial = "))
            break
        except ValueError:
            print("Please enter natural number.")
else:
    print("Factorial Ended.")
