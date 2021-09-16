from Add import add_student_to_list, add_subject_to_list
from show_menus import show_menu, show_search_menu, show_add_menu, show_delete_menu, show_modify_menu, show_statistics
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
                add_student_to_list(id_of_student, name_of_student)

            elif task == 2:
                id_of_subject = input("Introduceti ID-ul disciplinei si apasati enter:").upper()
                name_of_subject = input("Introduceti numele disciplinei si apasati enter:").upper()
                name_of_teacher = input("Introduceti numele profesorului si apasati enter:").upper()
                add_subject_to_list(id_of_subject, name_of_subject, name_of_teacher)

        elif task == 2:
            for i in show_delete_menu:
                print(i)

            task = int(input("Introduceti numarul urmatoarei operatii si apasati enter:"))
            if task == 1:
                student_to_delete = input(
                    "Introduceti NUME+PRENUME studentului care sa fie eliminat si apasati enter:").upper()
                for i in student_list:
                    if i.student_name == student_to_delete:
                        student_list.remove(i)

            elif task == 2:
                subject_to_delete = input(
                    "Introduceti numele disciplinei  care sa fie eliminata si apasati enter:").upper()
                for i in subjects_list:
                    if i.subject_name == subject_to_delete:
                        subjects_list.remove(i)

        elif task == 3:
            for i in show_search_menu:
                print(i)
            task = int(input("Introduceti numarul urmatoarei operatii si apasati enter:"))

            if task == 1:
                searched_student = input("Introduceti NUME + PRENUME studentului cautat exact cum acesta "
                                         "e "
                                         "inregistrat si "
                                         "apasati enter:").upper()
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
                searched_subject = input("Introduceti numele disciplinei exact cum aceasta e "
                                         "inregistrata si apasati "
                                         "enter:").upper()

                exists = False
                for i in subjects_list:
                    if i.subject_name == searched_subject:
                        exists = True
                        i.show_subjects()
                        break

                if not exists:
                    print("Aceasta disciplina nu e inregistrata")

        elif task == 4:
            id_of_student = input("Introduceti ID-ul studentului si apasati enter:").upper()
            while not student_exists(id_of_student):
                print("Acest student nu exista, mai incearca")
                id_of_student = input("Introduceti ID-ul studentului si apasati enter:")

            id_of_subject = input("Introduceti ID-ul disciplinei la care doriti sa adaugati o nota si apasati "
                                  "enter:").upper()
            while not subject_exists(id_of_subject):
                print("Aceasta disciplina nu a fost introdusa inca, mai incearca")
                id_of_subject = input("Introduceti ID-ul disciplinei la care doriti sa adaugati o nota si apasati "
                                      "enter:")

            grade_ = int(input("Introduceti nota obtinuta de catre student (de la 1 la 10) si apasati enter:"))

            for i in range(0, len(student_list)):
                if student_list[i].student_id == id_of_student:
                    for j in range(0, len(student_list[i].grades)):
                        if student_list[i].grades[j][0] == id_of_subject:
                            student_list[i].grades[j].append(grade_)
                            student_list[i].grades[j][2] += grade_
                            student_list[i].grades[j][2] = student_list[i].grades[j][2] / (
                                    len(student_list[i].grades[j]) - 4)
                            break

        elif task == 5:
            for i in show_statistics:
                print(i)

            task = int(input("Introduceti numarul urmatoarei operatii si apasati enter:"))

            if task == 1:
                sorted_students_by_name = sorted(student_list, key=lambda x: x.student_name, reverse=False)
                for i in sorted_students_by_name:
                    i.show_students()

            elif task == 2:
                sort_by_subject = input("Introduceti ID-ul disciplinei:").upper()
                for i in range(0, len(student_list[0].grades)):
                    if student_list[0].grades[i][0] == sort_by_subject:
                        target = i

                sorted_students_by_average = sorted(student_list, key=lambda x: x.grades[target][2], reverse=True)
                for i in sorted_students_by_average:
                    i.show_students()

            elif task == 3:
                for i in range(0, len(student_list)):
                    student_list[i].average = student_list[i].calculate_average_grades()
                best_students = sorted(student_list, key=lambda x: x.average, reverse=True)
                number_of_students = 20 * len(student_list) / 100
                for i in best_students:
                    i.show_students()

        elif task == 6:
            for i in show_modify_menu:
                print(i)
            task = int(input("Introduceti numarul urmatoarei operatii si apasati enter:"))

            if task == 1:
                student_to_modify = input(
                    "Introduceti NUME+PRENUME studentului pe care doriti sa il modificati").upper()
                modify_what = input(
                    "Ce doriti sa modificati?" + '\n' + "Tastati NUME pt a modifica numele" + '\n' + "Tastati ID pt a modifica ID-ul" + '\n' + "Apasati enter dupa:").upper()

                if modify_what == "NUME":
                    new_name = input("Introduceti noul nume, format NUME+PRENUME:").upper()
                    for i in range(0, len(student_list)):
                        if student_list[i].student_name == student_to_modify:
                            student_list[i].student_name = new_name

                elif modify_what == "ID":
                    new_id = input("Introduceti noul ID si apasati enter:").upper()
                    for i in range(0, len(student_list)):
                        if student_list[i].student_name == student_to_modify:
                            student_list[i].student_id = new_id

            elif task == 2:
                subject_to_modify = input("Tastati NUMELE sau ID-ul disciplinei care sa fie modificata si apasati "
                                          "enter:").upper()
                modify_what = input(
                    "Ce doriti sa modificati?" + '\n' + "Tastati NUME pt a modifica numele" + '\n' + "Tastati ID pt a modifica ID-ul sau PROFESOR pentru a modifica profesorul" + '\n' + "Apasati enter dupa:").upper()

                if modify_what == "NUME":
                    new_name = input("Introduceti noul nume al disciplinei:").upper()
                    for i in range(0, len(subjects_list)):
                        if subjects_list[i].subject_id == subject_to_modify or subjects_list[
                            i].subject_name == subject_to_modify:
                            subjects_list[i].subject_name = new_name

                elif modify_what == "ID":
                    new_id = input("Introduceti noul ID al disciplinei:").upper()
                    for i in range(0, len(subjects_list)):
                        if subjects_list[i].subject_id == subject_to_modify or subjects_list[
                            i].subject_name == subject_to_modify:
                            subjects_list[i].subject_id = new_id

                elif modify_what == "PROFESOR":
                    new_teacher = input("Introduceti numele profesorului:").upper()
                    for i in range(0, len(subjects_list)):
                        if subjects_list[i].subject_id == subject_to_modify or subjects_list[
                            i].subject_name == subject_to_modify:
                            subjects_list[i].teacher = new_teacher

        print('\n')
        for i in student_list:
            i.show_students()
        for i in subjects_list:
            i.show_subjects()
