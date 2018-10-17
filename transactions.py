import validation
import fileio

"""
CreateService(transactionList, validServices)
Creates a service using information given by the user. Requests a service number,
date and service number. If information passes validation checks, a CRE transaction 
code is added to transactionList.
"""
def CreateService(transactionList, validServices):
    print("now in createservice mode")
    serviceNumber = input()
    if not validation.ValidServNumber(serviceNumber):
        print("invalid service number")
        return
    serviceDate = input()
    if not validation.ValidServDate(serviceDate):
        print("invalid date")
        return
    serviceName = input()
    if not validation.ValidServName(serviceName):
        print("invalid name")
        return
    if validation.ServiceExistsVSF(serviceNumber, validServices):
        print("service exists in VSF")
        return
    if validation.ServiceExistsTSF(serviceNumber, transactionList):
        print("service has been newly created or newly deleted")
        return
    transactionList.append(fileio.CreateTransaction("CRE", serviceNumber, serviceName, serviceDate))

"""
DeleteService(transactionList, validServices)
Deletes a service using information given by the user. Requests a service number
and service name. If information passes validation checks, a DEL transaction
code is added to transactionList.
"""
def DeleteService(transactionList, validServices):
    print("now in deleteservice mode")
    serviceNumber = input()
    if not validation.ValidServNumber(serviceNumber):
        print("invalid service number")
        return
    serviceName = input()
    if not validation.ValidServName(serviceName):
        print("invalid name")
        return
    if not validation.ServiceExistsVSF(serviceNumber, validServices):
        print("service does not exist")
        return
    if validation.ServiceExistsTSF(serviceNumber, transactionList):
        print("service has been newly created or newly deleted")
        return
    transactionList.append(fileio.CreateTransaction("DEL", serviceNumber, serviceName))

"""
SellTicket(transactionList, validServices)
Sells tickets using information given by the user. Requests a service number
and number of tickets. If information passes service checks, a SEL transaction 
codeis added to transactionList.
"""
def SellTicket(transactionList, validServices):
    print("now in sellticket mode")
    serviceNumber = input()
    if not validation.ValidServNumber(serviceNumber):
        print("invalid service number")
        return
    numTickets = input()
    if not validation.validNumberOfTickets(numTickets):
        print("invalid number of tickets")
        return
    if not validation.ServiceExistsVSF(serviceNumber, validServices):
        print("service does not exist")
        return
    if validation.ServiceExistsTSF(serviceNumber, transactionList):
        print("service has been newly created or newly deleted")
        return
    transactionList.append(fileio.CreateTransaction("SEL", serviceNumber, numTickets))

"""
CancelTicket(transactionList, validServices)
Cancels tickets using information given by the user. Requests a service number
and number of tickets. If information passes service checks, a CAN transaction 
code is added to transactionList.

Note that the number of tickets sold this session is determined by reading the
transactionList for the number of tickets sold in prior transactions. If
loginMode is "agent", this value will be checked for ticket limits.
"""
def CancelTicket(transactionList, validServices, loginMode):
    print("now in cancelticket mode")
    serviceNumber = input()
    if not validation.ValidServNumber(serviceNumber):
        print("invalid service number")
        return

    numTickets = input()
    if not validation.validNumberOfTickets(numTickets):
        print("invalid number of tickets")
        return
    ticketsCancelled = int(numTickets) + validation.TicketsServiced(serviceNumber, "CAN", transactionList)
    if ticketsCancelled > 10 and loginMode == "agent":
        print("cannot cancel more than 10 tickets of same service in agent mode")
        return
    totalTicketsCancelled = int(numTickets) + validation.AllTicketsServiced("CAN", transactionList)
    if totalTicketsCancelled > 20 and loginMode == "agent":
        print("cannot cancel more than 20 tickets in agent mode") 
        
    if not validation.ServiceExistsVSF(serviceNumber, validServices):
        print("service does not exist")
        return
    if validation.ServiceExistsTSF(serviceNumber, transactionList):
        print("service has been newly created or newly deleted")
        return
    transactionList.append(fileio.CreateTransaction("CAN", serviceNumber, numTickets))

"""
ChangeTicket(transactionList, validServices)
Changes tickets using information given by the user. Requests two service numbers
and number of tickets. If information passes service checks, a CHG transaction 
code is added to transactionList.

Note that the number of tickets sold this session is determined by reading the
transactionList for the number of tickets sold in prior transactions. If
loginMode is "agent", this value will be checked for ticket limits.
"""
def ChangeTicket(transactionList, validServices, loginMode):
    print("now in changeticket mode")
    serviceNumber1 = input()
    if not validation.ValidServNumber(serviceNumber1):
        print("invalid source service number")
        return
    if not validation.ServiceExistsVSF(serviceNumber1, validServices):
        print("source service does not exist")
        return
    if validation.ServiceExistsTSF(serviceNumber1, transactionList):
        print("source service has been newly created or newly deleted")
        return

    serviceNumber2 = input()
    if not validation.ValidServNumber(serviceNumber2):
        print("invalid destination service number")
        return
    if not validation.ServiceExistsVSF(serviceNumber2, validServices):
        print("destination service does not exist")
        return
    if validation.ServiceExistsTSF(serviceNumber2, transactionList):
        print("destination service has been newly created or newly deleted")
        return

    numTickets = input()
    if not validation.validNumberOfTickets:
        print("invalid number of tickets")
        return
    totalTicketsCancelled = int(numTickets) + validation.AllTicketsServiced("CHG", transactionList)
    if totalTicketsCancelled > 20 and loginMode == "agent":
        print("cannot cancel more than 20 tickets in agent mode") 
    transactionList.append(fileio.CreateTransaction("CHG", serviceNumber1, serviceNumber2, numTickets))
