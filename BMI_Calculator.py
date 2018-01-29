# Body Mass Calculator
# Input Weight and Height

def calc_BMI_Index(height, weight):
    bmi = (weight / (height ** 2))
    return  bmi

height = int(input("Please enter the height in meters \n"))
weight = int(input("Please enter the weight in kg's \n"))
print("BMI Index = " + str(calc_BMI_Index(height, weight)))