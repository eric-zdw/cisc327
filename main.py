while(True):
    testinput = input()
    if testinput == "login":
        testinput = input()
        if testinput == "agent":
            print("agent clear")
        elif testinput == "planner":
            print("planner clear")
        else:
            print("wrong")