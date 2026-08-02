# Q3.  Accept no.of passengers from user and per ticket cost.
# Then accept age of each passenger and then calculate total amount to ticket to travel for all of them based on following condition:

# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.


n = int(input("Enter number of passengers: "))
ticket_price = float(input("Enter per ticket price: "))

total_price = 0

for i in range(1, n + 1):

    age = int(input(f"Enter age of passenger {i}: "))

    if age < 12:
        total_price += ticket_price * 0.70

    elif age > 59:
        total_price += ticket_price * 0.50

    else:
        total_price += ticket_price

print("Total amount to pay =", total_price)