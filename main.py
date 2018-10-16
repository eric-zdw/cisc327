"""
CISC 327: QIES Front End
Group 24
Eric Du (20025626)
Jason Lee (????????)

Intended input files:
Valid Services File; "vsf.txt"

Intended output files:
Transaction Summary File; "tsf.txt"

Intended usage:
python main.py [vsf] [tsf]
"""

import validation
import services
import tsf
import vsf
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
    transactions = []
    vsf.ReadVSF(sys.argv[1], validServices)
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
            tsf.CreateTSF(sys.argv[2], transactions)
        elif testinput == "createservice":
            services.CreateService(transactions, validServices)
            print("transactionList is now: ")
            for transaction in transactions:
                print(transaction)
        elif testinput == "deleteservice":
            services.DeleteService(transactions, validServices)
            print("transactionList is now: ")
            for transaction in transactions:
                print(transaction)
        elif testinput == "sellticket":
            services.SellTicket(transactions, validServices)
            print("transactionList is now: ")
            for transaction in transactions:
                print(transaction)
        elif testinput == "cancelticket":
            services.CancelTicket(transactions, validServices)
            print("transactionList is now: ")
            for transaction in transactions:
                print(transaction)
        elif testinput == "changeticket":
            services.ChangeTicket(transactions, validServices)
            print("transactionList is now: ")
            for transaction in transactions:
                print(transaction)

"""
main()
Start point of program. No transactions allowed except login, which executes
login().

Checks if program was given sufficient number of arguments; otherwise ends.
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