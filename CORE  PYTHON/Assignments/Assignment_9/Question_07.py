
# Q7. Write a program to find sum of digits using recursion :

def digitSum(n):

    if n == 0:
        return 0

    d = n % 10
    return d + digitSum (n//10)

n = int(input("Enter Number :"))
res = digitSum(n)
print("Sum of Digits :",res)
