"""
CISC 327: QIES Front End
Group 24
Eric Du (20025626)
Jason Lee (????????)

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
login()
Prompts user for login mode (ie. agent or planner). If mode is invalid,
aborts. Calls TransactionMode(agent/planner) depending on user selection.
"""
def login():
    testinput = input()
    if testinput == "agent":
        print("agent clear")
        TransactionMode("agent")
    elif testinput == "planner":
        print("planner clear")
        TransactionMode("planner")
    else:
        print("wrong")

"""
TransactionMode(mode)
Prompts user for any transaction to begin transaction. Depending on mode, will
run in agent or planner mode with respective transaction permissions.
"""
def TransactionMode(mode):
    validServices = []
    transactionList = []

    fileio.ReadVSF(sys.argv[1], validServices)
    for service in validServices:
        print(service)

    if mode == "agent":
        print("in agent")
    elif mode == "planner":
        print("in planner")

    loggedIn = True
    while (loggedIn):
        testinput = input()
        if testinput == "logout":
            loggedIn = False
            fileio.CreateTSF(sys.argv[2], transactionList)
        elif testinput == "createservice":
            if mode == "planner":
                transactions.CreateService(transactionList, validServices)
            else:
                print("not in planner mode")
        elif testinput == "deleteservice":
            if mode == "planner":
                transactions.DeleteService(transactionList, validServices)
            else:
                print("not in planner mode")
        elif testinput == "sellticket":
            transactions.SellTicket(transactionList, validServices)
        elif testinput == "cancelticket":
            transactions.CancelTicket(transactionList, validServices, mode)
        elif testinput == "changeticket":
            transactions.ChangeTicket(transactionList, validServices, mode)
        print("transactionList is now: ")
        for transaction in transactionList:
            print(transaction)

"""
main()
Start point of program. No transactions allowed except login, which executes
login().

Checks if program was given sufficient number of arguments; otherwise 
terminates.
"""
def main():
    if len(sys.argv) != 3:
        print("incorrect number of arguments")
    else:
        while(True):
            loginInput = input()
            if loginInput == "login":
                login()

main()