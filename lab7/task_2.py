from show_menus import show_delete_menu
from Delete import delete_student, delete_subject

def do_task_2():
    for i in show_delete_menu:
        print(i)

    task = int(input("Introduceti numarul urmatoarei operatii si apasati enter:"))

    if task == 1:
        student_to_delete = input(
            "Introduceti NUME+PRENUME studentului care sa fie eliminat si apasati enter:").upper()
        delete_student(student_to_delete)

    elif task == 2:
        subject_to_delete = input(
            "Introduceti numele disciplinei  care sa fie eliminata si apasati enter:").upper()
        delete_subject(subject_to_delete)