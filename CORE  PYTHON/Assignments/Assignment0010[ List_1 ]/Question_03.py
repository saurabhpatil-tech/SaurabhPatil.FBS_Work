
# Q3. Write a program to find the second largest element in the list.

li = [50, 70, 25, 10, 95, 60]

max = li[0]
second = li[0]

for num in li:

    if num > max:
        second = max
        max = num

    elif num > second:
        second = num

print("Second largest Element :",second)


# method 2 --

# li.sort()
# res = li[-2]
# print("Second largest Element :",res)