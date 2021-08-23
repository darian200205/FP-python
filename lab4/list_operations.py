def move_elements(i, array):
    array.append(array[len(array) - 1])
    for i in range(len(array) - 2, i, -1):
        array[i] = array[i - 1]
    array.remove(array[len(array) - 1])


def delete_elements(i, j, array):
    for el in range(i, j + 1):
        array.remove(array[el])


def _replace(replaced_real, replaced_imaginary, new_real, new_imaginary, array):
    for i in array:
        if i[0] == replaced_real and i[1] == replaced_imaginary:
            i[0] = new_real
            i[1] = new_imaginary
            i[2] = int(math.sqrt(new_real * new_real + new_imaginary * new_imaginary))


def _sum(start, end, array):
    sum_real = 0
    sum_imaginary = 0
    if end is not len(array):
        end += 1
    for i in range(start, end):
        sum_real += array[i][0]
        sum_imaginary += array[i][1]

    print(sum_real, end=" ")
    print(sum_imaginary)


def product(start, end, array, res_real, res_imaginary):
    prod_real = prod_imaginary = 0
    real = imaginary = 0

    for i in range(start, end + 1):
        if i == start:
            real = array[i][0]
            imaginary = array[i][1]
        else:
            prod_real += array[i][0] * real - imaginary * array[i][1]
            prod_imaginary += real * array[i][1] + imaginary * array[i][0]
            real = prod_real
            imaginary = prod_imaginary

    res_real = prod_real
    res_imaginary = prod_imaginary


def sort_descending_imaginary(array):
    array.sort(key=lambda tup: tup[1])
    array.reverse()
