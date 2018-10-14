def ReadVSF(filename, validServices):
    fstream = open(filename, "r")
    for service in fstream:
        validServices.append(service.rstrip())