def Calcualteafterdiscountamount (ActualPrice,discountPercentage):
    discountamount = (ActualPrice *discountPercentage)/100

    Afterdiscountamount = (ActualPrice-discountamount)
    return Afterdiscountamount


ActualPrice = int(input('Please enter Actual Price: '))
discountPercentage = int(input('Please enter discount Percentage: '))
ActualPrice = Calcualteafterdiscountamount(ActualPrice ,discountPercentage)

print (ActualPrice)