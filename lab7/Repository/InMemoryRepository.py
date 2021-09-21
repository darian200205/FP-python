from Domain.Student import Student
from Domain.Subject import Subject
from UI.UI_Representer import UIRepresenter


class InMemoryRepository:
    student_list = []
    subjects_list = []

    def __init__(self):
        self.ui_representer = UIRepresenter()

    def add_student(self, id_of_student, name_of_student):
        self.student_list.append(Student(id_of_student, name_of_student))
        for i in range(0, len(self.subjects_list)):
            self.student_list[len(self.student_list) - 1].grades.append(
                [self.subjects_list[i].subject_id, "Media", 0, "Notele"])

    def add_subject(self, id_of_subject, name_of_subject, name_of_teacher):
        self.subjects_list.append(Subject(id_of_subject, name_of_subject, name_of_teacher))
        for i in range(0, len(self.student_list)):
            self.student_list[i].grades.append([id_of_subject, "Media", 0, "Notele"])

    def delete_student(self, student_name):
        for i in self.student_list:
            if i.student_name == student_name:
                self.student_list.remove(i)

    def delete_subject(self, subject_to_delete):
        for i in self.subjects_list:
            if i.subject_name == subject_to_delete:
                self.subjects_list.remove(i)

    def grade_student(self, grade_, id_of_student, id_of_subject):
        for student in range(0, len(self.student_list)):
            if self.student_list[student].student_id == id_of_student:
                for grade in range(0, len(self.student_list[student].grades)):
                    if self.student_list[student].grades[grade][0] == id_of_subject:
                        self.student_list[student].grades[grade].append(grade_)
                        self.student_list[student].grades[grade][2] += grade_
                        self.student_list[student].grades[grade][2] = self.student_list[student].grades[grade][2] / (
                                len(self.student_list[student].grades[grade]) - 4)
                        break

    def modify_student(self, modify_what, target_student):
        if modify_what == "NUME":
            new_name = self.ui_representer.get_student_name()
            for student in range(0, len(self.student_list)):
                if self.student_list[student].student_name == target_student:
                    self.student_list[student].student_name = new_name

        elif modify_what == "ID":
            new_id = self.ui_representer.get_student_id()
            for student in range(0, len(self.student_list)):
                if self.student_list[student].student_name == target_student:
                    self.student_list[student].student_id = new_id

        else:
            self.ui_representer.show_error()

    def modify_subject(self, modify_what, target_subject):
        if modify_what == "NUME":
            new_name = self.ui_representer.get_subject_name()
            for i in range(0, len(self.subjects_list)):
                if self.subjects_list[i].subject_id == target_subject:
                    self.subjects_list[i].subject_name = new_name

        elif modify_what == "ID":
            new_id = self.ui_representer.get_subject_id()
            for i in range(0, len(self.subjects_list)):
                if self.subjects_list[i].subject_id == target_subject:
                    self.subjects_list[i].subject_id = new_id

        elif modify_what == "PROFESOR":
            new_teacher = self.ui_representer.get_teacher_name()
            for i in range(0, len(self.subjects_list)):
                if self.subjects_list[i].subject_id == target_subject:
                    self.subjects_list[i].teacher = new_teacher

        else:
            self.ui_representer.show_error()
