from Domain.Student import Student
from Domain.Subject import Subject
from UI.UI_Representer import UIRepresenter


class InMemoryRepository:
    _student_list = []
    _subjects_list = []

    def __init__(self):
        self.ui_representer = UIRepresenter()
        """
        for student in range(len(self._student_list)):
            for subject in range(len(self._subjects_list)):
                self._student_list[student].grades.append(
                    [self._subjects_list[subject].subject_id, "Media", 0, "Notele"])
        """

    def get_student_list(self):
        return self._student_list

    def get_subject_list(self):
        return self._subjects_list

    def add_student(self, id_of_student, name_of_student):
        self._student_list.append(Student(id_of_student, name_of_student))
        for i in range(0, len(self._subjects_list)):
            self._student_list[len(self._student_list) - 1].grades.append(
                [self._subjects_list[i].subject_id, "Media", 0, "Notele"])

    def add_subject(self, id_of_subject, name_of_subject, name_of_teacher):
        self._subjects_list.append(Subject(id_of_subject, name_of_subject, name_of_teacher))
        for i in range(0, len(self._student_list)):
            self._student_list[i].grades.append([id_of_subject, "Media", 0, "Notele"])

    def delete_student(self, student_name):
        for i in self._student_list:
            if i.student_name == student_name:
                self._student_list.remove(i)

    def delete_subject(self, subject_to_delete):
        for i in self._subjects_list:
            if i.subject_id == subject_to_delete:
                self._subjects_list.remove(i)
                break
        for student in self._student_list:
            for grade in range(len(student.grades)):
                if student.grades[grade][0] == subject_to_delete:
                    student.grades.remove(student.grades[grade])
                    break

    def grade_student(self, grade_, id_of_student, id_of_subject):
        for student in range(len(self._student_list)):
            if self._student_list[student].student_id == id_of_student:
                for grade in range(len(self._student_list[student].grades)):
                    if self._student_list[student].grades[grade][0] == id_of_subject:
                        self._student_list[student].grades[grade].append(grade_)
                        self._student_list[student].grades[grade][2] += grade_
                        self._student_list[student].grades[grade][2] = self._student_list[student].grades[grade][
                                                                           2] / (
                                                                               len(self._student_list[student].grades[
                                                                                       grade]) - 4)
                        break

    def modify_student(self, modify_what, target_student):
        if modify_what == "NUME":
            new_name = self.ui_representer.get_student_name()
            for student in range(0, len(self._student_list)):
                if self._student_list[student].student_name == target_student:
                    self._student_list[student].student_name = new_name

        elif modify_what == "ID":
            new_id = self.ui_representer.get_student_id()
            for student in range(0, len(self._student_list)):
                if self._student_list[student].student_name == target_student:
                    self._student_list[student].student_id = new_id

        else:
            self.ui_representer.show_error()

    def modify_subject(self, modify_what, target_subject):
        if modify_what == "NUME":
            new_name = self.ui_representer.get_subject_name()
            for i in range(0, len(self._subjects_list)):
                if self._subjects_list[i].subject_id == target_subject:
                    self._subjects_list[i].subject_name = new_name

        elif modify_what == "ID":
            new_id = self.ui_representer.get_subject_id()
            for i in range(0, len(self._subjects_list)):
                if self._subjects_list[i].subject_id == target_subject:
                    self._subjects_list[i].subject_id = new_id

        elif modify_what == "PROFESOR":
            new_teacher = self.ui_representer.get_teacher_name()
            for i in range(0, len(self._subjects_list)):
                if self._subjects_list[i].subject_id == target_subject:
                    self._subjects_list[i].teacher = new_teacher

        else:
            self.ui_representer.show_error()

    def search_student(self, searched_student):
        for student in self._student_list:
            if student.student_name == searched_student:
                return student
        return -1

    def search_subject(self, searched_subject):
        for subject in self._subjects_list:
            if subject.subject_name == searched_subject:
                return subject
        return -1

    def student_exists(self, current_id, __student_list):
        for student in self._student_list:
            if student.student_id == current_id:
                return True
        return False

    def subject_exists(self, current_subject):
        for subject in self._subjects_list:
            if subject.subject_id == current_subject:
                return True
        return False

    def sort_students_by_name(self):
        sorted_students_by_name = sorted(self._student_list, key=lambda x: x.student_name, reverse=False)
        return sorted_students_by_name

    def sort_by_subject_grades(self, target_subject):
        for student in range(len(self._student_list[0].grades)):
            if self._student_list[0].grades[student][0] == target_subject:
                target = student

        sorted_students_by_average = sorted(self._student_list, key=lambda x: x.grades[target][2], reverse=True)
        return sorted_students_by_average

    def sort_by_average(self):
        for student in range(len(self._student_list)):
            self._student_list[student].average = self._student_list[student].calculate_average_grades()
        best_students = sorted(self._student_list, key=lambda x: x.average, reverse=True)
        number_of_students = 20 * len(self._student_list) / 100
        return [best_students, number_of_students]
