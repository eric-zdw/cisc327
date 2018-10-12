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


while(True):
    testinput = input()
    if testinput == "login":
        login()

