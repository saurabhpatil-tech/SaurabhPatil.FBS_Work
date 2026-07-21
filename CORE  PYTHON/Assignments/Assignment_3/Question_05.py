# Q5. Write a program to check wheather the triangle is  equilateral , isosceles or scalene :

a =int(input("Enter Side 1 :"))
b =int(input("Enter Side 2 :"))
c =int(input("Enter Side 3 :"))

if a == b == c :
    print("Triangle is Equilateral ")
elif a==b or b==c or a==c :
    print("Triangle is Isosceles")
else:
    print("Triangle is Scalene")