
# Q12. Write a program to create three lists of numbers, their squares and cubes.

num = [1, 2, 3, 4, 5, 6]

li2 = []
li3 = []

for i in num:

    square = i ** 2
    li2 = li2 + [square]

    cube = i ** 3
    li3 = li3 + [cube]

print("Numbers :", num)
print("Squares :", li2)
print("Cubes :",li3)