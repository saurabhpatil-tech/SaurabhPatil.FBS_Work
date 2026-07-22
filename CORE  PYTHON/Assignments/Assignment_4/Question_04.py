# Q4. WAP to print Factorial of a number :

num = int(input("Enter Number :"))

fact = 1

for i in range (1 , num+1 ):
    fact *= i
print(f"Factorial of {num} : {fact}")