# while loop
i = 0
while i <= 10:
    print(i, " ", end = "")
    i += 1
print()

i = 0
while i < 10:
    print(f"{i} ", end = "")
    i += 1
print()

i = 0
while i <= 10:
    if i == 3:
        break
    print(i, " ", end = "")
    i += 1
print()

i = 0
while i <= 10:
    if i == 2:
        i += 1
        continue
    print(i, " ", end = "")
    i += 1
print()