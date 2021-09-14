from Student import Student
from Subject import Subject
from show_menus import show_menu, show_search_menu, show_add_menu
from data_lists import student_list, subjects_list


def student_exists(current_id):
    for it in range(0, len(student_list)):
        if student_list[it].student_id == current_id:
            return True
    return False


def subject_exists(current_subject):
    for it in range(0, len(subjects_list)):
        if subjects_list[it].subject_id == current_subject:
            return True
    return False


if __name__ == '__main__':
    while True:
        for i in show_menu:
            print(i)
        task = int(input("Introduceti numarul urmatoarei operatii si apasati enter:"))

        if task == 1:
            for i in show_add_menu:
                print(i)
            task = int(input("Introduceti numarul urmatoarei operatii si apasati enter:"))

            if task == 1:
                id_of_student = input("Introduceti ID-ul studentului si apasati enter:")
                name_of_student = input("Introduceti: NUME + PRENUME student si apasati enter:")
                student_list.append(Student(id_of_student, name_of_student))

            elif task == 2:
                id_of_subject = input("Introduceti ID-ul disciplinei si apasati enter:")
                name_of_subject = input("Introduceti numele disciplinei si apasati enter:")
                name_of_teacher = input("Introduceti numele profesorului si apasati enter:")
                subjects_list.append(Subject(id_of_subject, name_of_subject, name_of_teacher))

        elif task == 3:
            for i in show_search_menu:
                print(i)
            task = int(input("Introduceti numarul urmatoarei operatii si apasati enter:"))

            if task == 1:
                searched_student = input("Introduceti NUME + PRENUME studentului cautat cu majuscule exact cum acesta "
                                         "e "
                                         "inregistrat si "
                                         "apasati enter:")
                exists = False
                for i in student_list:
                    if i.student_name == searched_student:
                        exists = True
                        print("Studentul cauta este:")
                        i.show_students()
                        break

                if not exists:
                    print("Acest student nu e inregistrat")
                print('\n')

            if task == 2:
                searched_subject = input("Introduceti numele disciplinei cu majuscule exact cum aceasta e "
                                         "inregistrata si apasati "
                                         "enter:")

                exists = False
                for i in subjects_list:
                    if i.subject_name == searched_subject:
                        exists = True
                        i.show_subjects()
                        break

                if not exists:
                    print("Aceasta disciplina nu e inregistrata")

        elif task == 4:
            id_of_student = input("Introduceti ID-ul studentului si apasati enter:")
            while not student_exists(id_of_student):
                print("Acest student nu exista, mai incearca")
                id_of_student = input("Introduceti ID-ul studentului si apasati enter:")

            id_of_subject = input("Introduceti ID-ul disciplinei la care doriti sa adaugati o nota si apasati "
                                  "enter:")
            while not subject_exists(id_of_subject):
                print("Aceasta disciplina nu a fost introdusa inca, mai incearca")
                id_of_subject = input("Introduceti ID-ul disciplinei la care doriti sa adaugati o nota si apasati "
                                      "enter:")

            grade_ = int(input("Introduceti nota obtinuta de catre student (de la 1 la 10) si apasati enter:"))

            for i in range(0, len(student_list)):
                if student_list[i].student_id == id_of_student:
                    exists = False
                    for j in range(0, len(student_list[i].grades)):
                        if student_list[i].grades[j][0] == id_of_subject:
                            exists = True
                            student_list[i].grades[j].append(grade_)
                            break
                    if not exists:
                        student_list[i].grades.append([id_of_subject, grade_])

        for i in student_list:
            i.show_students()
        for i in subjects_list:
            i.show_subjects()
