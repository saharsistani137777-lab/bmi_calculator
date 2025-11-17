weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (meters): "))

bmi = weight / (height ** 2)

print("Your BMI:", round(bmi, 2))

if bmi < 18.5:
    print("Status: Underweight")
elif 18.5 <= bmi < 25:
    print("Status: Normal")
elif 25 <= bmi < 30:
    print("Status: Overweight")
else:
    print("Status: Obese")
