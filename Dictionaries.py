# Dictionaries are bat shit crazy and are vital data structures to know for anyone learning Python
# The core concept of Dictionaries is that it is like a list but has a key-value pair
# Every element in a list thuos has a key-value pair

dict_python = {"Nitin":567, "Varun": 908.76}
print(dict_python["Nitin"] + dict_python["Varun"])

dict_food = {"Food_List": ["Salad", "Chapathi", "Rice"], "Thottuka": ["Cheese", "Kootu", "Appalam"]}
print(str(dict_food["Food_List"]) + " and " + str(dict_food["Thottuka"]))

# Dictionary Functions

dict_numbers = {

    1: "Nitin",
    2: "Varun",
    3: "Ananth",
    4: "Manigandan"
}

# The first funcion is to check if a particular key is present in a dictionary
if(3 in dict_numbers):
    print("Present")
if(5 in dict_numbers):
    print("5 is present")
else:
    print("5 is absent")

# The next function - get() is used to get the value for a particular key value

print(dict_numbers.get(4, "Not found"))
print(dict_numbers.get(5)) # This prints none. We can add a custome message to indicate if a key is absent
print(dict_numbers.get(5, " Not found"))