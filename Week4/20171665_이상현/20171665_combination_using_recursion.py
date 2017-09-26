def combi(n, m):                        #recursion 을 이용한 combination 함수 작성.

    if m == 0 or n == m:
        return 1

    return combi(n-1, m-1) + combi(n-1, m)

while True:                             #무한 반복 프로그램 생성

    try:
        n = int(input("집합의 모든 원소의 갯수를 입력하세요: "))
        m = int(input("고르는 원소의 갯수를 입력하세요: "))
        if n < 0 or m < 0:                                          # 음수를 입력했을 때 사용자에게 프로그램 종료 의사를 물어봄
            end = input("종료하시겠습니까? (y/n): ")
            if end == 'y':
                break
            else:
                continue

        result = combi(n, m)

        print("%d 개의 원소를 가지는 집합에서 %d 개의 원소를 고르는 경우의 수는 %f 입니다." %(n, m, result))

    except ValueError:                      #정수 외의 다른 타입 입력 시 예외 처리
        print("정확한 값을 입력해주세요.")


