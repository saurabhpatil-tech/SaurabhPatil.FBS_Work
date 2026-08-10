#  Q2. Write a program to calculate area of Circle :
 
def areaCircle ( r ):

    area = 3.14 * r**2
    return area

radius = int(input("Enter radius :"))

result = areaCircle(radius)
print("Area of Circle :",result)