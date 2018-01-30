# File handling is a major concept in Python
# The following program reads, writes and appends to a file
# For the purpose of explanation, I am creating a new text file in the same directory called "trial.txt"

# To write to a file. Currently Trial.txt is empty
file = open("Trial.txt", "w")
# Open is the function we have to call when we are to open a file
# There are three modes - r for read, w for write and a for append
file.write("This is the first line that I am writing to the file") # The write function writes to the file
file.close() # Always remember to close the file after we use it

# We shall now read the contents of the file
file = open("Trial.txt", "r")
print(file.read())
# There are different options to read a file
print(file.read(10))  # Reads 10 bytes of data from the file
print(file.readline())  # This command reads one entire line from the file
file.close()

# When we try to write again into the same file, the previous content is overwritten
# To avoid this, we have to use the append mode
file = open("Trial.txt", "a")
file.write("This is the new line")
file.close()
