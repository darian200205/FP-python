from show_menus import show_modify_menu
from Modify import modify_student, modify_subject

def do_task_6():
    for i in show_modify_menu:
        print(i)
    task = int(input("Introduceti numarul urmatoarei operatii si apasati enter:"))

    if task == 1:
        student_to_modify = input(
            "Introduceti NUME+PRENUME studentului pe care doriti sa il modificati").upper()
        modify_what = input(
            "Ce doriti sa modificati?" + '\n' + "Tastati NUME pt a modifica numele" + '\n' + "Tastati ID pt a modifica ID-ul" + '\n' + "Apasati enter dupa:").upper()
        modify_student(modify_what, student_to_modify)

    elif task == 2:
        subject_to_modify = input("Tastati NUMELE sau ID-ul disciplinei care sa fie modificata si apasati "
                                  "enter:").upper()
        modify_what = input(
            "Ce doriti sa modificati?" + '\n' + "Tastati NUME pt a modifica numele" + '\n' + "Tastati ID pt a modifica ID-ul sau PROFESOR pentru a modifica profesorul" + '\n' + "Apasati enter dupa:").upper()

        modify_subject(modify_what, subject_to_modify)