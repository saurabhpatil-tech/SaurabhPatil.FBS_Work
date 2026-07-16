# Q5 :- Write a program to enter P,T,R and calculate Compound Interest :

p = float(input(" Enter Principle Amount :"))
t = float(input(" Enter Time :"))
r = float(input(" Enter Rate of Interest :"))

Amount = p * (( 1 + (r / 100 ))) ** t
Ci = Amount - p

print(" Compound Interest : ",Ci)
