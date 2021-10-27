from Domain.Student import Student
from Repository.InMemoryRepository import InMemoryRepository
import pickle
import os

empty_list = []

if os.path.isfile("another_test1.pickle"):
    print("it exists!")
else:
    print("the file does not exist!")

quit()

with open("another_test1.pickle", "wb") as handler:
    pickle.dump("", handler)

file_size = os.path.getsize("another_test.pickle")
print(str(file_size))
quit()

print(ans)
quit()

my_list = []

with open("test.pickle", "rb") as handler:
    while 1:
        try:
            my_list.append(pickle.load(handler))
        except EOFError:
            break

print(my_list)
quit()

for i in my_list:
    i.show_students()
