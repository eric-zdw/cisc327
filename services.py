def CreateService():
    print("now in createservice mode")
    serviceNumber = input()
    if not ValidServNumber(serviceNumber):
        print("not valid service number")
    else:
        serviceDate = input()
        if not ValidServDate(serviceDate):
            print("not valid date")
        else:
            serviceName = input()
            if not ValidServName(serviceName):
                print("not valid name")

def DeleteService():
    print("now in deleteservice mode")
    serviceNumber = input()
    if not ValidServNumber(serviceNumber):
        print("not valid service number")
    else:
        