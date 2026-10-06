
# Q2. Python Program to Remove the nth Index Character from a Non-Empty String.

str = input("Enter a string:")
n = int(input("Enter the index to remove:"))

str2=""

for i in range(len(str)):
    if i != n :
        str2 += str[i]

print("String after removing character:",str2)


# method 2 -->

# res = str[ :n] + str[n+1: ]