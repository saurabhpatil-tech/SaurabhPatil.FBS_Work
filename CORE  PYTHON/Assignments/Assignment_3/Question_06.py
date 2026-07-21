# Q6. Write a program to calculate Profit or Loss :

cp = int(input("Enter Cost Price :"))
sp = int(input("Enter Selling Price :"))

if sp > cp :
    print("Profit", sp-cp )
elif cp > sp :
    print("Loss" , cp-sp )
else:
    print("No Profit No Loss")