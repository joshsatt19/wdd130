"""v is the volume in liters,
π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches."""

import math
from datetime import datetime

#Calculate volume of the tire
pi = math.pi

print("TIRE VOLUME CALCULATOR:")

w = float(input("Enter the width of the tire in mm: "))
a = float(input("Enter the aspect ratio of the tire: "))
d = float(input("Enter the diameter of the wheel in inches: "))

x = w*a+2540*d
y = w** 2
v = float((pi*y*a*x)/10000000000)

print(f"The approximate volume is {round(v, 2)} liters")

#Saving information and writing in file named volumes.txt

current_date_and_time = datetime.now()
with open("volumes.txt", "a") as volumes_file:
    print(f"{current_date_and_time:%Y-%m-%d}", file=volumes_file)
    print(f"{round(w)}, {round(a)}, {round(d)},", file=volumes_file)
    print(f"{round(v, 2)}", file=volumes_file)

#Ask the customer if they would like to buy the tires they entered

buy = input("Would you like to buy the tires with these specific dimensions? Answer Y (yes) or N (no): ")

while buy != "Y" and buy != "N":
        buy = input("Please enter answer Y (yes) or N (no): ")
        

if buy == "Y":
    phone_number = input("Please enter your phone number: ")

    while len(phone_number) != 10 or not phone_number.isdigit():
         
         phone_number = input("Please enter a valid 10 digit phone number: ")

#Saves phone number to volumes.txt file

    with open("volumes.txt", "a") as volumes_file:

        print(f"{phone_number}", file=volumes_file)

    print("Thank you, your order has been placed. Have a nice day!")
else:

    print("Thank you, have a nice day!")