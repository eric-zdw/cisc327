"""
validation.py
Helper functions to validate correctly formatted service numbers, dates, etc.
"""

"""
ValidServNumber(num)
Checks service number requirements:
    -Must be length 5
    -Cannot begin with 0
Returns false if requirements aren't met, otherwise return true.
"""
def ValidServNumber(num):
    if not isNumeric(len(num)):
        print("error: service number must be numeric")
        return False
    if len(num) != 5:
        print("error: service number must be length 5")
        return False
    elif num[0] == "0":
        print("error: service number cannot start with 0")
        return False
    else:
        return True

"""
ValidServName(name)
Checks service name requirements:
    -Must be length 3-39
    -Cannot begin or end with 0
    -Cannot use symbols besides '
Returns false if requirements aren't met, otherwise return true.
"""
def ValidServName(name):
    if len(name) < 3 or len(name) > 39:
        print("error: service name invalid length")
    elif name[0] == " " or name[-1] == " ":
        print("error: service name cannot begin or end with space")
    else:
        return True

"""
ValidServDate(date)
Checks service date requirements:
    -Must be length 8
    -Must be numeric
    -Year must be 1980-2999
    -Month must be 1-12
    -Day must be 1-31
Returns false if requirements aren't met, otherwise return true.
"""
def ValidServDate(date):
    if len(date) != 8:
        print("error: service date must be length 8")
        return False
    elif not isNumeric(date):
        print("error: service date must be numeric")
        return False
    elif int(date[0:4]) < 1980 or int(date[0:4]) > 2999:
        print("error: service year out of range")
        return False
    elif int(date[4:6]) < 1 or int(date[4:6]) > 13:
        print("error: service month out of range")
        return False
    elif int(date[6:8]) < 1 or int(date[6:8]) > 32:
        print("error: service day out of range")
        return False
    else:
        return True

"""
ValidNumberOfTickets(num)
Checks service number requirements:
    -Must be length 3-39
    -Cannot begin or end with 0
    -Cannot use symbols besides '
Returns false if requirements aren't met, otherwise return true.
"""
def validNumberOfTickets(num):
    if not isNumeric(num):
        print("error: number of tickets must be numeric")
        return False
    elif int(num) < 1 or int(num) > 1000:
        print("error: number of tickets out of range")
        return False
    else:
        return True

"""
ServiceExistsVSF(num, validServices)
Checks if num is already in the VSF.
Return true if exists, otherwise return false.
"""
def ServiceExistsVSF(num, validServices):
    for service in validServices:
        if num == service:
            return True
    return False

"""
ServiceExistsTSF(num, transactionList)
Checks if num has been created or deleted in the TSF.
Return true if exists, otherwise return false.
"""
def ServiceExistsTSF(num, transactionList):
    for transaction in transactionList:
        if num == transaction.split()[1] and transaction.split()[0] == "CRE":
            return True
        if num == transaction.split()[1] and transaction.split()[0] == "DEL":
            return True
    return False

"""
TicketsServiced(serviceNum, transType, transactionList)
Checks transactionList for the number of tickets serviced for a specified
service number and transaction type. transType determines what type of 
transaction will be tracked (ie. CAN or CHG). Returns the number of tickets
serviced for the specified transaction type and service number.
"""
def TicketsServiced(serviceNum, transType, transactionList):
    ticketsServiced = 0
    for transaction in transactionList:
        if transaction.split()[0] == transType and transaction.split()[1] == serviceNum:
            ticketsServiced += transaction.split()[2]
    return ticketsServiced

"""
AllTicketsServiced(serviceNum, transType, transactionList)
Checks transactionList for the number of tickets serviced for a specified
transaction type (tracks ALL service numbers). transType determines what type of 
transaction will be tracked (ie. CAN or CHG). Returns the number of tickets
serviced for the specified transaction type.
"""
def AllTicketsServiced(transType, transactionList):
    ticketsServiced = 0
    for transaction in transactionList:
        if transaction.split()[0] == transType:
            ticketsServiced += transaction.split()[2]
    return ticketsServiced

"""
isNumeric(str)
Returns true if str can be converted to integer, returns false otherwise.
"""
def isNumeric(str):
    try:
        int(str)
        return True
    except ValueError:
        return False