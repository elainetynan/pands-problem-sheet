# bmi.py
# This program calculates a body mass index given a height and weight
# The input must be in centimentres and kilograms
# Author: Elaine Tynan

print("~~~~~~~~~~~~~~~~")
# Input
cm = float(input("Please enter your height in cm: "))
kg = float(input("Please enter your weight in kg: "))

# Convert cm to meters
mtr = cm/100

# Calculate bmi
bmi = kg/mtr**2

# Output
print ("Your BMI is {:.2f}".format(bmi))
print("~~~~~~~~~~~~~~~~")