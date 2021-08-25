import math
import sys

from filter_list import filter_module, filter_real_numbers
from list_operations import _replace, move_elements, delete_elements
from list_operations import _sum, product, sort_descending_imaginary
from user_menu import right_operation


class Complex:
    def __init__(self, real, imaginary, module):
        self.real = real
        self.imaginary = imaginary
        self.module = module

    def show_numbers(self):
        print("[" + str(self.real) + "+" + str(self.imaginary) + "i" + "]", end="")

    def __add__(self, other):
        real_ans = self.real + other.real
        imaginary_ans = self.imaginary + other.imaginary
        return Complex(real_ans, imaginary_ans, int(math.sqrt(real_ans * real_ans + imaginary_ans * imaginary_ans)))

    def __mul__(self, other):
        real_ans = self.real * other.real - self.imaginary * other.imaginary
        imaginary_ans = self.imaginary * other.real + self.real * other.imaginary
        return Complex(real_ans, imaginary_ans, int(math.sqrt(real_ans * real_ans + imaginary_ans * imaginary_ans)))


def do_task_1(array):
    num1, num2 = map(int, input("Introdu a si b:").split())
    print("1 Adaugă număr complex la sfârșitul listei")
    print("2 Inserare număr complex pe o poziție dată")
    _next = right_operation(1, 2, "Introdu 1 sau 2:")
    module = int(math.sqrt(num1 * num1 + num2 * num2))
    if _next == 1:
        array.append(Complex(num1, num2, module))
    else:
        position = right_operation(0, len(array), "Introdu pozitia:")
        if position == 0 and len(array) == 0:
            array.append(Complex(num1, num2, module))
        else:
            move_elements(position, array)
            array.insert(position, Complex(num1, num2, module))

    for nums in array:
        nums.show_numbers()
    print('\n')


def do_task_2(array):
    print("Care este urmatoarea operatie?")
    print("1 Șterge elementele de pe un interval de poziții.")
    print("2 Înlocuiește toate aparițiile unui număr complex cu un alt număr complex.")
    _next = right_operation(1, 2, "Introdu operatia:")
    if _next == 1:
        pos1 = right_operation(0, len(array) - 1, "Introdu prima pozitie:")
        pos2 = right_operation(0, len(array) - 1, "Introdu a doua pozitie:")
        delete_elements(pos1, pos2, array)
    else:
        a, b = map(int, input("Introduceti numarul complex care doriti sa fie inlocuit:").split())
        x, y = map(int, input("Introduceti numarul complex care sa il inlocuiasca:").split())
        _replace(a, b, x, y, array)

    for nums in array:
        nums.show_numbers()
    print('\n')


def do_task_3(array):
    print("Care este urmatoarea operatie?")
    print("1 Tipărește partea imaginara pentru numerele din listă. Se dă intervalul de poziții (sub secvența).")
    print("2 Tipărește toate numerele complexe care au modulul mai mic decât 10")
    print("3 Tipareste toate numerele complexe care au modulul egal cu 10")
    _next = right_operation(1, 3, "Introdu operatia:")

    if _next == 1:
        pos1 = right_operation(0, len(array) - 1, "Introdu prima pozitie:")
        pos2 = right_operation(0, len(array) - 1, "Introdu a doua pozitie:")
        for it in range(pos1, pos2 + 1):
            print(array[it].imaginary, end=" ")
        print('\n')

    elif _next == 2:
        for it in array:
            if it.module < 10:
                it.show_numbers()
        print('\n')

    elif _next == 3:
        for it in array:
            if it.module == 10:
                it.show_numbers()
        print('\n')


def do_task_4(array):
    print("1 suma numerelor dintr-o subsecventă dată:")
    print("2 Produsul numerelor dintr-o subsecventă dată:")
    print("3 Tipărește lista sortată descrescător după partea imaginara:")
    _next = right_operation(1, 3, "Alegeti urmatoarea operatie:")

    if _next == 1 or _next == 2:
        pos1 = right_operation(0, len(array) - 1, "Introdu prima pozitie:")
        pos2 = right_operation(0, len(array) - 1, "Introdu a doua pozitie:")

        if _next == 1:
            add = Complex(0, 0, 0)
            for i in range(pos1, pos2 + 1):
                add.imaginary += array[i].imaginary
                add.real += array[i].real
            add.show_numbers()
            print('\n')

        else:
            multiply = Complex(array[pos1].real, array[pos1].imaginary, array[pos1].module)
            add = Complex(0, 0, 0)
            for i in range(pos1+1, pos2+1):
                multiply = multiply*array[i]
                add = add + multiply
            add.show_numbers()
            print('\n')

    elif _next == 3:
        aux = array.copy()
        sort_descending_imaginary(aux)
        print(aux)


def do_task_5(array):
    print("1 Filtrare parte reala prim – elimină din listă numerele complexe la care partea reala este prim.:")
    print("2 Filtrare modul – elimina din lista numerele complexe la care modulul este <,= sau > decât un număr dat.:")
    _next = right_operation(1, 2, "Introduceti urmatoarea operatie:")
    if _next == 1:
        filter_real_numbers(array)
    else:
        target = right_operation(0, sys.maxsize, "Introduceti numarul:")
        operator = right_operation(1, 3, "Introduceti 1 pt '<', 2 pentru '=' si 3 pentru '>':")
        filter_module(array, target, operator)
    print(array)
