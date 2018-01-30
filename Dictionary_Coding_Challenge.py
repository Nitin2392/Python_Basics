# Sample coding challenges for Dictionaries

dict_prices_products = {
    "Soap":5,
    "Books":1,
    "Furniture":17,
    "Food":7
}
print("List of Products available right now")
for element in dict_prices_products:
    print(element)
user_input = input("Please choose  a product from one of the above choices and we will inform the price \n")
if user_input in dict_prices_products:
    faf = "The price for {0} is {1}".format(user_input, dict_prices_products[user_input])
    print(faf)
else:
    print("The product {0} is not present in our list".format(user_input))

# List all odd numbers in python from 1 tp 100
# We can use list comprehensions

list_odd = [x for x in range(1,101) if x%2 !=0]
print(list_odd)