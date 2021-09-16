from data_lists import student_list, subjects_list

def delete_student(student_to_delete):
    for i in student_list:
        if i.student_name == student_to_delete:
            student_list.remove(i)

def delete_subject(subject_to_delete):
    for i in subjects_list:
        if i.subject_name == subject_to_delete:
            subjects_list.remove(i)