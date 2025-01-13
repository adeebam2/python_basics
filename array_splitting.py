li = []
li_1 =[]
li_2 = []
size = int(input("Enter size of array: "))
for i in range (size):
    number = int(input("Enter array element: "))
    li.append(number)
k = int(input("Enter value from where to split: "))
for i in range(0,k):
    li_1.append(li[i])
for j in range(k,size):
    li_2.append(li[j])
li_2.extend(li_1)
for i in range(0,size):
    print(li_2[i], end=" ")
    