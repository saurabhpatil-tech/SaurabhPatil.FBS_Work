# Q11. WAP to check if given number Strong number :

num = int(input("Enter Number :"))

temp = num
sum = 0

while (num > 0):

    d = num % 10

    fact = 1
    for i in range (1,d+1):
        fact *= i
    
    sum += fact
    num = num // 10

if sum == temp :
    print(f"{temp} is Strong no")
else:
    print(f"{temp} is Not Strong no")