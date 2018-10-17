"""
CreateTransaction(transType, *args)
Return a string representing a transaction within a TSF. transType determines
the transaction type used and which arguments correspond to which entry.
"""
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

"""
CreateTSF(filename, transactionList)
Write the contents of transactionList to a new file located at filename.
"""
def CreateTSF(filename, transactionList):
    fstream = open(filename, "w")
    for transaction in transactionList:
        fstream.write(transaction)
    fstream.write("EOS 00000 0 00000 **** 0")

"""
ReadVSF(filename, validServices)
Read file at filename for service numbers and add numbers to list at 
validServices.
"""
def ReadVSF(filename, validServices):
    fstream = open(filename, "r")
    for service in fstream:
        validServices.append(service.rstrip())