
# Q13. Python Program to count number of digits and letters in a string.

str = input("Enter String :")

letters = 0
digits = 0

for i in str:

    if i.isalpha() == True:
        letters += 1


    if i.isdigit() == True:
        digits += 1


print("Number of Letters :",letters)
print("Number of Digits :",digits)
