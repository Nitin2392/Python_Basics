# This is a sample program written by me to check if I've understood all the List functions concept

list_user = ["Dark Knight", "Inception", "Titanic", "Avatar"]
print("Hey. This is our current movie list and we're looking for new additions to our database \n")
print(list_user)
a = input("\n Want a new movie to be added to the list ? Input Y or N \n")
if a == 'Y':
    b = input("Do you wish to add your movie to the end of the list (Choose A) or \n"
              "do you want ot insert the movie in between (Choose B) ?  \n")
    if b == 'A':
        c = input("Sure. Why not ? Please enter the name of the movie \n")
        list_user.append(c)
        print("Thank you. Our list is growing. \n " + str(list_user))
    elif b == 'B':
        c = int(input("Sure. At what position do you want to add your movie ? \n The current length"
                  "of the list is - "+ str(len(list_user)) + "\n Please enter your option below: \n"))
        if c <= len(list_user):
            d = input("\n Great. Give us a movie name and we will add it at position - " +str(c) + "\n")
            list_user.insert(c-1, d)
            print("Thank you. Our list is growing. \n " + str(list_user))
        else:
            print("I'm sorry. Looks like you got the wrong position there bud. Better luck next time")
    else:
        print("Hahah! Lol. Nice try. But the program won't work for wrong inputs bud!")
else:
    input("Thanks for your time and space :) We wish to see you back")