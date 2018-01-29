# Loops work in Python the same way they work in other languages - iterating over a range/set of data

for i in range(1,100,5):
    print(i) #Will print all numbers from 1 - 99 with difference of 5 numbers

# Program to print even numbers between 1 and 20

for i in range(1,21):
    if(i % 2  == 0 ):
        print(i)
    else:
        continue

# Another approach to the same problem
for i in range(1,21,2):
    print(i)

# Loops can iterate over lists as well
birds = ["Eagle", "Chicken", "Crow", "Parrot"]
for i in birds:
    print(i)

# Basic boolean operators in Python

firstName = "Nitin"
lastName = "Rangarajan"
a = 9
b = 10
if(firstName == "Nitin" and lastName == "Rangarajan"):
    if(a+1 == b or b == a):
        print("Both are successful")
    else:
        print("Or condition failed but first name and last name match")
else:
    print("First Name and Last Name don't match")

# While loop in Python

counter = 0
while(counter <= 10):
    print("Haha!")
    counter+=2

