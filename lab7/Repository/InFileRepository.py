from Repository.InMemoryRepository import InMemoryRepository
from Domain.Student import Student
from Domain.Subject import Subject

import os
import pickle


#  import json


class InFileRepository(InMemoryRepository):

    def __init__(self):
        #  super().__init__()
        # updating students list
        if os.path.isfile("studentList.pickle"):
            with open("studentList.pickle", "rb") as handler:
                while 1:
                    try:
                        self._student_list.append(pickle.load(handler))
                    except EOFError:
                        break
        # updating subjects list
        if os.path.isfile("subjectList.pickle"):
            with open("subjectList.pickle", "rb") as handler:
                while 1:
                    try:
                        self._subjects_list.append(pickle.load(handler))
                    except EOFError:
                        break

    def add_student(self, student_id, student_name):
        super().add_student(student_id, student_name)  # adds students in memory
        if os.path.isfile("studentList.pickle"):
            with open("studentList.pickle", "ab") as handler:
                pickle.dump(Student(student_id, student_name), handler, protocol=pickle.HIGHEST_PROTOCOL)
        else:
            with open("studentList.pickle", "wb") as handler:
                pickle.dump(Student(student_id, student_name), handler, protocol=pickle.HIGHEST_PROTOCOL)

    def add_subject(self, subject_id, subject_name, teacher_name):
        super().add_subject(subject_id, subject_name, teacher_name)  # adds subject in memory
        if os.path.isfile("subjectList.pickle"):
            with open("subjectList.pickle", "ab") as handler:
                pickle.dump(Subject(subject_id, subject_name, teacher_name), handler, protocol=pickle.HIGHEST_PROTOCOL)
        else:
            with open("subjectList.pickle", "wb") as handler:
                pickle.dump(Subject(subject_id, subject_name, teacher_name), handler, protocol=pickle.HIGHEST_PROTOCOL)
        self.update_student_list()

    def delete_student(self, student_name):
        super().delete_student(student_name)
        self.update_student_list()

    def delete_subject(self, subject_to_delete):
        super().delete_subject(subject_to_delete)
        self.update_subject_list()
        self.update_student_list()

    def grade_student(self, grade_, id_of_student, id_of_subject):
        super().grade_student(grade_, id_of_student, id_of_subject)
        self.update_student_list()

    def update_student_list(self):
        with open("studentList.pickle", "wb") as handler:
            for student in super()._student_list:
                updated_student = Student(student.student_id, student.student_name)
                updated_student.grades = student.grades
                pickle.dump(updated_student, handler, protocol=pickle.HIGHEST_PROTOCOL)

    def update_subject_list(self):
        with open("subjectList.pickle", "wb") as handler:
            for subject in super()._subjects_list:
                updated_subject = Subject(subject.subject_id, subject.subject_name, subject.teacher)
                pickle.dump(updated_subject, handler, protocol=pickle.HIGHEST_PROTOCOL)
