

my_list = ["salut", "ce", "faci"]

with open("test.txt", "w") as file:
    for element in my_list:
        file.write(element + "\n")

with open("test.txt", "r") as file:
    ans = file.read()
    print(ans)
