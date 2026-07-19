# Q5. WAP to calculate Selling price  of Book based on Cost price and Discount :

Cp = int(input("Enter Cost Price of Book :"))
Discount = float(input("Enter Discount :"))

Sp = Cp - (Cp * Discount/100 )

print("Selling Price of Book :",Sp)