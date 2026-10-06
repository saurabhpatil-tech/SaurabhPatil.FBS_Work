
# Q9. Write a program to create three lists of numbers, their squares and cubes.

# li = [1, 2, 3, 4, 5, 6]
num = []
li2 = []
li3 = []

for i in range(1,7):
    
    num.append(i)

    square = i ** 2
    li2.append(square)

    cube = i ** 3
    li3.append(cube)

print("Numbers :", num)
print("Squares :", li2)
print("Cubes :",li3)