from data_lists import student_list, subjects_list

def modify_student(modify_what, student_to_modify):
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


def modify_subject(modify_what, subject_to_modify):
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