from Add import add_student_to_list, add_subject_to_list
from show_menus import show_add_menu

def do_task_1():
    for i in show_add_menu:
        print(i)
    task = int(input("Introduceti numarul urmatoarei operatii si apasati enter:"))

    if task == 1:
        id_of_student = input("Introduceti ID-ul studentului si apasati enter:")
        name_of_student = input("Introduceti: NUME + PRENUME student si apasati enter:")
        add_student_to_list(id_of_student, name_of_student)

    elif task == 2:
        id_of_subject = input("Introduceti ID-ul disciplinei si apasati enter:").upper()
        name_of_subject = input("Introduceti numele disciplinei si apasati enter:").upper()
        name_of_teacher = input("Introduceti numele profesorului si apasati enter:").upper()
        add_subject_to_list(id_of_subject, name_of_subject, name_of_teacher)