l = []
n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    l.append(num)


l.sort(reverse=True)

print(f"Sorted list is {l}")
print(f"Second largest element is {l[1]}")