
# Q9. Write a program to calculate the M to the power N using recursion :

def power(m,n):

    if n == 0:
        return 1
    return m * power(m,n-1)

m = int(input("Enter Number :"))
n = int(input("Enter Number :"))

res = power(m,n)
print(res)
