
# Q14. Python Program to count the occurrences of ach word in a string.

str = input("Enter String :")

words = str.split()

for i in set(words):
    print(i, ":", words.count(i))