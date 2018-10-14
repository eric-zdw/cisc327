import validation
import services
import tsf
import vsf

def login():
    testinput = input()
    if testinput == "agent":
        print("agent clear")
        agent()
    elif testinput == "planner":
        print("planner clear")
        planner()
    else:
        print("wrong")

def agent():
    validServices = []
    transactions = []
    vsf.ReadVSF("vsf.txt", validServices)
    for services in validServices:
        print(services)

    loggedIn = True
    while (loggedIn):
        print("in agent")
        testinput = input()
        if testinput == "logout":
            loggedIn = False

def planner():
    validServices = []
    transactions = []
    vsf.ReadVSF("vsf.txt", validServices)
    for service in validServices:
        print(service)

    loggedIn = True
    while (loggedIn):
        print("in planner")
        testinput = input()
        if testinput == "logout":
            loggedIn = False
        elif testinput == "createservice":
            services.CreateService()

def main():
    while(True):
        testinput = input()
        if testinput == "login":
            login()

main()