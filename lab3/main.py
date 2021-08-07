
def max_equal(arr):
    max_len = length = 1

    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            length += 1
        else:
            max_len = max(max_len, length)
            length = 1

    max_len = max(max_len, length)
    return max_len




def max_ascending(arr):
    max_len = length = 1

    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            length += 1
        else:
            max_len = max(max_len, length)
            length = 1
    max_len = max(max_len, length)
    return max_len

def go_next(question):
    right_operation = False
    while right_operation == False:
        try:
            selected = int(input(question))
            right_operation = True
        except ValueError:
            print("raspuns invalid, mai incearca")
            right_operation = False
        if right_operation == True:
            if selected != 0 and selected != 1:
                right_operation = False
            elif selected == 1:
                return True
            else:
                return False




if __name__ == '__main__':

    menu = {}
    menu['1'] = "Citirea unei liste de numere intregi"
    menu['2'] = " Gasirea secventelor de lungime maxima - toate elementele egale"
    menu['3'] = " Gasirea secventelor de lungime maxima - in ordine crescatoare"
    menu['4'] = "Iesire"

    while True:
        _continue = True
        while _continue == True:
            print("ce operatie doriti sa efectuati?")
            print("1", end=" ")
            print(menu['1'])
            print("2", end=" ")
            print(menu['4'])
            right_operation = False
            while right_operation == False:
                try:
                    selected = int(input("Introduceti un numar:"))
                    right_operation = True
                except ValueError:
                    print("Trebuie sa fie numerica")
                    right_operation = False
                if right_operation == True:
                    if selected != 1 and selected != 2:
                        right_operation = False


            if selected == 1:
                n = int(input("Introduceti numarul de elemente si apasati enter:"))
                arr = input("Introduceti " + str(n) + " numere separate printr-un enter:").split()



                _continue = True
                while _continue == True:
                    print("care este urmatoarea operatie?")
                    for options, item in menu.items():
                        if options == "1":
                            continue
                        print(options, end=" ")
                        print(menu[options])
                    right_operation = False
                    while right_operation == False:
                        try:
                            selected = int(input("Introduceti un numar:"))
                            right_operation = True
                        except ValueError:
                            print("Trebuie sa fie numerica")
                            right_operation = False
                        if right_operation == True:
                            if selected < 2 and selected > 4:
                                right_operation = False

                    if selected == 2:
                        print("Rezultatul este " + str(max_equal(arr)))
                        if go_next("Doriti sa mai efectuati alta operatie? Introduceti 1 pt DA sau 0 pt nu: ") == False:
                            _continue = False

                    elif selected == 3:
                        print("Rezultatul este " + str(max_ascending(arr)))
                        if go_next("Doriti sa mai efectuati alta operatie? Introduceti 1 pt DA sau 0 pt nu: ") == False:
                            _continue = False

                    else: quit()

                print("doriti sa va intoarceti la meniul principal? pentru a incerca un nou sir de numere")
                if go_next("Introduceti 1 pt DA sau 0 pt NU: ") == False:
                    _continue = False
                else:
                    _continue = True

            else: quit()







