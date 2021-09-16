from data_lists import student_list, subjects_list

def search_student(searched_student, student_list):
    for i in student_list:
        if i.student_name == searched_student:
            return i
    return -1

def search_subject(searched_subject, subject_list):
    for i in subject_list:
        if i.subject_name == searched_subject:
            return i
    return -1

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
