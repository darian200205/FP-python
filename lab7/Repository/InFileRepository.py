from Repository.InMemoryRepository import InMemoryRepository
from Domain.Student import Student
from Domain.Subject import Subject

import os
import pickle


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
