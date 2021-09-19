from UI.UI_Representer import ui_representer
from Repository.InMemoryRepository import InMemoryRepository
from Domain.Student import Student

class AppController:


    def __init__(self, ui_representer, InMemoryRepository):
        self.memory_representer = InMemoryRepository()
        self.ui_representer = ui_representer(InMemoryRepository)

    def start(self):
        do_task = {
            1: self.task1,
            2: self.task2,
            3: self.task3,
            4: self.task4,
            5: self.task5,
            6: self.task6,
        }

        while True:
            self.ui_representer.show_menu()
            task = self.ui_representer.get_task()
            do_task[task]()
            self.ui_representer.show_student_list()
            self.ui_representer.show_subject_list()

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
        pass

    def task3(self):
        pass

    def task4(self):
        pass

    def task5(self):
        pass

    def task6(self):
        pass


