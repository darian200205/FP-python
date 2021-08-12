def right_operation(operation1, operation2, text):
    good = False
    while not good:
        try:
            task = int(input(text))
            good = True
        except ValueError:
            print("Trebuie sa fie numerica")
            good = False
        if good:
            if operation1 <= task <= operation2:
                return task
            else:
                good = not good

