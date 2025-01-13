def result(operator, num1, num2):
    if operator == "+":
        print(num1+num2)
    elif operator == "-":
        print(num1-num2)
    elif operator == "*":
        print(num1*num2)
    elif operator == "/":
        print(num1/num2)
    elif operator == "%":
        print(num1%num2)
    elif operator == "**":
        print(num1**num2)
    else:
        print("Invalid!!!")

def main():
    while 1:
        operator = input("Enter operator (enter exit to end): ")
        if operator == "exit":
            break
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result(operator, num1, num2)
main()