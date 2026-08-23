
# Q2. Write a program to find maximum and minimum element in a list.

li = [50, 70, 25, 88, 10, 95, 60]

max = li[0]
min = li[0]

for num in li:

    if num > max:
        max = num

    if num < min:
        min = num

print("Maximum Number :",max)
print("Minimum Number :",min)

