#problem 3
def gasCost(distance,gallonCost,mpg):

    return distance * (gallonCost / mpg)

total = int(gasCost(100, 2.50, 25))
print(total)