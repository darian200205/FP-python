import math


def right_operation(operation1, operation2):
    good = False
    while not good:
        try:
            task = int(input("Introduceti un numar:"))
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
    for it in range(len(array), i, -1):
        array[i] = array[i - 1]


def delete_elements(i, j, array):
    for it in range(i, j):
        array.remove(array[it])


def _replace(replaced_real, replaced_imaginary, new_real, new_imaginary, array):
    for it in array:
        if replaced_real == new_real and replaced_imaginary == new_imaginary:
            it[0] = new_real
            it[1] = newImaginary
            it[2] = int(math.sqrt(new_real * new_real + new_imaginary * new_imaginary))


def output_list(array):
    for it in range(len(array)):
        print(array[it], end=" ")


if __name__ == '__main__':

    menu = {'1': "Adaugă număr în listă. ", '2': "Modifică elemente din listă. ", '3': "Căutare numere. ",
            '4': "Operații cu numerele din listă ", '5': "Filtrare. ", '6': "Undo "}

    _continue = True
    list = []
    while _continue:
        _continue = False

        for options in menu:
            print(options, end=" ")
            print(menu[options])

        _selected = right_operation(1, 6)
        if _selected == 1:
            num1, num2 = map(int, input("Introdu a si b").split())
            print("1 Adaugă număr complex la sfârșitul listei")
            print("2 Inserare număr complex pe o poziție dată")
            _selected = right_operation(1, 2)
            module = int(math.sqrt(num1 * num1 + num2 * num2))
            if _selected == 1:
                list.append(num1, num2, module)
            else:
                position = right_operation(0, len(list) - 1)
                move_elements(position, list)
                list[position].append(num1, num2, module)
                output_list(list)

        if _selected == 2:
            print("Care este urmatoarea operatie?")
            print("1 Șterge elementele de pe un interval de poziții.")
            print("2 Înlocuiește toate aparițiile unui număr complex cu un alt număr complex.")
            print("Introdu u numar:")
            _selected = right_operation(1, 2)
            if _selected == 1:
                pos1, pos2 = map(int, input("Introduceti pozitile separate printr-un space:").split())
                pos1 = right_operation(0, len(list) - 1)
                pos2 = right_operation(0, len(list) - 1)
                delete_elements(pos1, pos2, list)
                output_list(list)
            else:
                a, b = map(int, input("Introduceti numarul complex care doriti sa fie inlocuit").split())
                x, y = map(int, input("Introduceti numarul complex care sa il inlocuiasca:").split())
                _replace(a, b, x, y, list)
                output_list(list)

        if _selected == 3:
            print("Care este urmatoarea operatie?")
            print("1 Tipărește partea imaginara pentru numerele din listă. Se dă intervalul de poziții (sub secvența).")
            print("2 Tipărește toate numerele complexe care au modulul mai mic decât 10")
            print("3 Tipareste toate numerele complexe care au modulul egal cu 10")
            print("Introdu u numar:")
            _selected = right_operation(1, 3)
            if _selected == 1:
                pos1, pos2 = map(int, input("Introduceti pozitile separate printr-un space:").split())
                pos1 = right_operation(0, len(list) - 1)
                pos2 = right_operation(0, len(list) - 1)
                for it in list:
                    print(it[1], end=" ")

    output_list(list)
