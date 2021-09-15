from data_lists import subjects_list
from data_lists import student_list
from Student import Student
from Subject import Subject


def add_student_to_list(id_of_student, name_of_student):
    student_list.append(Student(id_of_student, name_of_student))
    for i in range(0, len(subjects_list)):
        student_list[len(student_list) - 1].grades.append([subjects_list[i].subject_id, "Media", 0, "Notele"])


def add_subject_to_list(id_of_subject, name_of_subject, name_of_teacher):
    subjects_list.append(Subject(id_of_subject, name_of_subject, name_of_teacher))
    for i in range(0, len(student_list)):
        student_list[i].grades.append([id_of_subject, "Media", 0, "Notele"])
