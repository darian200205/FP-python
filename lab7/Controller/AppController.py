from UI.UI_Representer import UIRepresenter
from Repository.InMemoryRepository import InMemoryRepository
from Domain.Student import Student
from Domain.Subject import Subject
from Controller.Search import SearchModule

class AppController:


    def __init__(self, UIRepresenter, InMemoryRepository):
        self.memory_representer = InMemoryRepository()
        self.ui_representer = UIRepresenter()
        self.search_representer = SearchModule()



    def start(self):
        do_task = {
            1: self.task1,
            2: self.task2,
            3: self.task3,
            4: self.task4,
            5: self.task5,
            6: self.task6,
            7: self.task7,
        }

        while True:
            self.ui_representer.show_menu()
            task = self.ui_representer.get_task()

            if task in do_task:
                do_task[task]()
            else:
                self.ui_representer.show_error()
                continue

            self.ui_representer.show_student_list(self.memory_representer.student_list)
            self.ui_representer.show_subject_list(self.memory_representer.subjects_list)



    def task1(self):
        self.ui_representer.show_add_menu()
        task = self.ui_representer.get_task()
        if task == 1:
            student = self.ui_representer.get_student_info()
            self.memory_representer.add_student(student[0], student[1])
        elif task == 2:
            subject = self.ui_representer.get_subject_info()
            self.memory_representer.add_subject(subject[0], subject[1], subject[2])



    def task2(self):
        self.ui_representer.show_delete_menu()
        task = self.ui_representer.get_task()
        if task == 1:
            student_to_delete = self.ui_representer.get_student_info().upper()
            self.memory_representer.delete_student(student_to_delete[1])
        elif task == 2:
            subject_to_delete = self.ui_representer.get_subject_info()
            self.memory_representer.delete_subject(subject_to_delete[1])



    def task3(self):
        self.ui_representer.show_search_menu()
        task = self.ui_representer.get_task()

        if task == 1:
            searched_student = self.ui_representer.get_student_name()

            if self.search_representer.search_subject(searched_student, self.memory_representer.student_list) != -1:
                self.search_representer.search_student(searched_student, self.memory_representer.student_list).show_students()
            else:
                self.ui_representer.show_error()

        elif task == 2:
            searched_subject = self.ui_representer.get_subject_name()

            if self.search_representer.search_subject(searched_subject, self.memory_representer.subjects_list) != -1:
                self.search_representer.search_subject(searched_subject, self.memory_representer.subjects_list).show_subjects()
            else:
                self.ui_representer.show_error()



    def task4(self):
        if not self.memory_representer.subjects_list:
            self.ui_representer.show_error()
        else:
            student_to_grade = self.ui_representer.get_student_id()
            while not self.search_representer.student_exists(student_to_grade, self.memory_representer.student_list):
                self.ui_representer.show_error()
                student_to_grade = self.ui_representer.get_student_id()

            id_of_subject = self.ui_representer.get_subject_id()
            while not self.search_representer.subject_exists(id_of_subject, self.memory_representer.subjects_list):
                self.ui_representer.show_error()
                id_of_subject = self.ui_representer.get_subject_id()

            grade = self.ui_representer.get_grade()
            if grade < 1 or grade > 10:
                self.ui_representer.show_error()
            else:
                self.memory_representer.grade_student(grade, student_to_grade, id_of_subject)


    def task5(self):
        pass

    def task6(self):
        pass

    def task7(self):
        quit()

