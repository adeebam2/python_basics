l = (1,4,9,16,25,36,49,64,81,100)
s = int(input("Enter number to search: "))
i = 0
while i < len(l):
    if s==l[i]:
        print(f"{s} found at index {i}")
        break
    else:
        i += 1