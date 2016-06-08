weight = int(input("Please enter your weight in pounds: "))
print("Next, enter your height in feet and inches:")
feet = int(input("Enter feet: "))
inches = int(input("Enter inches: "))
mass = (weight * 0.454)
height = (((feet * 12) + (inches)) * 0.0254)
BMI = (mass/(height*height))
print("Your BMI is ", BMI)
if BMI < 18.5:
    print("UNDERWEIGHT")
elif BMI >= 18.5 and BMI < 25:
    print("NORMAL WEIGHT")
elif BMI >= 25 and BMI < 30: 
    print("OVERWEIGHT")
elif BMI >= 30:
    print("OBESE")