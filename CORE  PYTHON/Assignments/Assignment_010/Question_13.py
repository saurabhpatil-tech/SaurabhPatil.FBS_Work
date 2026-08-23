
# Q13. Write a program to print list after removing even numbers.

li = [22, 45, 90, 33, 72, 47, 70, 27, 80]

li2 = []

for i in li:

    if i % 2 != 0:
        li2 = li2 + [i]

print("Original List :",li)
print("After Remove even No :",li2)
