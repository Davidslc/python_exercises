while True:
    try:
        gallons = float(input("Please enter the number of gallons of gasoline: "))
        break
    except ValueError:
        print("Invalid entry. Try again")

while True:
    try:
        price = float(input("What is the price of gas? "))
        break
    except ValueError:
        print("Invalid entry. Try again")

liters = float(3.7854)
liters_equivalent = (gallons * liters)
co2 = float(20)
co2_produced = float(gallons * co2)
ethanol = float(115000 / 75700)
ethanol_equivalent = float(gallons * ethanol)
barrels_required = float(gallons / 19.5)
cost = float(gallons * price)


print("Original number of gallons is: %.1f" % (gallons))
print("%.1f gallons is the equivalent of %.2f liters" % (gallons, liters_equivalent))
print("%.1f gallons of gasoline requires %.1f barrels of oil" % (gallons, barrels_required))
print("%.1f gallons of gasoline produces %.1f pounds of CO2" % (gallons, co2_produced))
print("%.1f gallons of gasoline is energy equivalent to %.3f gallons of ethanol" % (gallons, ethanol_equivalent ))
print("%.1f gallons of gasoline requires %.1f US dollars" % (gallons, cost))
print("Thanks for playing")


