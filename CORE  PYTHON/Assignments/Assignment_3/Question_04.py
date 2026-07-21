# Q4. Write a program to input all sides of triangle and check wheather the Triangle is valid or not :

a =int(input("Enter Side 1 :"))
b =int(input("Enter Side 2 :"))
c =int(input("Enter Side 3 :"))

if a+b>c and b+c>a and c+a>b :
    print("Triangle is Valid ")
else:
    print("Triangle is Invalid ")