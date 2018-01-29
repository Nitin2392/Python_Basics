# Coding challenge part 2.

# Create a list of your favorite food items, the list should have minimum 5 elements.
# List out the 3rd element in the list.
# Add additional item to the current list and display the list.
# Insert an element named tacos at the 3rd index position of the list and print out the list elements.

fav_food_items = ["Dosa", "Idly", "Bread", "Salads", "Rice"]
print(fav_food_items[2])
fav_food_items.append("Bisi Bele Bath")
fav_food_items.insert(3, "Tacos")
print(fav_food_items)

# Coding challenge 3
# Section 3, Lecture 25
# Coding challenge part 3
# Task no 1: Using a for-loop and a range function, print "I am a programmer" 5 times.
# Task no 2: Create a function which displays out the square values of numbers from 1 to 9.

for print_String in range(1,6):
    print("I am a programmer")

def func_square():
    for i in range(1, 10):
        print("i: " +str(i) + " and Square = " + str(i*i))
func_square()