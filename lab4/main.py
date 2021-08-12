import math
import sys
from user_menu import right_operation
from list_operations import _replace, move_elements, delete_elements
from list_operations import _sum, product, sort_descending_imaginary
from filter_list import filter_module, filter_real_numbers



if __name__ == '__main__':
    menu = {'1': "Adaugă număr în listă. ", '2': "Modifică elemente din listă. ", '3': "Căutare numere. ",
            '4': "Operații cu numerele din listă ", '5': "Filtrare. ", '6': "Undo ", '7': "Iesire"}

    list = []
    aux = []
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
            if _selected == 1:
                list.append([num1, num2, module])
            else:
                position = right_operation(0, len(list), "Introdu pozitia:")
                if position == 0 and len(list) == 0:
                    list.append([num1, num2, module])
                else:
                    move_elements(position, list)
                    list.insert(position, [num1, num2, module])
            print(list)

        elif _selected == 2:
            print("Care este urmatoarea operatie?")
            print("1 Șterge elementele de pe un interval de poziții.")
            print("2 Înlocuiește toate aparițiile unui număr complex cu un alt număr complex.")
            _selected = right_operation(1, 2, "Introdu operatia:")
            if _selected == 1:
                pos1 = right_operation(0, len(list) - 1, "Introdu prima pozitie:")
                pos2 = right_operation(0, len(list) - 1, "Introdu a doua pozitie:")
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
                pos1 = right_operation(0, len(list) - 1, "Introdu prima pozitie:")
                pos2 = right_operation(0, len(list) - 1, "Introdu a doua pozitie:")
                for it in range(pos1, pos2 + 1):
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
            if _selected == 1 or _selected == 2:
                pos1 = right_operation(0, len(list) - 1, "Introdu prima pozitie:")
                pos2 = right_operation(0, len(list) - 1, "Introdu a doua pozitie:")
                if _selected == 1:
                    _sum(pos1, pos2, list)
                else:
                    product(pos1, pos2, list)
            elif _selected == 3:
                aux = list.copy()
                sort_descending_imaginary(aux)

        elif _selected == 5:
            print("1 Filtrare parte reala prim – elimină din listă numerele complexe la care partea reala este prim.:")
            print("2 Filtrare modul – elimina din lista numerele complexe la care modulul este <,= sau > decât un număr dat.:")
            _selected = right_operation(1, 2, "Introduceti urmatoarea operatie:")
            if _selected == 1:
                filter_real_numbers(list)
            else:
                target = right_operation(0, sys.maxsize, "Introduceti numarul:")
                operator = right_operation(1, 3, "Introduceti 1 pt '<', 2 pentru '=' si 3 pentru '>':")
                filter_module(list, target, operator)
            print(list)

        elif _selected == 6:
            quit()
