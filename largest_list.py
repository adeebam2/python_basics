l = []
n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    l.append(num)

largest = l[0]

for i in range(n):
    if l[i]>largest:
        largest = l[i]


print(largest)