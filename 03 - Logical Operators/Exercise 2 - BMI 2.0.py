# Coded by Lukasz Spychala

# Program calculates BMI and print different phrases based on that BMI.

import os
os.system("cls")

boldTextStart = "\033[1m"
boldTextEnd = "\033[0m"
moveCursorUp = "\033[A"

CENTIMETER_TO_METER = 0.01
MAX_UNDER_WEIGHT_BMI = 18.5
MAX_NORMAL_WEIGHT_BMI = 25
MAX_OVER_WEIGHT_BMI = 30
MAX_OBESE_BMI = 35

print("{}Welcome to the BMI Calculator!{}\n".format(boldTextStart, boldTextEnd))

height = float(input("Please enter your height (cm): {}".format(boldTextStart)))

# Reprinting previous line to add cm at the end of the line.
print("{}{}Please enter your height (cm): {}{} cm{}"
      .format(boldTextEnd, moveCursorUp, boldTextStart, height, boldTextEnd))

weight = float(input("Please enter your weight (kg): {}".format(boldTextStart)))

# Reprinting previous line to add kg at the end of the line.
print("{}{}Please enter your weight (kg): {}{} kg{}\n"
      .format(boldTextEnd, moveCursorUp, boldTextStart, weight, boldTextEnd))

bmi = weight / ((height * CENTIMETER_TO_METER) ** 2)
roundedBmi = round(bmi)

if roundedBmi < MAX_UNDER_WEIGHT_BMI:
    print("Your BMI is {}, you are {}underweight{}.\n".format(roundedBmi, boldTextStart, boldTextEnd))
elif roundedBmi < MAX_NORMAL_WEIGHT_BMI:
    print("Your BMI is {}, your weight is {}normal{}.\n".format(roundedBmi, boldTextStart, boldTextEnd))
elif roundedBmi < MAX_OVER_WEIGHT_BMI:
    print("Your BMI is {}, you are {}overweight{}.\n".format(roundedBmi, boldTextStart, boldTextEnd))
elif roundedBmi < MAX_OBESE_BMI:
    print("Your BMI is {}, you are {}obese{}.\n".format(roundedBmi, boldTextStart, boldTextEnd))
elif roundedBmi >= MAX_OBESE_BMI:
    print("Your BMI is {}, you are {}clinically obese{}.\n".format(roundedBmi, boldTextStart, boldTextEnd))


