
# Q10. Write a program to remove all occurrence of a given element in the list.


li = [22, 45, 90, 33, 22, 45, 70, 22, 80]

num = int(input("Enter Number you want to remove :"))

new_li = []

for i in li:

    if i != num :
        new_li = new_li + [i]

print("Original List :",li)
print(f"After Removing {num} :",new_li)