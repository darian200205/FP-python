import copy
from do_task import do_task_1, do_task_2, do_task_3, do_task_4, do_task_5, Complex

list = []

if __name__ == '__main__':

    aux = []
    undo_array = []

    show_menu = [
        "1 Adauga numar in lista",
        "2 Modifică elemente din listă. ",
        "3 Căutare numere. ",
        "4 Operații cu numerele din listă ",
        "5 Filtrare. ",
        "6 Iesire ",
        "7 Undo"
    ]

    functionality_menu = {
        1: do_task_1,
        2: do_task_2,
        3: do_task_3,
        4: do_task_4,
        5: do_task_5,
        6: quit,
        7: print
    }

    while True:
        for options in range(0, len(show_menu)):
            print(show_menu[options])

        while True:
            key = int(input("Introdu un numar:"))
            if key in functionality_menu:
                break
            else:
                print("Gresit. Mai incearca!")

        if key == 6:
            quit()
        functionality_menu[key](list)
