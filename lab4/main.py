import math


def right_operation(operation1, operation2, text):
    good = False
    while not good:
        try:
            task = int(input(text))
            good = True
        except ValueError:
            print("Trebuie sa fie numerica")
            good = False
        if good:
            if operation1 <= task <= operation2:
                return task
            else:
                good = not good


def move_elements(i, array):
    array.append(array[len(array)-1])
    for it in range(len(array)-2, i, -1):
        array[it] = array[it-1]
    array.remove(array[len(array)-1])


def delete_elements(i, j, array):
    for it in range(i, j+1):
        array.remove(array[it])


def _replace(replaced_real, replaced_imaginary, new_real, new_imaginary, array):
    for it in array:
        if it[0] == replaced_real and it[1] == replaced_imaginary:
            it[0] = new_real
            it[1] = new_imaginary
            it[2] = int(math.sqrt(new_real * new_real + new_imaginary * new_imaginary))

def sum(start, end, array):
    sum_real = 0
    sum_imaginary = 0
    if end is not len(array):
        end += 1
    for it in range(start, end):
        sum_real += it[0]
        sum_imaginary += it[1]

    print(sum_real, end=" ")
    print(sum_imaginary)

def product(start, end, array):
    real=1
    imaginary = 1
    prod = 1
    i_power = 1
    prod_real = 1
    prod_imaginary = 1

    for it in array:
        if it == 0:
            real = it[0]
            imaginary = it[1]
        else:
            prod_real += it[0]*real - imaginary*it[1]
            prod_imaginary += real*it[1] + imaginary*it[0]
            real = prod_real
            imaginary = prod_imaginary

    print(prod_real, end=" ")
    print(prod_imaginary, end=" ")

def sort_descending_imaginary(array):
    array.sort(key=lambda tup:tup[1])
    array.reverse()
    print(array)






def output_list(array):
    for it in range(len(array)-1):
        print(array[it], end=" ")


if __name__ == '__main__':

    menu = {'1': "Adaugă număr în listă. ", '2': "Modifică elemente din listă. ", '3': "Căutare numere. ",
            '4': "Operații cu numerele din listă ", '5': "Filtrare. ", '6': "Undo ", '7': "Iesire"}

    list = []
    while True:

        for options in menu:
            print(options, end=" ")
            print(menu[options])

        _selected = right_operation(1, 7, "Introdu un numar:")
        if _selected == 1:
            num1, num2 = map(int, input("Introdu a si b:").split())
            print("1 Adaugă număr complex la sfârșitul listei")
            print("2 Inserare număr complex pe o poziție dată")
            _selected = right_operation(1, 2, "Introdu 1 sau 2:")
            module = int(math.sqrt(num1 * num1 + num2 * num2))
            power_of_i = 1
            if _selected == 1:
                list.append([num1, num2, module, power])
            else:
                position = right_operation(0, len(list), "Introdu pozitia:")
                if position == 0 and len(list) == 0:
                    list.append([num1, num2, module, power_of_i])
                else:
                    move_elements(position, list)
                    list.insert(position, [num1, num2, module, power_of_i])
            print(list)

        elif _selected == 2:
            print("Care este urmatoarea operatie?")
            print("1 Șterge elementele de pe un interval de poziții.")
            print("2 Înlocuiește toate aparițiile unui număr complex cu un alt număr complex.")
            _selected = right_operation(1, 2, "Introdu operatia:")
            if _selected == 1:
                pos1 = right_operation(0, len(list), "Introdu prima pozitie:")
                pos2 = right_operation(0, len(list), "Introdu a doua pozitie:")
                delete_elements(pos1, pos2, list)
            else:
                a, b = map(int, input("Introduceti numarul complex care doriti sa fie inlocuit:").split())
                x, y = map(int, input("Introduceti numarul complex care sa il inlocuiasca:").split())
                _replace(a, b, x, y, list)
            print(list)

        elif _selected == 3:
            print("Care este urmatoarea operatie?")
            print("1 Tipărește partea imaginara pentru numerele din listă. Se dă intervalul de poziții (sub secvența).")
            print("2 Tipărește toate numerele complexe care au modulul mai mic decât 10")
            print("3 Tipareste toate numerele complexe care au modulul egal cu 10")
            _selected = right_operation(1, 3, "Introdu operatia:")
            if _selected == 1:
                pos1 = right_operation(0, len(list), "Introdu prima pozitie:")
                pos2 = right_operation(0, len(list), "Introdu a doua pozitie:")
                for it in range(pos1, pos2+1):
                    print(list[it], end=" ")
            elif _selected == 2:
                cnt = 0
                for it in list:
                    if it[2] < 10:
                        print(list[cnt], end=" ")
                    cnt += 1
            elif _selected == 3:
                cnt = 0
                for it in list:
                    if it[2] == 10:
                        print(list[cnt], end=" ")
                    cnt += 1

        elif _selected == 4:
            print("1 suma numerelor dintr-o subsecventă dată:")
            print("2 Produsul numerelor dintr-o subsecventă dată:")
            print("3 Tipărește lista sortată descrescător după partea imaginara:")
            _selected = right_operation(1, 3, "Alegeti urmatoarea operatie:")
            if _selected ==  1 or _selected == 2:
                pos1 = right_operation(0, len(list), "Introdu prima pozitie:")
                pos2 = right_operation(0, len(list), "Introdu a doua pozitie:")
                if _selected == 1:
                    sum(pos1, pos2, list)
                else:
                    product(pos1, pos2, list)
            elif _selected == 3:





        elif _selected == 7:
            quit()

    output_list(list)
