def converdecimatobinary(decimalnumber):
    if (decimalnumber <0 or decimalnumber>1024):
        return "Input must be a positive decimal number less than 1024"
    else:
       binarynumber = bin(decimalnumber)[2:]
    
    return binarynumber

decimalnumber = 10
print(converdecimatobinary(decimalnumber))