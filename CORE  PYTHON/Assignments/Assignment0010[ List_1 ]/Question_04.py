
# Q4. Write a program to reverse the list.

li = [10, 20, 30, 40, 50]

rev =[]
num = len(li)-1

while ( num >= 0 ):
    rev = rev + [li[num]]
    num = num - 1

print("Reverse List :", rev) 


# method 2 --

# res = li[::-1]
# print("Reverse List :" , res)



# method 3 ---

# li.reverse()
# print("Reverse List :",li)