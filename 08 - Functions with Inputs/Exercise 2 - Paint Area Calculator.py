import os, math
os.system("cls")

def PaintCalculator(can_coverage, x, y):
    cans_needed = (x*y) / can_coverage
    cans_rounded_up = int(math.ceil(cans_needed))
    return cans_rounded_up

print("Welcome to Paint Area Calcualtor!")

can_coverage = float(input("How many square meters "
                              "one can of paint can cover?: "))
x = float(input("What is the length of the area? (m): "))
y = float(input("What is the width of the area? (m): "))

cans_rounded_up = PaintCalculator(can_coverage, x, y)

print(f"To paint {x}m x {y}m area "
      f"you will need: {cans_rounded_up} cans of paint.")

