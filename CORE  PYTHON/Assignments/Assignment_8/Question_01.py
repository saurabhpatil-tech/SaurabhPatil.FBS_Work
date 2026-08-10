# Q1. Write a program to calculate area of rectangle :

def  areaRectangle (length , breadth):

    area = length * breadth
    return area

length = int(input("Enter Length :"))
breadth = int(input("Enter Breadth :"))

result = areaRectangle (length , breadth)
print("Area of Rectangle :",result)
