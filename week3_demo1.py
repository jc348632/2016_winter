# Use try except to handle provlematic situation.
# Error occurs when the normal flow of program is disrupted
# ValueError occurs when the input does not tally with the expected type.
# There are 2 parts to exception: Try the risky code
#                                 Except, manage/ contain the error, could have multiple except
"""
flag = True

while(flag):
    try:
        print("1")
        user_input = int(input("Give me number please: "))
        print("2")
        print("You have entered {}".format(user_input))
        print("3")
        flag = False
        print("4")
    except ValueError:
        print("Please enter a valid number.")

try:
    numerator = int(input("Enter the numeretor: "))
    denominator = int(input("Enter the denominator (Enter a non zero): "))
    while denominator == 0:
        print("Cannot ")

"""

"""
1.  When will a ValueError occur? When a non-numeric is entered
2.  When will a eroDivisionError occur? When a zero is entered as denominator
3.  Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

"""
Get a file name from user with extension.
Try open the file using the filename.
Prompt error message if the file does not exist.
Or else, read out the content of the file.

open(), close(), try, except, print()
"""


