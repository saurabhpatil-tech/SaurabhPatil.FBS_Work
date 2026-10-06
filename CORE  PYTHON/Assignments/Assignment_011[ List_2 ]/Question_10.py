
# Q10. Write a program to print list after removing even numbers.


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

li2 = []

for i in range(len(li)):

    if li[i] % 2 != 0:
        li2.append(li[i])

print("Original List :",li)
print("After Remove even No :",li2)