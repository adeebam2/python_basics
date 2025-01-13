num = int(input("Enter a number to check prime or not: "))
count = 0
for i in range(2,num):
    if num%i==0:
        count += 1
if count >= 1:
    print("Number is not prime")
else:
    print("Number is prime")