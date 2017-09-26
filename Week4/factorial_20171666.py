# 재귀적으로 팩토리얼을 구현. trivial case 고려.


def factorial(n):
    if n == 0:  # trivial case 1.
        return 1
    elif n == 1:  # trivial case 2.
        return 1
    else:
        return factorial(n-1) * n

a = int(input("number : "))
print(factorial(a))

# End of factorial.


def ncr(alpha, beta):
    if beta == 0:
        return 1
    elif beta == alpha:
        return 1
    else:
        return ncr(alpha-1) * alpha // ncr(beta - 1) * beta * ncr(alpha - beta)

n = int(input("n : "))
r = int(input("r : "))
print(ncr(n, r))