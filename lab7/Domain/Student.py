class Student:

    def __init__(self, student_id, student_name):
        self.student_id = student_id.upper()
        self.student_name = student_name.upper()
        self.grades = []

    def show_students(self):
        print(str('ID:' + self.student_id) + ' ' + str(self.student_name) + ':' + str(self.grades))

    def calculate_average_grades(self):
        answer = 0
        for i in range(0, len(self.grades)):
            answer += self.grades[i][2]
        answer /= len(self.grades)
        return answer
