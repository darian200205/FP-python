from show_menus import show_search_menu
from Search import search_student, search_subject
from data_lists import subjects_list, student_list

def do_task_3():

    for i in show_search_menu:
        print(i)
    task = int(input("Introduceti numarul urmatoarei operatii si apasati enter:"))

    if task == 1:
        searched_student = input("Introduceti NUME + PRENUME studentului cautat exact cum acesta "
                                "e "
                                "inregistrat si "
                                "apasati enter:").upper()
        if search_student(searched_student, student_list) != -1:
            print("Studentul cautat este:")
            search_student(searched_student, student_list).show_students()
        else:
            print("Acest student nu a fost gasit!")


    if task == 2:
        searched_subject = input("Introduceti numele disciplinei exact cum aceasta e "
                                "inregistrata si apasati "
                                "enter:").upper()
        if search_subject(searched_subject, subjects_list) != -1:
            print("Disciplina cautata este:")
            search_subject(searched_subject, subjects_list).show_subjects()
        else:
            print("Aceasta disciplina nu e inregistrata")

