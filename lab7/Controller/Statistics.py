from Repository.InMemoryRepository import InMemoryRepository
from Domain.Student import Student

class Statistics:
    def __init__(self):
        self.memory_repository = InMemoryRepository()

    def sort_students_by_name(self):
        sorted_students_by_name = sorted(self.memory_repository.student_list, key=lambda x: x.student_name, reverse=False)
        return sorted_students_by_name

    def sort_by_subject_grades(self, target_subject):
        for student in range(0, len(self.memory_repository.student_list[0].grades)):
            if self.memory_repository.student_list[0].grades[student][0] == target_subject:
                target = student

        sorted_students_by_average = sorted(self.memory_repository.student_list, key=lambda x: x.grades[target][2], reverse=True)
        return sorted_students_by_average

    def sort_by_average(self):
        for student in range(0, len(self.memory_repository.student_list)):
            self.memory_repository.student_list[student].average = self.memory_repository.student_list[student].calculate_average_grades()
        best_students = sorted(self.memory_repository.student_list, key=lambda x: x.average, reverse=True)
        number_of_students = 20 * len(self.memory_repository.student_list) / 100
        return [best_students, number_of_students]