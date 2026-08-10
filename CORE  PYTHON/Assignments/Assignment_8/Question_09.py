# Q9. Write a program to check if entered number is a Palindrome or not :


def palindrome(n):

    rev = 0

    while(n > 0):
        d = n % 10
        rev = rev * 10 + d
        n = n // 10

    return rev


n = int(input("Enter Number :"))
result = palindrome(n)

if n == result:
    print("Palindrome Number")
else:
    print("Not Palindrome Number")