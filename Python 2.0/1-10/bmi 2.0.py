import os

os.system('cls' if os.name == 'nt' else 'clear')

print("Welcome to the BMI Calculator!\n")

weight = float(input("Please enter your weight in kg:"))
height_cm = float(input("\nPlease enter your height in centimeters:"))



height_m = height_cm / 100
bmi = weight / height_m**2

print("\nYour BMI is: " + str(round(bmi, 2)) + "\n")

if bmi < 18.5:
    print("You are underweight.\n")
elif bmi < 25:
    print("You have a normal weight.\n")
else:
    print("You are overweight.\n")

print("Thank you for using the BMI Calculator!")