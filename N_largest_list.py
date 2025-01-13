l = []
n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    l.append(num)


l.sort(reverse=True)

print(f"The sorted list is {l}")

N = int(input("Enter N value: "))

for i in range(N):
    print(f"The {i} largest element is {l[i]}")