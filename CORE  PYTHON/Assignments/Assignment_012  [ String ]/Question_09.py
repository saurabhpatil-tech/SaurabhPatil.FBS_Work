
# Q9. Python Program to Calculate the Number of Words and the Number of Characters Present in a String.


str = input("Enter String :")

count = 0
words = 1

for i in str:

    count+=1

    if i == " ":
        words+=1


print("Number of Words :",words)
print("Number of Characters :",count)