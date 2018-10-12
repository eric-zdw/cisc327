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
    loggedIn = True
    while (loggedIn):
        print("in agent")
        testinput = input()
        if testinput == "logout":
            loggedIn = False

def planner():
    loggedIn = True
    while (loggedIn):
        print("in planner")
        testinput = input()
        if testinput == "logout":
            loggedIn = False
        elif testinput == "createservice":
            createservice()

def createservice():
    print("now in createservice mode")
    serviceNumber = input()
    if len(serviceNumber) != 5:
        print("error: must be length 5")
    elif serviceNumber[0] == "0":
        print("error: cannot start with 0")
    else:
        serviceDate = input()
        if len(serviceDate) != 8:
            print("error: must be length 8")
        elif not isNumeric(serviceDate):
            print("error: must be numeric")
        elif int(serviceDate[0:4]) < 1980 or int(serviceDate[0:4]) > 2999:
            print("error: year out of range")
        elif int(serviceDate[4:6]) < 1 or int(serviceDate[4:6]) > 13:
            print("error: month out of range")
        elif int(serviceDate[6:8]) < 1 or int(serviceDate[6:8]) > 32:
            print("error: day out of range")
        else:
            serviceName = input()
            if len(serviceName) < 3 or len(serviceName) > 39:
                print("error: service name invalid length")
            elif serviceName[0] == " " or serviceName[-1] == " ":
                print("error: service name cannot begin or end with space")



def isNumeric(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

while(True):
    testinput = input()
    if testinput == "login":
        login()

