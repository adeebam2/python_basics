l = []
n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    l.append(num)
l_odd = []
for i in range(n):
    if l[i] % 2 != 0:
        l_odd.append(l[i])

print(l_odd)