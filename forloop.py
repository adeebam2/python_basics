# for loop
for i in range(10):
    print(i, " ", end = "")
print()

for i in range(0, 11):
    print(i, " ", end = "")
print()

for i in range(0, 11, 2):
    print(i, " ", end = "")
print()

for index, i in enumerate(range(10)):
    print(f"Index: {index} number: {i+1}")
print()

for index, i in enumerate(range(10, 20)):
    print(f"Index: {index} number: {i}")
print()

for i in range(10):
    if i == 3:
        print("i = 3")
        break
    print(i)
print()

for i in range(10):
    if i == 2:
        continue
    print(i)
print()

# Nested for loop
for i in range(10):
    for j in range(2):
        print("*", end = "")
    print()
print()

for i in range(10):
    for j in range(i):
        print("*", end = "")
    print()
print()

'''
hello
this is a 
multiline 
comment okay byee
'''

