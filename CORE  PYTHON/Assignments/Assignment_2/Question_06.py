# Q6.  WAP to calculate Total Salary of Employee based on basic , da=10% of basic , ta=12% of basic , hra=15% of basic :

basic = int(input("Enter Basic Salary :"))

da = basic * 10/100
ta = basic * 12/100
hra = basic * 15/100

total_salary = basic + da + ta + hra

print("Total Salary of Employee :",total_salary)