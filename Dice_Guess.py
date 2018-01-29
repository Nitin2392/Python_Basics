# A simple dice game in Python
# Program allows user to input a number and randomly checks if user's guess correlates with random number generated
import random
print("Hello! \n Welcome to the Random Dice Guess Game \n")
print("\n Go ahead. Enter a number of your choice from 1 - 10. Let's see if you can win \n")

user_choice = 'Y'
while(user_choice != 'N'):
    user_input = int(input("Enter input below \n"))
    rand = random.randint(1, 10)
    if user_input == rand:
        print("Wohoo! What a wonderful guess")
        user_choice = input("Want to play again ? Enter Y/N \n")
    else:
        print("Ptchh. Try again.")
        user_choice = input("Want to play again ? Enter Y/N \n")

print("Thanks for playing. Have a nice day")


