# In this code block, we shall see how to handle Exceptions in Python
# As usual, wrap the code which you feel might throw an Exception inside the try block

import random
def func_random_no_generator(a, user_choice):
    if user_choice == 'Y':
        try:
            var = random.randint(1, 2)
            if a == var:
                print(1234/(a-var))
            else:
                print("Okay. You are saved! ")
        except ZeroDivisionError:
            print("Oops. Your chosen value matched bugger!!")

        finally:
            user_choice = input("Play again ? Y/N \n ")
            a = input("Enter number below \n")
            func_random_no_generator(a,user_choice)

print("Game Rules - You guess a number. If it matches with our choice, you are eaten. If not, you will be saved! \n Let's start with 5")
func_random_no_generator(5,'Y')

