li=[]

size = int(input("Enter number of elements: "))
for i in range(size):
    number = int(input("Enter element: "))
    li.append(number)

r = int(input("Enter number of rotations: "))

for i in range(r):
    temp = li[0]
    for j in range(size-1):
        li[j] = li[j+1]
    li[-1] = temp

for i in range(0,size):
    print(li[i], end=" ")