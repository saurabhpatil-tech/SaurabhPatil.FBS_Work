# Q10. Write a program to reverse three-digit Number :

num = int(input("Enter Three Digit Number :"))

d1 = num % 10
num = num // 10 

d2 = num % 10
num = num // 10 

d3 = num % 10
num = num // 10 

Rev = d1*100+d2*10+d3

print("Reverse of Three Digit No :",Rev)
