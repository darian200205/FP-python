class Subject:
    def __init__(self, subject_id, subject_name, teacher):
        self.subject_id = subject_id.upper()
        self.subject_name = subject_name.upper()
        self.teacher = teacher.upper()

    def show_subjects(self):
        print(str('ID:' + self.subject_id) + ':' + str(self.subject_name) + '-' + str(self.teacher))
