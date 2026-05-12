operator=input("Enter your operator(+ - / *) : ")
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

if operator == "+":
    result = num1 + num2
    print(f"Your result is {result}")
elif operator == "-":
    result = num1 - num2
    print(f"Your result is {result}")
elif operator == '*':
    result = num1 * num2
    print(f"Your result is {result}")
elif operator == '/':
    result = num1 / num2
    print(f"Your result is {result}")
else:
    print("Please enter a valid operator")