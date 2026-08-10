# Q7. Write a program to find sum of digit of a number :

def sumDigit(n):

    sum = 0
    while (n > 0):
        d = n % 10
        sum = sum + d
        n = n // 10

    return sum

n = int(input("Enter Number :"))
result = sumDigit(n)
print("Sum of Digit:",result)