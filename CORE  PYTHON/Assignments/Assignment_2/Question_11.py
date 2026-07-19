# Q11. Write a program to accept an integer amount from user and tell minimum number of Notes needed for representing that amount :

amount =int(input("Enter Amount :"))

N2000 = amount // 2000
amount = amount % 2000

N500 = amount // 500
amount = amount % 500

N200 = amount // 200
amount = amount % 200

N100 = amount // 100
amount = amount % 100

N50 = amount // 50
amount = amount % 50

N20 = amount // 20
amount = amount % 20

N10 = amount // 10
amount = amount % 10

print("Notes 2000 =",N2000)
print("Notes 500 =",N500)
print("Notes 200 =",N200)
print("Notes 100 =",N100)
print("Notes 50 =",N50)
print("Notes 20 =",N20)
print("Notes 10 =",N10)
print("Remaining Amount =",amount)
