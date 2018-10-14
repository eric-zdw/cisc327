def CreateTransaction(transType, *args):
    tsf = open("tsf.txt", "")
    if transType == "CRE":
        tsf.write("CRE " + args[0] + " 0 00000 " + args[1] + " " + args[2])
    elif transType == "DEL":
        tsf.write("DEL " + args[0] + " 0 00000 " + args[1] + " 0")
    elif transType == "SEL":
        tsf.write("SEL " + args[0] + " " + args[1] + " 00000 **** 0")
    elif transType == "CAN":
        tsf.write("CAN " + args[0] + " " + args[1] + " 00000 **** 0")
    elif transType == "CHG":
        tsf.write("CHG " + args[0] + " " + args[2] + " " + args[1] + " **** 0")
    print("transaction file is now: ")
    for transaction in tsf:
        print(transaction)