#Python calculator
print("choice1= 'addition',choice2 = 'subtraction',choice3 = 'multiplication',choice4 = 'division'")
choose = input("Enter your choice(1 to 5):")
if choose == '1':
    a= int(input("Enter your first number"))
    b= int(input("Enter your second number"))
    resuit= a+b
    print(f"addition is:{a}+{b}={result}")
elif choose == '2':
    a= int(input("Enter your first number"))
    b= int(input("Enter your second number"))
    result= a-b
    print(f"subtraction is :{a}-{b}={result}")
elif choose == '3':
    a= int(input("Enter your first number"))
    b= int(input("Enter your second number"))
    result= a*b
    print(f"multiplication is :{a}*{b}={result}")
elif choose == '4':
    a= int(input("Enter your first number"))
    b= int(input("Enter your second number"))
    result= a/b
    print(f"division is :{a}//{b}={result}")
else:
    print("Please enter a valid choice")


