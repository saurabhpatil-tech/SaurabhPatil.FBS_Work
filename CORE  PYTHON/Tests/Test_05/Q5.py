# 5. Python Program to Find the Union of two Lists without
# using set concept.


list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

list3 = list1.copy()

for i in list2:
    if i not in list3:
        list3.append(i)

print("Union of two lists:", list3)