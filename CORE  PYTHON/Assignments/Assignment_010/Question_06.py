
# Q6. Write a program to remove duplicates from the list.

li = [22, 45, 90, 33, 22, 45, 70, 22, 80]

new_li =[]

for val in li:

    if val not in new_li:
        new_li = new_li + [val]

print("Original List :", li)
print("List after removing duplicates :" , new_li)