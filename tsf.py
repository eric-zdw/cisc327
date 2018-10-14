def CreateTransaction(transType, args*):
    if transType = "CRE":
        return "CRE " + args[0] + " 0 00000 " + args[1] + " " + args[2]
    elif transType = "DEL":
        return "DEL " + args[0] + " 0 00000 " + args[1] + " 0"
    elif transType = "SEL":
        return "SEL " + args[0] + " " + args[1] + " 00000 **** 0"
    elif transType = "CAN":
        return "CAN " + args[0] + " " + args[1] + " 00000 **** 0"
    elif transType = "CHG":
        return "CHG " + args[0] + " " + args[2] + " " + args[1] + " **** 0"