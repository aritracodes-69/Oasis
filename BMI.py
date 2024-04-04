def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)
print("Your BMI is:", bmi)
if bmi<18.5:
    print("You are Underweight!")
elif bmi>18.5 and bmi<=25:
    print("You have a Healthy Body Weight!")
elif bmi<30 and bmi>25:
    print("You are Overweight!")
elif bmi>30:
    print("You are Obese!")
else:
    print("Please Provide Proper Details.")