import re

def checkMatch(text):
    regex = "[A-Z][a-z]+"
    #Using re.search() searches the whole string for a match anywhere instead
    # of just from the beginning like re.match does
    if re.search(regex, text):
        return True
    return False


testStrings = ["asdvasdfvd", "ASDFB", "absdfEadasv"]
for i in testStrings:
    print("Checking if string \"",i,"\" matches: ", checkMatch(i))