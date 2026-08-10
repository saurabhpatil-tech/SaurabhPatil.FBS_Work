# Q3. Write a program to find sum of following series using functions :

#  c .  1^1 + 2^2 + 3^3 +.......+ n^n

def series (n):

    sum = 0 
    for i in range(1 , n+1):
       
        sum = sum + i**i
    return sum

n = int(input("Enter N :"))

result = series(n)
print("Sum of Series:",result)


