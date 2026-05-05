#problem 2
def tipCalc(billAmount):
    print("Bill: $"+ str(billAmount))
    tenTip = billAmount * 0.10
    fifteenTip = billAmount * 0.15
    twentyTip = billAmount * 0.20
    print("10% tip: $"+ str(int(tenTip)) + " TOTAL $" + str(int((billAmount + tenTip))))
    print("15% tip: $"+ str(int(fifteenTip))+ " TOTAL $" + str(int((billAmount + fifteenTip))))
    print("20% tip: $"+ str(int(twentyTip))+ " TOTAL $" + str(int((billAmount + twentyTip))))
    #print("Bill: $" + (billAmount)+"10% tip: $"+ str(tenTip) +"TOTAL $" + billAmount)
tipCalc(100)