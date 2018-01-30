# We shall be trying to understand basics of Lists in Python
number_list = [19, 23, 42, 12, 3432, 123213]
print(number_list)

movie_names = ["Memento", "Batman", "Dark Knight", "Dark Knight rises", "Interstellar", "Inception" "Dunkirk"]
print(movie_names)
print("My favorite Nolan movie is:- " + movie_names[4])

# Operations using Lists. In this episode, we will check how to implement basic operations using Lists

# How to add an element to a list ?
print(number_list)
number_list[3] = 9090 # This piece of code adds the number to the third position in the list
print(number_list)

# We can add lists to each other and multiply lists to increase the list content

list_1 = [1,3,5,7]
list_2 = [9,11,13,15]
list_3 = list_1 + list_2; print(list_3)

# Likewise, we can also multiply a number to a list

list_4 = ["Nitin", "Adarsh"]
print(list_4 * 5)

# To search a list, we can use the "in" operator

list_5 = ["Apples", "Oranges", "Banana", "Guava"]
if "Apples" in list_5:
    print("Apples is present in the bag")
else:
    print("Apples is absent in the bag")
