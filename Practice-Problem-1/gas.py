# Calculates the total cost of gas for a trip using distance, cost per gallon, and miles per gallon.
def gasCost(distance,gallonCost,mpg):

    return distance * (gallonCost / mpg)

total = int(gasCost(100, 2.50, 25))
print(total)
