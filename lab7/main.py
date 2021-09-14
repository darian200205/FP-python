show_menu = ["1: Adauga"
             "2: Sterge",
             "3:Cautare",
             "4:Asignare de note",
             "5:Statistici"
             ]


class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.grades = []

    def show_students(self):
        print(str(self.student_name) + ':' + str(self.grades))


class Subject:
    def __init__(self, subject_id, subject_name, teacher):
        self.subject_id = subject_id
        self.subject_name = subject_name
        self.teacher = teacher


student_list = []

if __name__ == '__main__':
    id_student = int(input("id student:"))
    name_student = input("name:")
    student_list.append(Student(id_student, name_student))

    subject_id = int(input("id-ul disciplinei:"))
    grade = input("introduceti nota:")
    student_to_grade = int(input("introduceti id-ul studentului:"))

    for i in range(0, len(student_list)):
        if student_list[i].student_id == student_to_grade:
            student_list[i].grades.append([subject_id, grade])
            break

    subject_id = int(input("id-ul disciplinei:"))
    grade = input("introduceti nota:")
    student_to_grade = int(input("introduceti id-ul studentului:"))

    for i in range(0, len(student_list)):
        if student_list[i].student_id == student_to_grade:
            exists = False
            for j in range(0, len(student_list[i].grades)):
                if student_list[i].grades[j][0] == subject_id:
                    exists = True
                    student_list[i].grades[j].append(grade)
                    break
            if not exists:
                student_list[i].grades.append([subject_id, grade])

    for i in student_list:
        i.show_students()
