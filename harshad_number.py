num = input("Enter number: ")
sum = 0
for i in range(len(num)):
    sum += int(num[i])
if int(num)%sum==0:
        print("Number is harshad number")
else:
        print("Number is not harshad number")