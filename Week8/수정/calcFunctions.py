from math import factorial as fact


def calcFunctions(key, n):
    if key == 'factorial (!)':
        n = int(n)
        r = str(fact(n))
        return r
    if key == '-> binary':
        n = int(n)
        r = bin(n)[2:]
        return r
    if key == 'binary -> dec':
        n = int(n, 2)
        r = str(n)
        return r
    if key == '-> roman':
        return 'dec -> Roman'
