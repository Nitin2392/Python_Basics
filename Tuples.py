# Tuples are immutable data structures - They can be used to store values that cannot be changed

# Tuples can be defined by specifying values inside the parantheses..
tuple_1 = ("Nitin", "Varun", "Ananth")

#.. or without them as well.
tuple_2 = "Mani", "Prashanth", "Abhishek", "Gokul", "Adarsh"

print(tuple_1)
print(tuple_2)

# Tuples are immutable. They cannot be changed

tuple_2[0]  = "Suresh"
print(tuple_2)