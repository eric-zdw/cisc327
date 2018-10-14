import validation
import tsf

def CreateService():
    print("now in createservice mode")
    serviceNumber = input()
    if not validation.ValidServNumber(serviceNumber):
        print("not valid service number")
    else:
        serviceDate = input()
        if not validation.ValidServDate(serviceDate):
            print("not valid date")
        else:
            serviceName = input()
            if not validation.ValidServName(serviceName):
                print("not valid name")
            else:
                tsf.CreateTransaction("CRE", serviceNumber, serviceDate, serviceName)

def DeleteService():
    print("now in deleteservice mode")
    serviceNumber = input()
    if not validation.ValidServNumber(serviceNumber):
        print("not valid service number")
    else:
        serviceName = input()
        if not validation.ValidServName(serviceName):
            print("not valid name")
        else:
            tsf.CreateTransaction("DEL", serviceNumber, serviceName)

def SellTicket():
    print("now in sellticket mode")
    serviceNumber = input()
    if not validation.ValidServNumber(serviceNumber):
        print("not valid service number")
    else:
        numTickets = input()
        if not validation.validNumberOfTickets(numTickets):
            print("not valid number of tickets")
        else:
            tsf.CreateTransaction("SEL", serviceNumber, numTickets)

def CancelTicket():
    print("now in cancelticket mode")
    serviceNumber = input()
    if not validation.ValidServNumber(serviceNumber):
        print("not valid service number")
    else:
        numTickets = input()
        if not validation.validNumberOfTickets(numTickets):
            print("not valid number of tickets")
        else:
            tsf.CreateTransaction("CAN", serviceNumber, numTickets)

def ChangeTicket():
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
                tsf.CreateTransaction("CHG", serviceNumber1, serviceNumber2, numTickets)
