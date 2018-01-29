# The Range function plays a vital role in Python. Specifies a range for a sequence

a1 = list(range(1,10)); print(a1)
b1 = list(range(1,100,5)); print(b1)

#It is important to note that the range can only set for numbers
# range_alp = list(range('A','Z',1))
# print(range_alp)

# We can also define functions in Python as follows
# Functions improve code-reusability


def func_to_add_two_numbers():
    a = int(input("Please enter number 1"))
    b = int(input("Please enter number 2"))
    print("The sum of " + str(a) + " and " + str(b) + " is " + str(a+b))


func_to_add_two_numbers()