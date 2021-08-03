import math
import datetime


def isPrime(num):
    if n == 1:
        return 0
    for i in range(2, math.sqrt(num) + 1):
        if num % i == 0:
            return 0
    return 1

def firstPrime(num):
    ans = num + 1
    while isPrime(ans) == 0:
        ans = ans + 1
    return ans

def age(Day, Month, Year):
    curr = datetime.datetime.now()
    ans = 0
    ans += (curr.year - Year - 1) * 365
    ans += (curr.month * 30) + curr.day
    ans += (30 - Day) + (12 - Month) * 30
    return ans


if __name__ == '__main__':
    task = int(input())
    if task == 1:
        number = int(input())
        print(firstPrime(num))
    elif task == 2:
        Day = int(input())
        Month = int(input())
        Year = int(input())
        print(age(Day, Month, Year))





