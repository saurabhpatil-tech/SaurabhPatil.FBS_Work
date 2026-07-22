# Q10. WAP to check if given number is Perfect number :

num = int(input("Enter number :"))

sum = 0
for i in range (1 , num):
    if (num % i == 0):
        sum += i 

if ( sum == num ):
    print(f"{num} is Perfect number ")
else:
    print(f"{num} is Not Perfect number")