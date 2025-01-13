ran = int(input("Enter range: "))
for i in range(2,ran+1):
    count = 0
    for j in range(2,i):
        if i%j==0:
            count += 1
            break
    else:
        print(i)