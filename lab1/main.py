import math

def sum(n):
    s = 0
    for i in range(n):
        s += i+1
    return s

def isPrime(n):
    if n == 1:
        return 0
    for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return 0
    return 1

def gcd(x, y):
    while y:
        r = x % y
        x = y
        y = r
    return x



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











