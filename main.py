"""
CISC 327: QIES Front End
Group 24
Eric Du (20025626)
Jason Lee (20026161)

Intended input files:
Valid Services File
Location is determined by first command line parameter.

Intended output files:
Transaction Summary File
Location is determined by second command line parameter.

Intended usage:
python main.py [vsf location] [tsf location]
"""
import transactions
import fileio
import sys

"""
Login()
Prompts user for login mode (ie. agent or planner). If mode is invalid,
aborts. Calls TransactionMode(agent/planner) depending on user selection.
"""
def Login():
    testinput = input()
    if testinput == "agent":
        TransactionMode("agent")
    elif testinput == "planner":
        TransactionMode("planner")
    else:
        print("error: invalid login mode")

"""
TransactionMode(mode)
Prompts user for any transaction to begin transaction. Depending on mode, will
run in agent or planner mode with respective transaction permissions.
"""
def TransactionMode(mode):
    validServices = []
    transactionList = []
    fileio.ReadVSF(sys.argv[1], validServices)

    loggedIn = True
    while (loggedIn):
        userInput = input()

        if userInput == "logout":
            loggedIn = False
            fileio.CreateTSF(sys.argv[2], transactionList)
        elif userInput == "createservice":
            if mode == "planner":
                transactions.CreateService(transactionList, validServices)
            else:
                print("error: not in planner mode")
        elif userInput == "deleteservice":
            if mode == "planner":
                transactions.DeleteService(transactionList, validServices)
            else:
                print("error: not in planner mode")
        elif userInput == "sellticket":
            transactions.SellTicket(transactionList, validServices)
        elif userInput == "cancelticket":
            transactions.CancelTicket(transactionList, validServices, mode)
        elif userInput == "changeticket":
            transactions.ChangeTicket(transactionList, validServices, mode)
        else:
            print("error: invalid transaction type")

        print("transaction list is now:")
        for transaction in transactionList:
            print(transaction)


"""
Main()
Start point of program. No transactions allowed except login, which executes
login().

Checks if program was given sufficient number of arguments; otherwise 
terminates.
"""
def Main():
    if len(sys.argv) != 3:
        print("error: incorrect number of arguments")
    else:
        while(True):
            loginInput = input()
            if loginInput == "login":
                Login()
            else:
                print("error: please login")

Main()