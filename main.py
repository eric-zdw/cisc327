import valid
import services
import tsf

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
    ReadVSF("vsf.txt", validServices)
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
    ReadVSF("vsf.txt", validServices)
    for service in validServices:
        print(service)

    loggedIn = True
    while (loggedIn):
        print("in planner")
        testinput = input()
        if testinput == "logout":
            loggedIn = False
        elif testinput == "createservice":
            CreateService()

def ReadVSF(filename, validServices):
    fstream = open(filename, "r")
    for service in fstream:
        validServices.append(service)

def main():
    while(True):
        testinput = input()
        if testinput == "login":
            login()

main()