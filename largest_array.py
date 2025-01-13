list = []
num = int(input("Enter number of elements: "))
for i in range(num):
    number = int(input(f"Enter array element{i}: "))
    list.append(number)
maximum = list[0]
for i in range(num):
    if maximum < list[i]:
        maximum = list[i]
print(maximum)
