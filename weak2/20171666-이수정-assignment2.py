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
        num = int(input("Enter natural number to start factorial = "))
    except ValueError:
        print("Please enter natural number.")
        continue
    if num == -1:
        print("Factorial Ended.")
        break
    elif num >= 0:
        print(factorial(num))
    else:
        print("Please Enter number 0 or over to start factorial.")

"""
==========2ND WEEK HOMEWORK COMMENT============
++While TRUE 를 사용하지 않기 위하여 while NUM + 1: 를 사용하여 -1이 되는 경우를
else로 보내려고 했으나, -1 이하의 정수가 들어가는 경우에서 반복문을 끝내지 
않고 다시 입력받는 방법을 찾지 못했습니다. 5조의 다른 팀원의 코드를 참조하여
 최종코드를 완성했습니다.(while TRUE를 사용함.)
++try, except 구문으로 int 이외의 값이 입력된 경우를 걸러냈습니다.
++factorial은 함수로 처리하여 코드 맨 위에 작성하였습니다.
++다음번 코드리뷰에서는 모든 팀원의 사례를 더 자세히 살펴보고 논의하여 가장
이상적인 코드를 만들 수 있도록 하겠습니다. 
++감사합니다.
===============================================
"""
