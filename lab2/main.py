import math
import datetime


def isPrime(num):
    if num == 1:
        return 0
    for i in range(2, int(math.sqrt(num)) + 1):
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
    ans += (curr.year - Year - (curr.year != Year)) * 365
    ans += (curr.month * 30) + curr.day
    ans += (30 - Day) + (12 - Month) * 30
    return ans

def showDate(Year, xDay):
    Month =  int(xDay / 30) + (xDay % 30 != 0)
    if xDay > 30:
        xDay %= 30
    print(xDay, end = " ")
    print(Month, end = " ")
    print(Year)

def findPrimes(num):
    if isPrime(num - 2) == 1:
        print(2, end = " ")
        print(num - 2)
    else:
        for i in range(3, num - 1, 2):
            if isPrime(num - i):
                print(i, end = " ")
                print(num - i)
                break


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

    elif task == 3:
        Year = int(input())
        xDay = int(input())
        print(showDate(Year, xDay))

    elif task == 4:
        number = int(input())
        findPrimes(number)





