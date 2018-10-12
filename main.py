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
    for services in validServices:
        print(services)

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
    if not ValidServNumber(serviceNumber):
        print("not valid service number")
    else:
        serviceDate = input()
        if not ValidDate(serviceDate):
            print("not valid date")
        else:
            serviceName = input()
            if not ValidServName(serviceName):
                print("not valid name")


def ValidServNumber(num):
    if len(num) != 5:
        print("error: must be length 5")
        return False
    elif num[0] == "0":
        print("error: cannot start with 0")
        return False
    else:
        return True

def ValidServName(name):
    if len(name) < 3 or len(name) > 39:
        print("error: service name invalid length")
    elif name[0] == " " or name[-1] == " ":
        print("error: service name cannot begin or end with space")
    else:
        return True

def ValidDate(date):
    if len(date) != 8:
        print("error: must be length 8")
        return False
    elif not isNumeric(date):
        print("error: must be numeric")
        return False
    elif int(date[0:4]) < 1980 or int(date[0:4]) > 2999:
        print("error: year out of range")
        return False
    elif int(date[4:6]) < 1 or int(date[4:6]) > 13:
        print("error: month out of range")
        return False
    elif int(date[6:8]) < 1 or int(date[6:8]) > 32:
        print("error: day out of range")
        return False
    else:
        return True

def isNumeric(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

def ReadVSF(filename, validServices):
    fstream = open(filename, "r")
    for line in fstream:
        service = line
        validServices.append(service)

def main():
    while(True):
        testinput = input()
        if testinput == "login":
            login()

main()