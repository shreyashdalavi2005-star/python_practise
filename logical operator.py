#Logical operator = Evaluate multiple condition( and , or , not)
#                   Or = at least one condition must be  true
#                   and = both condition must be true
#                   not = inverts the conditions( if True , if False)

temp = 23
is_raning = False

if temp>=38 or temp <= 10 or is_raning:
    print("the match will be cancelled")
else :
    print("the match will be as per scheduled")