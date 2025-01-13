l = []
n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    l.append(num)

smallest = l[0]

for i in range(n):
    if l[i]<smallest:
        smallest = l[i]

print(smallest)