def ValidServNumber(num):
    if len(num) != 5:
        print("error: must be length 5")
        return False
    elif num[0] == "0":
        print("error: cannot start with 0")
        return False
    else:
        return True

def ValidServName(name):
    if len(name) < 3 or len(name) > 39:
        print("error: service name invalid length")
    elif name[0] == " " or name[-1] == " ":
        print("error: service name cannot begin or end with space")
    else:
        return True

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

def isNumeric(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

def validNumberOfTickets(num):
    if not isNumeric(num):
        print("error: must be numeric")
        return False
    elif int(num) < 1 or int(num) > 1000:
        print("error: number of tickets out of range")
        return False

def ServiceExistsVSF(num, validServices):
    for service in validServices:
        if num == service:
            return True
    return False

def ServiceExistsTSF(num, transactionList):
    for transaction in transactionList:
        if num == transaction.split()[1] and transaction.split()[0] == "CRE":
            return True
    return False