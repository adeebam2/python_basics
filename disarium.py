num = input("Enter a number: ")
sum = 0
for i in range(len(num)):
    sum += int(num[i])**(i+1)
if sum == int(num):
    print("Number is disarium")
else:
    print("Number is not disarium")