from Domain.Student import Student
from Domain.Subject import Subject


class SearchModule:

    def __init__(self):
        pass

    def search_student(self, searched_student, students):
        for student in students:
            if student.student_name == searched_student:
                return student
        return -1

    def search_subject(self, searched_subject, subjects):
        for subject in subjects:
            if subject.subject_name == searched_subject:
                return subject
        return -1

    def student_exists(self, current_id, students):
        for student in students:
            if student.student_id == current_id:
                return True
        return False

    def subject_exists(self, current_subject, subjects):
        for subject in subjects:
            if subject.subject_id == current_subject:
                return True
        return False
