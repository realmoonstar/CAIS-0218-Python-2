#This function takes a list of item prices, adds them together, applies a 6% sales tax, and returns the final total.
def cartTotal(prices):
    prices = [1.99,2.99,3.99]
    total = prices[0] + prices[1] + prices[2]
    total += total * 0.06
    taxTotal = total
    return taxTotal
prices = [1.99,2.99,3.99]

print(cartTotal(prices))
