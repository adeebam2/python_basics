limit = int(input("Enter number of elements in array: "))
my_array = []
sum = 0
for i in range(0,limit):
    my_array.append(int(input(f"Enter element[{i}]: ")))
for i in range(0,limit):
    sum = sum + my_array[i]
print(f"Sum of array elements is {sum}")