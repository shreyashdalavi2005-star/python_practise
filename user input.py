#input()= a function that prompts the user to enter data that return the
#         data as a string
name=input("whats your name: ")
age=input("Whats your age:")
age = int(age)
# OR we could simply use [ age= int(input("Whats your age: ")) ]
age = age + 1
print("happy birthday")
print(f"hello mrs {name}")


print(f"your age is {age}")
