
# Q4. Python Program to Find the Second Largest Number in a List Using Bubble Sort.

li = [10, 55, 35, 95, 75, 40]

size = len(li)

for i in range (1,size):
    for j in range(0,size - i):
        if (li[j] > li[j + 1]):
            li[j] , li[j+1] = li[j+1] , li[j]

res = li[-2]

print("Sorted list :",li)
print("Second largest No :",res)