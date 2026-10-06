
# Q8. Write a program to create a duplicate of an existing list. It should not point to same list. 

li = [10, 20, 30, 40, 50]

new_li = []

for val in li:

    new_li = new_li + [val]

print("Original List :", li)
print("Duplicate List :", new_li)
