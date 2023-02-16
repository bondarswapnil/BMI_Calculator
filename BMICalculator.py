'''
Author : Swapnil Bondar
Description : Python Mini Project: Create BMI calculator in under 1 minute, 
              Body Mass Index or BMI is value calculated from the Mass and Height of an individual.
Date : 17-02-2023
'''



weight = float(input("Enter Your weight in kg: "))

height = float(input("Enter Your height in cm: "))

BMI = weight / height ** 2

if BMI < 18.5:
    print("under weight")

elif BMI < 25:
    print("Healthy weight")

else:
    print("Over weight")