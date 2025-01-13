#non-decreasing monotonic array means that each element is greater than or equal to previous elements
#non increasing monotonic array means that each element is less than or equal to previous element
li = []
 
size = int(input("Enter size of array: "))

for i in range(0,size):
    number = int(input("Enter array element: "))
    li.append(number)

count = 0

for i in range(0,size-1):
    if li[i] <= li[i+1] or li[i] >= li[i+1]:
        count += 1

if count == size-1:
    print("Array is monotonic")
else:
    print("Array is not monotonic")