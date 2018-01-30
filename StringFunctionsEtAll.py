# We shall start with List Comprehension
# List comprehensions allow us to define rules on what kind of elements need to be present inside a List

# Assume we need squares of elements from 1 to 20 in a list.
# If we go about adding each element manually, it is going to take a lot of time.
# We can thus define rules (list comprehension) for the same

list_squares = [x**2 for x in range(1,21)]
print(list_squares)

#If we want the same list comprehension to be modified to include only even numbers
list_squares = [x**2 for x in range(1,21,2)]
print(list_squares)

list_squares = [x**2 for x in range(1,21) if x%2 == 0]
print(list_squares)

# String Formatting
# This concept is C#'s answer for place holder printing

string_temp = "The difference of {a} and {b} is {c}".format(a=100, b=50, c=100-50)
print(string_temp)

# O/P : The difference of 100 and 50 is 50

list_temp = ["Ananth", "Mani", "Gokul", "Adarsh", "Abhi"]
for i in list_temp:
    c = "Best friend {0} of Nitin is {1}".format(list_temp.index(i), i)
    print(c)

# String Formatting is largely useful in cases of dates
date = [12, 12, 2012]
new_str = "Date of birth is {0}/{1}/{2}".format(date[0],date[1],date[2])
print(new_str)

#   O/P is Date of birth is 12/12/2012

# Join functions for lists
print(list_temp)

# The join function joins a string with a list. Here, we are joining a , between the list elements and storing it as CSV
join_str = ", ".join(list_temp)
print(join_str)
# O/P is Ananth, Mani, Gokul, Adarsh, Abhi

print(": ".join(["We", "Are", "Going", "To", "Join", "With", "Colon"]) )

# O/P is We: Are: Going: To: Join: With: Colon

# The next function is replace

inital_word = "Nitin is the greatest!"
print(inital_word.replace("Nitin", "Everyone"))
# O/P is Everyone is the greatest!

print("Hello there".replace("there", "World"))
# O/P is Hello World

# Starts With and Ends With
new_str = "This string is an important lifeline"
if new_str.startswith("This"): # startswith and endswith returns a boolean value
    if new_str.endswith("lifeline"):
        print("Yahoo")

# Output is Yahoo

# String functions - Upper and Lower

str_temp = "tHiS iS A DuMMy"
print(str_temp.lower() + " and the upper half is " +str_temp.upper())

# O/P is this is a dummy and the upper half is THIS IS A DUMMY

# Numerical functions

print(min(1,2,3,4,-4)) # O/p is -4

print(max(0.3,42,11,-3.56)) # O/p is -42

print(abs(-4.567)) # O/p is 4.567

