
# Q7. Write a program to create a new list from existing list which contain cube of each number of list.

li = [1, 2, 3, 4, 5, 6]

new_li = []

for val in li:

    cube = val ** 3
    new_li = new_li + [cube]


print("Original List :", li)
print("Cube of each number of list :",new_li)