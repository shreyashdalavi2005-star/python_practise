#Conditional expression = one line shortcut for if else statement
#                        print or assign one  of the  two values based on the condition
#                         X if condition true else Y

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
#print("positive" if num >= 0 else "negative")
#result = "even" if num  % 2 == 0 else "odd"
max_num = num1 if num1> num2 else num2
print(max_num)


