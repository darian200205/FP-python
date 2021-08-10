class ComplexNumber:
    def __init__(self, a, b):
        self.__nr = [a, b]

    def getRealNumber(self):
        return self.__nr[0]

    def getImaginaryNumber(self):
        return self.__nr[1]


def right_operation(operation1, operation2):
    good = False
    while not good:
        try:
            task = int(input("Introduceti un numar:"))
            good = True
        except ValueError:
            print("Trebuie sa fie numerica")
            good = False
        if good:
            if operation1 <= task <= operation2:
                return task
            else:
                good = not good



if __name__ == '__main__':

    menu = []
    menu['1'] = "Adaugă un scor la un participant."
    menu['2'] = "Modificare scor."
    menu['3'] = "Tipărește lista de participanți."
    menu['4'] = "Operații pe un subset de participanți."
    menu['5'] = "Filtrare."
    menu['6'] = "Undo"

    _continue = True
    list = []
    while _continue:
        _continue = False

        for options in menu:
            print(options, end=" ")
            print(menu[options])

        _selected = right_operation(1, 6)
        if _selected == 1:
            num1, num2 = map(int, input("Introdu a si b").split())
            print("1 Adaugă număr complex la sfârșitul listei")
            print("2 Inserare număr complex pe o poziție dată")
            _selected = right_operation(1, 2)
            if _selected == 1:
                list.append(ComplexNumber(num1, num2))
            else:












