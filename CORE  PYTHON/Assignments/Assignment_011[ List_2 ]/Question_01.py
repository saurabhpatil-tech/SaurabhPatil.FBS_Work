
# Q1. Python program to put Even and Odd elements of a list into two different Lists.

li = [10, 20, 23, 7, 73, 90, 17, 88, 62, 100] 

even_li = []
odd_li = []

for i in range(len(li)):

    if li[i] % 2 == 0:
        even_li.append(li[i])
    else:
        odd_li.append(li[i])

print("Even List :",even_li)
print("Odd List :",odd_li)