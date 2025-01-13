for i in range(0,101):
    sum = 0
    string_number = str(i)
    for j in range(len(string_number)):
        sum += int(string_number[j])**(j+1)
    if sum == i:
        print(i)