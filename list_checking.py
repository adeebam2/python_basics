li = []
num = int(input("Enter list size: "))
for i in range(num):
    str = input("Enter list element: ")
    li.append(str)
new_li = li.copy()
new_li.reverse()
if li == new_li:
    print("List is a palindrome")
else:
    print("List is not a palindrome")