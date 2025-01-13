from math import pow
num = input("Enter number to check armstrong or not: ")
c = len(num)
sum = 0
for i in num:
    i=int(i) 
    sum = sum+pow(i,c)
if sum == int(num):
    print("Armstrong")
else:
    print("Not Armstrong")