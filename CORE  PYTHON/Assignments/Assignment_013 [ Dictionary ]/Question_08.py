
# Q8. Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary.


str = input("Enter String :")

words = str.split()
count = {}

for i in words:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

print(count)