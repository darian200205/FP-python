from Add import add_student_to_list, add_subject_to_list
from show_menus import show_menu, show_search_menu, show_add_menu, show_delete_menu, show_modify_menu, show_statistics
from data_lists import student_list, subjects_list

from task_1 import do_task_1
from task_2 import do_task_2
from task_3 import do_task_3
from task_4 import do_task_4
from task_5 import do_task_5
from task_6 import do_task_6





do_task= {
    1: do_task_1,
    2: do_task_2,
    3: do_task_3,
    4: do_task_4,
    5: do_task_5,
    6: do_task_6,
}

if __name__ == '__main__':
    while True:
        for i in show_menu:
            print(i)
        task = int(input("Introduceti numarul urmatoarei operatii si apasati enter:"))

        do_task[task]()

        print('\n')
        for i in student_list:
            i.show_students()
        for i in subjects_list:
            i.show_subjects()
