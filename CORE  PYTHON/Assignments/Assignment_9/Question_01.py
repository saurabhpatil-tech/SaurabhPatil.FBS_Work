
# Q1. Write a program to find sum of following series using recursive function :
#  i . 1! + 2! + 3! + 4! +.....+ n!

def fact(n):
    if  n == 0 or n == 1 :
        return 1
    return n * fact(n-1)

def factSum(n):
    if n == 1:
        return 1
    return fact(n) + factSum(n-1)

n = int(input("Enter Number :"))
res = factSum(n)
print(res)