from data_lists import student_list, subjects_list
from Search import student_exists, subject_exists

def do_task_4():
    if not subjects_list:
        print("Deocamdata nu a fost inregistrata nicio disciplina!")
    else:
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
        if grade_ < 1 or grade_ > 10:
            print("Nota trebuie sa fie [1, 10]")
        else:
            for i in range(0, len(student_list)):
                if student_list[i].student_id == id_of_student:
                    for j in range(0, len(student_list[i].grades)):
                        if student_list[i].grades[j][0] == id_of_subject:
                            student_list[i].grades[j].append(grade_)
                            student_list[i].grades[j][2] += grade_
                            student_list[i].grades[j][2] = student_list[i].grades[j][2] / (
                                    len(student_list[i].grades[j]) - 4)
                            break