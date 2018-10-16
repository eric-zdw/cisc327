"""
ValidServNumber(num)
Checks service number requirements:
    -Must be length 5
    -Cannot begin with 0
Returns false if requirements aren't met, otherwise return true.
"""
def ValidServNumber(num):
    if not isNumeric(len(num)):
        print("error: must be numeric")
        return False
    if len(num) != 5:
        print("error: must be length 5")
        return False
    elif num[0] == "0":
        print("error: cannot start with 0")
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
ValidServDate(name)
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
        print("error: must be length 8")
        return False
    elif not isNumeric(date):
        print("error: must be numeric")
        return False
    elif int(date[0:4]) < 1980 or int(date[0:4]) > 2999:
        print("error: year out of range")
        return False
    elif int(date[4:6]) < 1 or int(date[4:6]) > 13:
        print("error: month out of range")
        return False
    elif int(date[6:8]) < 1 or int(date[6:8]) > 32:
        print("error: day out of range")
        return False
    else:
        return True

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
        print("error: must be numeric")
        return False
    elif int(num) < 1 or int(num) > 1000:
        print("error: number of tickets out of range")
        return False


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
Checks if num has already been created in the TSF.
Return true if exists, otherwise return false.
"""
def ServiceExistsTSF(num, transactionList):
    for transaction in transactionList:
        if num == transaction.split()[1] and transaction.split()[0] == "CRE":
            return True
    return False