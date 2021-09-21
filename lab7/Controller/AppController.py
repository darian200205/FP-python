from UI.UI_Representer import UIRepresenter
from Repository.InMemoryRepository import InMemoryRepository
from Domain.Student import Student
from Domain.Subject import Subject


class AppController:

    def __init__(self):
        self.memory_representer = InMemoryRepository()
        self.ui_representer = UIRepresenter()

    def start(self):
        do_task = {
            1: self.task1,
            2: self.task2,
            3: self.task3,
            4: self.task4,
            5: self.task5,
            6: self.task6,
            7: quit,
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
        else:
            self.ui_representer.show_error()

    def task2(self):
        self.ui_representer.show_delete_menu()
        task = self.ui_representer.get_task()
        if task == 1:
            student_to_delete = self.ui_representer.get_student_info().upper()
            self.memory_representer.delete_student(student_to_delete[1])
        elif task == 2:
            subject_to_delete = self.ui_representer.get_subject_info()
            self.memory_representer.delete_subject(subject_to_delete[1])
        else:
            self.ui_representer.show_error()

    def task3(self):
        self.ui_representer.show_search_menu()
        task = self.ui_representer.get_task()

        if task == 1:
            searched_student = self.ui_representer.get_student_name()

            if self.search_student(searched_student, self.memory_representer.student_list) != -1:
                self.search_student(searched_student,
                                                       self.memory_representer.student_list).show_students()
            else:
                self.ui_representer.show_error()

        elif task == 2:
            searched_subject = self.ui_representer.get_subject_name()

            if self.search_subject(searched_subject, self.memory_representer.subjects_list) != -1:
                self.search_subject(searched_subject,
                                                       self.memory_representer.subjects_list).show_subjects()
            else:
                self.ui_representer.show_error()

    def task4(self):
        if not self.memory_representer.subjects_list:
            self.ui_representer.show_error()
        else:
            student_to_grade = self.ui_representer.get_student_id()
            while not self.student_exists(student_to_grade, self.memory_representer.student_list):
                self.ui_representer.show_error()
                student_to_grade = self.ui_representer.get_student_id()

            id_of_subject = self.ui_representer.get_subject_id()
            while not self.subject_exists(id_of_subject, self.memory_representer.subjects_list):
                self.ui_representer.show_error()
                id_of_subject = self.ui_representer.get_subject_id()

            grade = self.ui_representer.get_grade()
            if grade < 1 or grade > 10:
                self.ui_representer.show_error()
            else:
                self.memory_representer.grade_student(grade, student_to_grade, id_of_subject)

    def task5(self):
        self.ui_representer.show_statistics_menu()

        task = self.ui_representer.get_task()
        if task == 1:
            sorted_students_by_name = self.sort_students_by_name()
            self.ui_representer.show_student_list(sorted_students_by_name)

        elif task == 2:
            target_subject = self.ui_representer.get_subject_id()
            sorted_students_by_average = self.sort_by_subject_grades(target_subject)
            self.ui_representer.show_student_list(sorted_students_by_average)

        elif task == 3:
            best_students = self.sort_by_average()[0]
            number_of_students = self.sort_by_average()[1]
            self.ui_representer.show_best_students(best_students, number_of_students)

        else:
            self.ui_representer.show_error()

    def task6(self):
        self.ui_representer.show_modify_menu()
        task = self.ui_representer.get_task()

        if task == 1:
            student_to_modify = self.ui_representer.get_student_name()
            modify_what = self.ui_representer.get_answer()
            self.memory_representer.modify_student(modify_what, student_to_modify)

        elif task == 2:
            subject_to_modify = self.ui_representer.get_subject_id()
            modify_what = self.ui_representer.get_answer()
            self.memory_representer.modify_subject(modify_what, subject_to_modify)

        else:
            self.ui_representer.show_error()

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

    def sort_students_by_name(self):
        sorted_students_by_name = sorted(self.memory_representer.student_list, key=lambda x: x.student_name, reverse=False)
        return sorted_students_by_name

    def sort_by_subject_grades(self, target_subject):
        for student in range(0, len(self.memory_representer.student_list[0].grades)):
            if self.memory_representer.student_list[0].grades[student][0] == target_subject:
                target = student

        sorted_students_by_average = sorted(self.memory_representer.student_list, key=lambda x: x.grades[target][2], reverse=True)
        return sorted_students_by_average

    def sort_by_average(self):
        for student in range(0, len(self.memory_representer.student_list)):
            self.memory_representer.student_list[student].average = self.memory_representer.student_list[student].calculate_average_grades()
        best_students = sorted(self.memory_representer.student_list, key=lambda x: x.average, reverse=True)
        number_of_students = 20 * len(self.memory_representer.student_list) / 100
        return [best_students, number_of_students]
