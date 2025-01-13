mat = []
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

for i in range(rows):
    li = []
    for j in range(columns):
        number = int(input(f"Enter array element{i}{j} :"))
        li.append(number)
    mat.append(li)


for i in range(rows):
    for j in range(columns):
        print(mat[j][i], end=" ")
    print()