# List Slicing is an important concept in Python

list_slicing = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# To slice the list, we can use the : operator

# The following command slices the list from position 1 to n-1. So [1:5] - 1,2,3 and 4
print(list_slicing[1:5])

# We can also slice with one value specified

print(list_slicing[:8]) # Prints all values from position 0 to position 7
print(list_slicing[5:]) # Prints all values from position 5 to position n

# Interval slicing
print(list_slicing[1:8:2]) # Prints all values from 1 to 7 with intervals of 2

# Reverse a list

print(list_slicing[::-1])
