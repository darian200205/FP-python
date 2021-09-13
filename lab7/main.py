class Student:
    def __init__(self, id, nume):
        self.id = id
        self.nume = nume

class Subject:
    def __init__(self, id, nume, profesor):
        self.id = id
        self.nume = nume
        self.profesor = profesor


show_menu = [
    "1 - Adauga",
    "2 - Sterge",
    "3 - Modifica",
    "4 - Cautare",
    "5 - Asignare note",
    "6 - Statistici"
]


student_list = []
subjects_list = []

if __name__ == '__main__':
    while True:
        for i in show_menu:
            print(i)
        while False:
            try:
                do_task = int(input("Introduceti un nr:"))
            except ValueError:
                print("Introduceti o valoare corecta")

        if do_task == 1:
            do_task = int(input("In care lista doriti sa adaugati?:"))
            print("1 - Elevi" + '\n' + "2 - Discipline")
            if do_task == 1:
                student_id = input("Introduceti ID-ul studentului si apasati enter:")
                student_name = input("Introduceti numele studentului si apasati enter:")
                student_list.append(Student(student_id, student_name))
            elif do_task == 2:
                subject_id = input("Introduceti ID-ul disciplinei si apasati enter:")
                subject_name = input("Introduceti numele disciplinei si apasati enter:")
                subject_teacher = input("Introduceti numele profesorului care preda disciplina si apasati enter:")
                subjects_list.append(Subject(subject_id, subject_name, subject_teacher))

        if do_task == 2:
            do_task = int(input("In care lista doriti sa stergeti?:"))
            print("1 - Elevi" + '\n' + "2 - Discipline")
            if do_task == 1:
                student_id = input("Introduceti ID-ul elevului pe care doriti sa il eliminati din lista si apasati enter:")
                if student_id in student_list:
                    for i in range(0, len(student_list)):
                        if student_list[i].id == student_id:
                            student_list.remove(student_list[i])
                            break
                else:
                    print("Acest student nu se afla in lista")

            elif do_task == 2:
                subject_id = input("Introduceti ID-ul disciplinei pe care doriti sa o eliminati din lista si apasati enter:")
                if subject_id in subjects_list:
                    for i in range(0, len(subjects_list)):
                        if subjects_list[i].id == subject_id:
                            subjects_list.remove(subjects_list[i])
                            break
                else:
                    print("Aceasta disciplina nu exista")


