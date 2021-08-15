from user_menu import right_operation
from do_task import do_task_1, do_task_2, do_task_3, do_task_4, do_task_5


if __name__ == '__main__':
    menu = {'1': "Adaugă număr în listă. ", '2': "Modifică elemente din listă. ", '3': "Căutare numere. ",
            '4': "Operații cu numerele din listă ", '5': "Filtrare. ", '6': "Iesire "}

    list = []
    aux = []
    while True:

        for options in menu:
            print(options, end=" ")
            print(menu[options])

        _selected = right_operation(1, 6, "Introdu un numar:")
        if _selected == 1:
            do_task_1(list)

        elif _selected == 2:
            do_task_2(list)

        elif _selected == 3:
            do_task_3(list)

        elif _selected == 4:
            do_task_4(list)

        elif _selected == 5:
            do_task_5(list)

        elif _selected == 6:
            quit(list)
