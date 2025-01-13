l = []
n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    l.append(num)
l_even = []
for i in range(n):
    if l[i] % 2 == 0:
        l_even.append(l[i])

print(l_even)