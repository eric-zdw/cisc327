def CreateTransaction(transType, *args):
    if transType == "CRE":
        return "CRE " + args[0] + " 0 00000 " + args[1] + " " + args[2] + "\n"
    elif transType == "DEL":
        return "DEL " + args[0] + " 0 00000 " + args[1] + " 0" + "\n"
    elif transType == "SEL":
        return "SEL " + args[0] + " " + args[1] + " 00000 **** 0" + "\n"
    elif transType == "CAN":
        return "CAN " + args[0] + " " + args[1] + " 00000 **** 0" + "\n"
    elif transType == "CHG":
        return "CHG " + args[0] + " " + args[2] + " " + args[1] + " **** 0" + "\n"

def CreateTSF(transactionList):
    fstream = open("tsf.txt", "w")
    for transaction in transactionList:
        fstream.write(transaction)
    fstream.write("EOS 00000 0 00000 **** 0")