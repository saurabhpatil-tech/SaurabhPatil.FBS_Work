# Q3. Convert distance given in feet and inches into meter and centimeter :

feet = float(input("Enter Distance in Feet :"))
inches = float(input("Enter Distance in inches : "))

total_inches = feet*12 + inches
cm = total_inches*2.54
meter = cm / 100

print("Centimeter :",cm)
print("Meter :",meter)
