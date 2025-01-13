from math import pow
limit = int(input("Enter limit: "))
sum = 0
for i in range(1,limit+1):
    sum = sum + pow(i,3)
print(f"Cube sum of first n natural numbers is {sum}")