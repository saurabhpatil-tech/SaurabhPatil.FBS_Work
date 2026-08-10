# Q3. Write a program to find sum of following series using functions :

#  b .  1! + 2! + 3! + 4! + ...... + n!

def series (n):

    sum = 0 
    fact = 1 
    for i in range(1 , n+1):
        fact *= i
        sum+=fact
    return sum

n = int(input("Enter N :"))

result = series(n)
print("Sum of Factorial Series:",result)
