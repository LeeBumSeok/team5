def factorial(a):                       #factorial 함수 정의

    if a == 1 or a == 0:
        return 1
    else:
        return a*factorial(a-1)

while True:                             #무한 반복 프로그램 생성

    try:
        n = int(input("집합의 모든 원소의 갯수를 입력하세요: "))
        m = int(input("고르는 원소의 갯수를 입력하세요: "))
        if n < 0 or m < 0:                                  # 음수를 입력했을 때 사용자에게 프로그램 종료 의사를 물어봄.
            end = input("종료하시겠습니까? (y/n): ")
            if end == 'y':
                break
            else:
                continue
        elif n < m:
            print ("n보다 m이 더 큽니다. 다시 입력해주세요.")
            continue
        result = factorial(n) / (factorial(m) * factorial((n - m)))

        print("%d 개의 원소를 가지는 집합에서 %d 개의 원소를 고르는 경우의 수는 %d 입니다." %(n, m, result))

    except ValueError:                  #정수 외의 다른 타입 입력 시 예외 처리
        print("정확한 값을 입력해주세요.")

