# Q7. Find the Sum of Three Digit No :

num = int(input("Enter Three Digit Number :"))

d1 = num % 10
num = num // 10 

d2 = num % 10
num = num // 10 

d3 = num % 10
num = num // 10 

Sum = d1 + d2 + d3
print("Sum of Three Digit No :",Sum)
