from Domain.Student import Student

class UIRepresenter:


    def __init__(self):

        self.main_menu = [
                "1:Adauga",
                "2:Sterge",
                "3:Cautare",
                "4:Asignare de note",
                "5:Statistici",
                "6:Modifica",
                "7:Iesire"
                ]
        self.add_menu = [
        "1 - Adauga un student nou",
        "2 - Adauga o disciplina noua"
    ]

    def show_student_list(self, students):
        for i in students:
            i.show_students()

    def show_subject_list(self, subjects):
        for i in subjects:
            i.show_subjects()

    def show_menu(self):
        for i in self.main_menu:
            print(i)

    def show_add_menu(self):
        for i in self.add_menu:
            print(i)

    def get_task(self):
        task = int(input("Introduceti numarul urmatoarei operatii si apasati enter:"))
        return task

    def get_student_info(self):
        student_id = input("Introduceti ID-ul studentului si apasati enter:").upper()
        student_name = input("Introduceti: NUME + PRENUME student si apasati enter:").upper()
        student = [student_id, student_name]
        return student

    def get_subject_info(self):
        id_of_subject = input("Introduceti ID-ul disciplinei si apasati enter:").upper()
        subject_name = input("Introduceti numele disciplinei si apasati enter:").upper()
        teacher_name= input("Introduceti numele profesorului si apasati enter:").upper()
        subject = [id_of_subject, subject_name, teacher_name]
        return subject

    def show_error(self):
        print("Aceasta operatie nu se afla in meniu")
