# Q7. Program to find Root of Quadratic Equation :

a = float(input("Enter value of a :"))
b = float(input("Enter value of b :"))
c = float(input("Enter value of c :"))

d = b**2 - 4*a*c

Root1 = ( -b + d**0.5 ) / ( 2*a )
Root2 = ( -b - d**0.5 ) / ( 2*a )

print( "Root1 is :",Root1 )
print( "Root2 is :",Root2 )