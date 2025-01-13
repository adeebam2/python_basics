interval = int(input("Enter interval: "))

for i in range(1,interval+1):
    sum = 0
    j = str(i)
    c = len(j)
    for digit in j:
        sum = sum + pow(int(digit),c)
    if sum == i:
        print(i)