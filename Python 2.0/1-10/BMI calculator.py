print("Welcome to the BMI Calculator!")
print("Please enter your weight in kg:")
weight = float(input())
print("Please enter your height in centimeters:")
height_cm = float(input())
height_m = height_cm / 100
bmi = weight / height_m**2
print("Your BMI is: " + str(round(bmi, 2)))