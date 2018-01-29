# This episode we try to understand the significance of Function parameters and modules

def func_to_Add(a,b):
    print(a+b)

func_to_Add(200,-123)
func_to_Add("Nitin ", "Rangarajan")

# To make the function return a value:

def return_func(a,b,c):
    return (a*b)-c

print(str(return_func(3,4,5))) # Make a function call here

# Passing function call as function arguments to another function
def calc_sum(a,b):
    return a+b
def calc_square(a):
    return a * a

print(str(calc_square(calc_sum(3,4)))) # Here we are passing the method call as arguments to another method

# Modules in Python
# Modules are small chunks of code which have functions in them
# They can be imported and used in our programs to perform some activities.

# In the below program, we shall be creating a virtual dice to understand how the module - "random()" works

import random
for i in range(5):
    res = random.randint(1,6)
    print(res)
