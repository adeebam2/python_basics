mat_1 = []
mat_2 = []
mat_result = []
#li_1 = []
#li_2 = []
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

for i in range(rows):
    li_1 = []
    for j in range(columns):
        number = int(input(f"Enter element for matrix_1 {i}{j}: "))
        li_1.append(number)
    mat_1.append(li_1)

for i in range(rows):
    li_1 = []
    for j in range(columns):
        number = int(input(f"Enter element for matrix_2 {i}{j}: "))
        li_1.append(number)
    mat_2.append(li_1)

for i in range(rows):
    sum_result = []
    for j in range(columns):
        result = mat_1[i][j]+mat_2[i][j]
        sum_result.append(result)
    mat_result.append(sum_result)

for i in range(rows):
    for j in range(columns):
        print(mat_result[i][j], end=" ")
    print()        