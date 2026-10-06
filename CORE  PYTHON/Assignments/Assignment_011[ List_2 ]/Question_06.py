
# Q6. Python Program to Find the Union of two Lists.

li = [10, 20, 30, 40]
li2 = [30, 40, 50, 60]

res = list( set(li) | set(li2) )
# set() --> Remove Duplicate value
#  |  --> Combine Two sets 

print("Union of Two List :", res)