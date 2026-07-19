# Q1. Convert the Time entered in hh , min and sec into Seconds :

hh = int(input("Enter Hours :"))
min = int(input("Enter Minutes :"))
sec = int(input("Enter Seconds :"))

Total_Seconds = hh*3600 + min*60 + sec

print("Total Seconds :",Total_Seconds)