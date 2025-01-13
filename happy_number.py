num = input("Enter number: ")
sum = 0
while sum != 1:
    sum = 0
    for i in range(len(num)):
        sum += int(num[i])**2
    num = str(sum)
if sum == 1:
    print("Happy")
else:
    print("Not Happy")