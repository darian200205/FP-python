from Domain.Student import Student
from Domain.Subject import Subject

class InMemoryRepository:
    student_list = []
    subjects_list = []
    def __init__(self):
        pass
    def add_student(self, id_of_student, name_of_student):
        self.student_list.append(Student(id_of_student, name_of_student))
        for i in range(0, len(self.subjects_list)):
            self.student_list[len(self.student_list) - 1].grades.append([self.subjects_list[i].subject_id, "Media", 0, "Notele"])

    def add_subject(self, id_of_subject, name_of_subject, name_of_teacher):
        self.subjects_list.append(Subject(id_of_subject, name_of_subject, name_of_teacher))
        for i in range(0, len(self.student_list)):
            self.student_list[i].grades.append([id_of_subject, "Media", 0, "Notele"])