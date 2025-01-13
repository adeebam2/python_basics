def add(x,y):
    return (x+y)
def sub(x,y):
    return (x-y)
def multiply(x,y):
    return (x*y)
def div(x,y):
    return (x/y)
i = 1 
while i:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    choice = int(input("Enter choice\n1: Add\n2:Subtract\n3: Multiply\n4: Divide\n"))
    if choice == 1:
        result=add(x,y)
        print(result)
        
    elif choice == 2:
        result=sub(x,y)
        print(result)
        
    elif choice == 3:
        result=multiply(x,y)
        print(result)
        
    else:
        result=div(x,y)
        print(result)
        
    i = int(input("Press 1 to continue else 0 "))
    if i == 0:
        break
