"""
ReadVSF(filename, validServices)
Read file at filename for service numbers and add numbers to list at 
validServices.
"""
def ReadVSF(filename, validServices):
    fstream = open(filename, "r")
    for service in fstream:
        validServices.append(service.rstrip())