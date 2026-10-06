
# Q5. Python Program to Count the Number of Vowels in a String:

str = input("Enter String:")

count = 0

for i in str:
    if i in "AEIOUaeiou":
        count += 1

print("Number of Vowels Present :",count)