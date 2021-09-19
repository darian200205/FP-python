from data_lists import student_list
from show_menus import show_statistics
import math

def do_task_5():
    for i in show_statistics:
        print(i)

    task = int(input("Introduceti numarul urmatoarei operatii si apasati enter:"))

    if task == 1:
        sorted_students_by_name = sorted(student_list, key=lambda x: x.student_name, reverse=False)
        for i in sorted_students_by_name:
            i.show_students()

    elif task == 2:
        sort_by_subject = input("Introduceti ID-ul disciplinei:").upper()
        for i in range(0, len(student_list[0].grades)):
            if student_list[0].grades[i][0] == sort_by_subject:
                target = i

        sorted_students_by_average = sorted(student_list, key=lambda x: x.grades[target][2], reverse=True)
        for i in sorted_students_by_average:
            i.show_students()

    elif task == 3:
        for i in range(0, len(student_list)):
            student_list[i].average = student_list[i].calculate_average_grades()
        best_students = sorted(student_list, key=lambda x: x.average, reverse=True)
        number_of_students = 20 * len(student_list) / 100
        for i in range(0, math.ceil(number_of_students)):
            best_students[i].show_students()