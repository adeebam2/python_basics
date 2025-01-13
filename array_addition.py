li_1 = []
li_2 = []
sum_li= []

size = int(input("Enter size of array: "))

for i in range(size):
    number = int(input(f"Enter array element{i} for array_1: "))
    li_1.append(number)

for i in range(size):
    number = int(input(f"Enter array element{i} for array_2: "))
    li_2.append(number)

for i in range(size):
    summ = li_1[i]+li_2[i]
    sum_li.append(summ)

for i in range(size):
    print(sum_li[i])