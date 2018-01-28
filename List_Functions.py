# In this episode, we shall see how to use basic Python List Functions

# The first function is to observe how to append to a list ?
# Remember, append() is always adding an element to the end of the list and not elsewhere

list_1 = ["Nitin", "Varun", "Adarsh", "Ananth", "Abhishek"]
list_1.append("Gokul")
print(list_1)

# The second function is insert.We can insert any value to any possible location in the list

list_1.insert(3, "Suresh")
print(list_1)

# The third function is to find the length of the list - using len()

print("The length of the list is : " + str(len(list_1)))

# To find at what index a particular element is present, we can use the index function
print("The index of element Adarsh in the list is " + str(list_1.index("Adarsh")))