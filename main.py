import validation
import services
import tsf
import vsf

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

def TransactionMode(mode):
    validServices = []
    transactions = []
    vsf.ReadVSF("vsf.txt", validServices)
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
            tsf.CreateTSF(transactions)
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

def main():
    while(True):
        testinput = input()
        if testinput == "login":
            login()

main()