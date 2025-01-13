l = []
n = int(input("Enter number of elements: "))
for i in range(n):
    num = int(input("Enter element: "))
    l.append(num)
sum = 0 
for i in range(n):
    sum = sum+l[i]

print(sum)