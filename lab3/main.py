
def maxEqual(arr, n):
    maxLen = Len = 1

    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            Len = Len + 1
        else:
            maxLen = max(maxLen, Len)
            Len = 1

    maxLen = max(maxLen, Len)
    return maxLen




def maxAscending(arr, n):
    maxLen = Len = 1

    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            Len = Len + 1
        else:
            maxLen = max(maxLen, Len)
            Len = 1
    maxLen = max(maxLen, Len)
    return maxLen




if __name__ == '__main__':

    menu = {}
    menu['1'] = "Citirea unei liste de numere intregi"
    menu['2'] = " Gasirea secventelor de lungime maxima - toate elementele egale"
    menu['3'] = " Gasirea secventelor de lungime maxima - in ordine crescatoare"
    menu['4'] = "Iesire"

    while True:
        for options in menu:
            print(options, end=" ")
            print(menu[options])

        selected = int(input("Introduceti un numar:"))

        if selected == 1:
            n = int(input())
            arr = []
            arr = input().split()
            selected = int(input("care este urmatoarea operatie:"))

            if selected == 2:
                print(maxEqual(arr, n))
                break

            elif selected == 3:
                print(maxAscending(arr, n))
                break

            else: quit()

        else: quit()







