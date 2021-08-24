import math

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def filter_real_numbers(array):
    for i in array:
        if is_prime(i[0]):
            array.remove(i)


def filter_module(array, target, operator):
    for i in array:
        if operator == 1 and i[2] < target:
            array.remove(i)
        elif operator == 2 and i[2] == target:
            array.remove(i)
        elif operator == 3 and i[2] > target:
            array.remove(i)