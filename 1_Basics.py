print("Welcome to the Simple Interest Calculator")
print("-----------------------------------------")
principal = input("Enter Principal Amount \n")
rate = input("Enter rate of interest \n")
years = input("Enter number of years \n")

principal = float(principal)
rate = float(rate)
years  = float(years)

simple_interest = (principal * rate * years)/100

print("Computed simple_interest = " + str(simple_interest))

