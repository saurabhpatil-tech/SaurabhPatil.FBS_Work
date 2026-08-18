
# Q8. Write a program to check whether a number is prime or not using recursion :

def prime(num , i):

    if i == num:
        return True

    if num % i == 0 :
        return False

    return prime(num , i+1)

num = int(input("Enter Number :"))

if num < 2:
    print(f"{num} is Not Prime number")
elif prime(num,2):
    print(f"{num} is a Prime number")
else:
    print(f"{num} is Not Prime number")