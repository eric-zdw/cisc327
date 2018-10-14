import validation
import tsf

def CreateService(transactionList, validServices):
    print("now in createservice mode")
    serviceNumber = input()
    if not validation.ValidServNumber(serviceNumber):
        print("not valid service number")
        return
    serviceDate = input()
    if not validation.ValidServDate(serviceDate):
        print("not valid date")
        return
    serviceName = input()
    if not validation.ValidServName(serviceName):
        print("not valid name")
        return
    if validation.ServiceExists(serviceNumber, validServices):
        print("service exists")
        return
    if validation.ServiceExistsTSF(serviceNumber, transactionList):
        print("service exists in TSF")
        return
    transactionList.append(tsf.CreateTransaction("CRE", serviceNumber, serviceName, serviceDate))

def DeleteService(transactionList, validServices):
    print("now in deleteservice mode")
    serviceNumber = input()
    if not validation.ValidServNumber(serviceNumber):
        print("not valid service number")
    else:
        serviceName = input()
        if not validation.ValidServName(serviceName):
            print("not valid name")
        else:
            transactionList.append(tsf.CreateTransaction("DEL", serviceNumber, serviceName))

def SellTicket(transactionList, validServices):
    print("now in sellticket mode")
    serviceNumber = input()
    if not validation.ValidServNumber(serviceNumber):
        print("not valid service number")
    else:
        numTickets = input()
        if not validation.validNumberOfTickets(numTickets):
            print("not valid number of tickets")
        else:
            transactionList.append(tsf.CreateTransaction("SEL", serviceNumber, numTickets))

def CancelTicket(transactionList, validServices):
    print("now in cancelticket mode")
    serviceNumber = input()
    if not validation.ValidServNumber(serviceNumber):
        print("not valid service number")
    else:
        numTickets = input()
        if not validation.validNumberOfTickets(numTickets):
            print("not valid number of tickets")
        else:
            transactionList.append(tsf.CreateTransaction("CAN", serviceNumber, numTickets))

def ChangeTicket(transactionList, validServices):
    print("now in changeticket mode")
    serviceNumber1 = input()
    if not validation.ValidServNumber(serviceNumber1):
        print("not valid source service number")
    else:
        serviceNumber2 = input()
        if not validation.ValidServNumber(serviceNumber2):
            print("not valid destination service number")
        else:
            numTickets = input()
            if not validation.validNumberOfTickets:
                print("not valid number of tickets")
            else:
                transactionList.append(tsf.CreateTransaction("CHG", serviceNumber1, serviceNumber2, numTickets))
