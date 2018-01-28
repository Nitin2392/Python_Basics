# Simple code to learn If statements in Python
_input_age = int(input("Please enter your age: \n"))
if _input_age < 18:
    print("You are not eligible to consume any traces of alcohol")
else:
    print("Go Party You Dumbass!")

# Program to check else if statements in Python
_input_marks = int(input("Please enter the marks you have obtained"))
if _input_marks >= 90:
    print("Grade A+")
elif _input_marks >= 80:
    print("Grade B")
elif _input_marks >= 70:
    print("Grade C")
elif _input_marks >= 60:
    print("Grade D")
else:
    print("Fail. Sorry")
