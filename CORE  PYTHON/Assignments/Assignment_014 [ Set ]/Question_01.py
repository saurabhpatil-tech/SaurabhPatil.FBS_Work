
# Q1. Write a Python program to find elements in a given set that are not in
# another set.


s1 = { 10, 20, 30, 40, 50 } 
s2 =  {30, 40, 50, 60, 70 }

res = s1 - s2
print("Elements in first set but not in second set:", res)