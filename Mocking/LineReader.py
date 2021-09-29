import os

def readFromFile(filename):
    if not os.path.exists(filename):
        raise Exception("Bad File")
    file = open(filename, "r")
    line = file.readline()
    return line