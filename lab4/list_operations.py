import math


def move_elements(i, array):
    last = len(array) - 1
    array.append(array[last])
    for j in range(len(array) - 2, i, -1):
        array[j] = array[j - 1]
    array.remove(array[last])


def delete_elements(i, j, array):
    for el in range(i, j + 1):
        array.remove(array[el])


def _replace(replaced_real, replaced_imaginary, new_real, new_imaginary, array):
    for i in range(0, len(array)):
        if array[i].real == replaced_real and array[i].imaginary == replaced_imaginary:
            array[i].real = new_real
            array[i].imaginary = new_imaginary
            array[i].module = int(math.sqrt(new_real * new_real + new_imaginary * new_imaginary))


def sort_descending_imaginary(array):
    array.sort(key=lambda tup: tup.real)
    array.reverse()
