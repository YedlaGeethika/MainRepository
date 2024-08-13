def maskedcredicardnumber(creditcardnumber):

    creditcardnumber = str(creditcardnumber)
    if (len(creditcardnumber)<4):
        return "Invalid card number"
        #print ('Invalid number: please verify your credit card number')

    maskedcredicardnumber = '*' * (len(creditcardnumber)-4 )+ creditcardnumber[-4:]
    return maskedcredicardnumber

creditcardnumber = "2321312312312312314"
print (maskedcredicardnumber(creditcardnumber))



