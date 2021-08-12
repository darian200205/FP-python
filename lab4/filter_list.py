def is_prime(num):
    if num == 1:
        return 0
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return 0
    return 1


def filter_real_numbers(array):
    for i in range(0, len(array)-1):
        if is_prime(array[i][0]):
            array.remove(array[i])


def filter_module(array, target, operator):
    for i in range(0, len(array)-1):
        if operator == 1 and array[i][2] < target:
            array.remove(array[i])
        elif operator == 2 and array[i][2] == target:
            array.remove(array[i])
        elif operator == 3 and array[i][2] > target:
            array.remove(array[i])