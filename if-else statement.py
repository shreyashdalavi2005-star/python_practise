#if = Do some code only if some condition are true
#   Else Do something else

age = int(input("Enter your age: "))
if age >= 18:
   print("you are old enough to vote")
elif age < 0:
    print("enter a valid age")
else :
    print("you are not old enough to vote")

 #the compiler  will first check the if code and then it will move sequentially downwards

name = input("Enter your name: ")
if name == "":

    print("please enter your name")
else:
    print(f"your nmae is {name}")


for_sale = True
if for_sale:
    print("🤩You can purchase this item🤩")
else:
    print("This item is out of stock23💔🚫12")

