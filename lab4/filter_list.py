import math


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def filter_real_numbers(array):
    i = 0
    while i < len(array):
        if is_prime(array[i].real):
            array.remove(array[i])
        else:
            i += 1


def filter_module(array, target, operator):
    i = 0
    while i < len(array):
        if operator == 1 and array[i].module < target:
            array.remove(i)
        elif operator == 2 and array[i].module == target:
            array.remove(i)
        elif operator == 3 and array[i].module > target:
            array.remove(i)
        else:
            i += 1