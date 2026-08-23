
# Q9. Write a program of having n number of elements in the list and find out even and odd elements in that list and then create two seperate lists which wll have even elements and other will have odd elements.

li = [10, 25, 11, 33, 50, 65, 80,40,77,90]

even_li = []
odd_li = []

for i in li:

    if ( i % 2 == 0 ):
        even_li = even_li + [i]
    else:
        odd_li = odd_li + [i]

print("Original List :",li)
print("Even Elements :",even_li)
print("Odd Elements:",odd_li)

