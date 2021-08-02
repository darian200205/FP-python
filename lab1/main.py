import math


def sum(num):
    s = 0
    for i in range(num):
        s += i + 1
    return s


def isPrime(num):
    if num == 1:
        return 0
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return 0
    return 1


def gcd(num1, num2):
    while num2:
        r = num1 % num2
        num1 = num2
        num2 = r
    return num1


if __name__ == '__main__':
    print("1 pt suma a n numere")
    print("2 pt a verifica daca nr este prim")
    print("3 cmmdc a doua nre")
    x = int(input())
    if x == 1:
        n = int(input())
        print(sum(n))
    elif x == 2:
        n = int(input())
        print(isPrime(n))
    elif x == 3:
        print("introdu 2 numere")
        a, b = map(int, input().split())
        print(gcd(a, b))
