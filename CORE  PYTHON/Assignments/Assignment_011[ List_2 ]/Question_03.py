
# Q3. Python Program to sort the list Accourding to the Second Element in sublist.

li = [[1,3], [2,5], [4,2], [6,1]]

for i in range(len(li)):
    for j in range(i+1 , len(li)):

        if li[i][1] > li[j][1]:
            li[i] , li[j] = li[j] , li[i]

print("Sorted List :",li)