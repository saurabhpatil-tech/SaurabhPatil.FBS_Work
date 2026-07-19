# Q9. Write a program to swap two numbers without using third variable :

x = int(input("Enter value of x :"))
y = int(input("Enter value of y :"))

# x , y = y , x         # python technique to swap 

x = x + y
y = x - y
x = x - y 


print(f"After Swapping : x={x}  and  y={y} " )
